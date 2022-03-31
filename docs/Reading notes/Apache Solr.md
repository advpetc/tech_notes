## Reading notes for Scaling Apache Solr

Book link: https://www.google.com/books/edition/Scaling_Apache_Solr/WB8ZBAAAQBAJ?hl=en&gbpv=0

### What is Solr
In order to search a document, Apache Solr performs the following operations in sequence:

1.  Indexing: converts the documents into a machine-readable format.
    
2.  Querying: understanding the terms of a query asked by the user. These terms can be images or keywords, for example.
    
3.  Mapping: Solr maps the user query to the documents stored in the database to find the appropriate result.
    
4.  Ranking: as soon as the engine searches the indexed documents, it ranks the outputs by their relevance.
    

Since Apache Solr uses Apache Lucene for indexing and searching, Solr and Lucene index are the same. That means Apache Solr can access indexes generated using Lucene; although, we may just need to modify the Solr schema file to accommodate all the attributes of the Lucene index. Additionally, if Apache Solr is using a different Lucene library, we need to change <luceneMatchVersion> in solrconfig.xml. This is particularly useful when the client would like to upgrade his custom Lucene search engine to Solr without losing data.

### Selected Features

1. Near real-time search: Allow users to search near-real-time updated database.

> Whenever users upload documents to the Solr server, they must run a commit operation, to ensure that the uploaded documents are stored in the Solr repository. A soft commit is a Solr 4.0 introduced feature that allows users to commit fast, by passing costly commit procedures and making the data available for near real-time search.

Soft commit can allow fast search, but data won't be available on a persistent store.

2. Caching: The caching can be performed at filter level (mainly used for filtering), field values (mainly used in facets), query results (top-k results are cached in certain order), and document level cache.



