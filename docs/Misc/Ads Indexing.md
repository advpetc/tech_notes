# Overview
The retrieval stage in a system typically does three things:
1. **Eligibility filtering.** Walk an inverted index over targeting attributes (geo, industry, seniority, audience segments, negative targeting) intersected with serving-state constraints: budget remaining, pacing, frequency caps, brand safety, blocklists. This shrinks a few million ads down to maybe thousands or tens of thousands.
2. **Scoring.** Dot product of the user embedding against each surviving ad embedding.
3. **Top-K selection.** Heap down to 100.

## Two Indexes
In the pre-filtering (eligibility search), the inverted index is used to pre-filter all the candidates (ads) by certain rules. The second index is used to find the closest match based on embeddings (ad embeddings and the user embedding). 

The bottleneck for the second indexing is not about computation, but about the number of _fetches_ from memory (especially if the ad server and ad scorer are on separate servers). Splitting the computation into multiple cores can reduce the load on each machine, and can further improve scalability by simply adding more machines. The ad embeddings are partitioned by creativeId; each machine then finds its local top-k, and the results are finally merged together.

# Scoring
During scoring to generate the embedding, we can filter out the ads that are inactive first and then apply the cross join. This will first filter out ineligible ads using an entity cache on the machine to check if the ad is still alive, and then generate the embedding. 

Ads are special because they require ensuring the freshness of the ads served, otherwise it will cause issues with tracking (e.g. late events for reporting vs charging). Below are some examples that are not ads:
- **Spotify** built Annoy, a forest of random-projection trees, for music recommendations. Notably, it's designed around loading a prebuilt file into memory and never updating it, which is fine for music catalogs and a poor fit for ads.
- **Meta** built Faiss, which is the most widely used toolkit for this and implements essentially every variant discussed above, including the clustering and compression combinations.
- **Google** built ScaNN, which is interesting because it compresses embeddings using anisotropic vector quantization, tuned specifically for the kind of inner-product comparison recommendation systems use, rather than for generic (e.g. Euclidean) nearest-neighbor accuracy. That distinction turns out to matter more than people expected.
- **Microsoft** published work on running these structures partly from disk rather than entirely in memory, which is the direction you'd look if inventory outgrew what fits in RAM.


# Common problems on sharding

## Hot partition
A hot partition happens when one shard ends up storing, or serving, far more than its fair share of the data or traffic, while the other shards sit comparatively idle.

For example, suppose ads are split across 10 shards using `advertiserId % 10`. If one advertiser (say, a large retailer running a huge campaign) owns far more active ads than everyone else, every single one of those ads still lands on the same shard, since the remainder of that one advertiser's id never changes. That one shard now has to store and serve far more data and traffic than the other nine, even though the sharding rule looks perfectly even on paper.

Sharding by any id can cause imbalanced ad counts in different shards, so it requires consistent hashing or rehashing.  
* **Consistent hashing** spreads keys across shards more evenly, and, importantly, only moves a small fraction of keys when a shard is added or removed (a plain `id % number_of_shards` scheme reshuffles almost everything the moment the shard count changes). It does not, by itself, fix one single key being too large, like the advertiser example above; that usually needs a finer-grained sharding key (for example, sharding by ad id instead of advertiser id, so one advertiser's ads spread across many shards instead of landing on just one).
* **Rehashing** means periodically redistributing keys across a different, usually larger, number of shards to rebalance load as traffic patterns shift over time, for example splitting one overloaded shard's data across two new shards.

## Wait for the slowest machine
When scoring is split across many machines, the overall request has to wait for every machine to respond before it can return a result. If even one machine is slow, for example because of a garbage-collection pause or a network hiccup, the whole request is held up waiting on that single straggler, even though every other machine already finished. This is sometimes called the straggler problem: if 99 out of 100 machines respond in 20 milliseconds but one takes 500 milliseconds, the overall request still takes 500 milliseconds, since the slowest machine sets the pace for everyone.

* **Accept the truncated result by interrupting the scoring.** Set a deadline, and once it passes, stop waiting for any machines that have not yet responded and return the best results gathered so far. This trades a small amount of completeness, since the best-scoring ad might have lived on the slow machine, for a predictable, bounded response time.
* **Create a timeout and try another replica to do the scoring.** Most systems keep more than one copy, or replica, of each shard for redundancy. If one replica is slow to respond, the request can be quickly resent to a different replica holding the same data instead of continuing to wait, on the assumption that a second copy will respond faster.

## Versioning
A ranking model's embeddings are only meaningful relative to each other if they came from the same version of the model; an embedding produced by version 5 of a model is not guaranteed to mean the same thing, geometrically, as an embedding produced by version 6, even though both are just lists of numbers that look equally valid.

For example, suppose a new model version is deployed and starts producing new user embeddings right away, but the embeddings for millions of existing ads have not been recomputed yet, since regenerating every ad's embedding takes time. If a fresh, new-version user embedding is accidentally scored against one of those old, stale ad embeddings, the resulting similarity score will look like a normal number, but it is really comparing two unrelated coordinate systems, silently producing meaningless rankings.

Only the ad and user embeddings from the same model version can be scored. 
* Put a version stamp on the embeddings to ensure they always match. Every embedding is tagged with the model version that produced it when it is generated, and before two embeddings are scored against each other, their version stamps are checked; if they do not match, that pair is skipped, or the stale side is queued to be refreshed, rather than producing a meaningless score.


# Existing technologies

## Solr
Apache Solr is a search engine built on Lucene, the same indexing library many text-search tools use. Newer versions of Solr let a field store a dense vector, meaning an embedding, alongside each document, and support approximate nearest-neighbor search over those vectors using a graph-based structure called HNSW (Hierarchical Navigable Small World), which finds close matches by hopping across a small, cleverly connected graph instead of comparing against every vector one by one. For scoring, Solr computes a similarity between the query vector (for example, the user embedding) and each candidate document's vector, using dot product, cosine similarity, or Euclidean distance, and uses that similarity directly as the document's score, letting it play the role of the "second index" described earlier in this document.

## ElasticSearch
Elasticsearch, also built on Lucene, offers a very similar capability: a dense vector field type paired with the same kind of approximate nearest-neighbor search over an HNSW graph. Its score is likewise derived from a configurable similarity metric between the query vector and each document's vector (dot product, cosine similarity, Euclidean distance, or a specialized "maximum inner product" mode built for exactly this kind of ranking task). Because the whole graph needs to fit in memory for the search to stay fast, Elasticsearch's vector search runs into the same memory-bound bottleneck described earlier for the second index.

## Vespa
Vespa, originally built at Yahoo, is designed from the ground up to combine retrieval and scoring in one system, rather than treating them as two separate steps stitched together. It represents both queries and documents as tensors, a generalization of vectors and matrices, and lets a scoring function, anywhere from a simple dot product up to a full machine-learning model, run directly inside the serving engine at query time. Vespa also supports doing this in multiple passes: a fast, approximate similarity search narrows a huge set of candidates down to a smaller set, and then a slower, more accurate scoring function re-ranks just that smaller set. This maps closely onto this document's own eligibility, scoring, and top-k pipeline, but running inside a single system instead of across separate ones.

## Twitter's Earlybird
Earlybird is Twitter's real-time, in-memory search engine, also built on Lucene, and its role is closer to this document's "eligibility filtering" stage than to embedding-based scoring. It maintains an inverted index that is constantly updated as new tweets arrive, and retrieves candidates primarily by matching search terms and recency, returning the most recent matching tweets first. Rather than scoring documents with embeddings, Earlybird factors in real-time engagement signals, such as how many retweets, likes, and replies a tweet has received so far, which are continuously updated in the background and folded into its ranking. Heavier, embedding-based scoring in Twitter's broader ranking stack typically happens downstream, in a separate service that re-ranks the candidates Earlybird retrieves.