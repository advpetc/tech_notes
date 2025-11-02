> Reading notes for Streaming Systems by Tyler Akidau

## Chapter 1: Streaming 101
[Lambda Architecture](http://nathanmarz.com/blog/how-to-beat-the-cap-theorem.html)
For those of you not already familiar with the Lambda Architecture, the basic idea is that you run a streaming system alongside a batch system, both performing essentially the same calculation. The streaming system gives you low-latency, inaccurate results (either because of the use of an approximation algorithm, or because the streaming system itself does not provide correctness), and some time later a batch system rolls along and provides you with correct output.
[“Questioning the Lambda Architecture”](https://oreil.ly/2LSEdqz)
Delightful. Kreps addressed the issue of repeatability in the context of using a **replayable** system like Kafka as the streaming interconnect, and went so far as to propose the Kappa Architecture, which basically means running a single pipeline using a well-designed system that’s appropriately built for the job at hand.
[Apache Flink](http://flink.apache.org/)
Support both streaming and batching.
[“Streaming 101”](http://oreil.ly/1p1AKux)
[“Streaming 102”](http://oreil.ly/1TV7YGU)
[“Why local state is a fundamental primitive in stream processing”](https://oreil.ly/2l8asqf)
If you’re curious to learn more about what it takes to get strong consistency in a streaming system, I recommend you check out the [MillWheel](http://bit.ly/2Muob70), [Spark Streaming](http://bit.ly/2Mrq8Be), and [Flink snapshotting](http://bit.ly/2t4DGK0) papers.


> I propose that instead of attempting to groom unbounded data into finite batches of information that eventually become complete, we should be designing tools that allow us to live in the world of uncertainty imposed by these complex datasets. New data will arrive, old data might be retracted or updated, and any system we build should be able to cope with these facts on its own, with notions of completeness being a convenient optimization for specific and appropriate use cases rather than a semantic necessity across all of them.

Instead of making sure there is no late events, creating a remedy tool to process late events.

**MapReduce** is useful when dealing with bounded data, but not so useful for unbounded data. Batch engines is used for unbounded data, and the most common way to process an unbounded dataset using repeated runs of a batch engine is by windowing the input data into **fixed-size windows** and then processing each of those windows as a separate, bounded data source (sometimes also called _tumbling windows_). However, both cases need to deal with late event data, complicated design of windowing and session (Sessions are typically defined as periods of activity (e.g., for a specific user) terminated by a gap of inactivity).

**Streaming** improves on processing unbounded data.
1. Approximate: [approximate Top-N](http://bit.ly/2JLcOG9)
2. Approximate: [streaming k-means](http://bit.ly/2JLQE6O)
3. Windowing:
	1. **Fixed windows** (aka tumbling windows): **aligned windows** if the window doesn't change based on dataset. However, window size is fixed.
	2. **Sliding window** (aka hopping windows): period (how long next window comes in) and length (how long is the window), if period < length, there is going to be overlaps between windows; if period == length, it's fixed window above. Usually sliding window is aligned.
	3. **Sessions**: dynamic windows composed of sequences of events defined by inactivity. Example of **unaligned** windows.

## Chapter 2: The _What_, _Where_, _When_, and _How_ of Data Processing

[Apache Beam](https://beam.apache.org/)

Apache Beam is a unified programming model and portability layer for batch and stream processing, with a set of concrete SDKs in various languages (e.g., Java and Python). Pipelines written with Apache Beam can then be portably run on any of the supported execution engines (Apache Apex, Apache Flink, Apache Spark, Cloud Dataflow, etc.).

It’s real-world Beam code (and real code is available on [GitHub](http://bit.ly/2KMsDwR) for all examples in this chapter). 

### Terms
A **trigger** is a mechanism for declaring when the output for a window should be materialized (or ready to be outputted and consumed) relative to some external signal.

A **watermark** is a notion of input completeness with respect to event times. A watermark with value of time X makes the statement: “all input data with event times less than X have been observed.” 

An **accumulation** mode specifies the relationship between multiple results that are observed for the same window. Those results might be completely disjointed; that is, representing independent deltas over time, or there might be overlap between them.

`PCollections` : dataset
`PTransforms`: group/aggregate or any other ways to transform dataset A into dataset B


### Example 1: batch with finite data

```java
public static class Example2_1 extends ExampleTransform {
        @Override
        public PCollection<String> expand(PCollection<KV<String, Integer>> input) {
            return input
                .apply(Sum.integersPerKey())
                .apply(ParDo.of(new FormatAsStrings()));
        }

        @Override
        public String[] getExpectedResults() {
            return new String[] { "[global window]: TeamX:48 END_OF_GLOBAL_WINDOW ON_TIME index=0 onTimeIndex=0 isFirst isLast" };
        }
    }

```
* Need to wait until all data have processed
* We need windowing to process infinite data stream

### Example 2: streaming with window
```java
public static class Example2_2 extends ExampleTransform {
        @Override
        public PCollection<String> expand(PCollection<KV<String, Integer>> input) {
            return input
                .apply(Window.<KV<String, Integer>>into(FixedWindows.of(TWO_MINUTES)))
                .apply(Sum.integersPerKey())
                .apply(ParDo.of(new FormatAsStrings()));
        }

        @Override
        public String[] getExpectedResults() {
            return new String[] { "[12:00:00, 12:02:00): TeamX:14 12:01:59 ON_TIME index=0 onTimeIndex=0 isFirst isLast",
                                  "[12:02:00, 12:04:00): TeamX:18 12:03:59 ON_TIME index=0 onTimeIndex=0 isFirst isLast",
                                  "[12:04:00, 12:06:00): TeamX:4  12:05:59 ON_TIME index=0 onTimeIndex=0 isFirst isLast",
                                  "[12:06:00, 12:08:00): TeamX:12 12:07:59 ON_TIME index=0 onTimeIndex=0 isFirst isLast" };
        }
    }
```
* Each window has 2 minutes
* We get several outputs every 2 minutes
* Tigger is when after 2 minutes, we create an output.
* There are two types of **triggers**: 1. Repeated update tiggers and 2. Completeness triggers
* Completeness triggers are less frequently encountered, but provide streaming semantics that more closely align with those from the classic batch processing world. They also provide tools for reasoning about things like missing data and late data, both of which we discuss shortly (and in the next chapter) as we explore the underlying primitive that drives completeness triggers: watermarks.

### Example 3: adding trigger
```java
public static class Example2_3 extends ExampleTransform {
        @Override
        public PCollection<String> expand(PCollection<KV<String, Integer>> input) {
            return input
             .apply(Window.<KV<String, Integer>>into(FixedWindows.of(TWO_MINUTES))
                    .triggering(Repeatedly.forever(AfterPane.elementCountAtLeast(1)))
                          .withAllowedLateness(Duration.standardDays(1000))
                          .accumulatingFiredPanes())
             .apply(Sum.integersPerKey())
             .apply(ParDo.of(new FormatAsStrings()));
        }

        @Override
        public String[] getExpectedResults() {
            return new String[] {
                "[12:00:00, 12:02:00): TeamX:5  12:01:59 EARLY   index=0 isFirst",
                "[12:00:00, 12:02:00): TeamX:14 12:01:59 EARLY   index=1",
                "[12:02:00, 12:04:00): TeamX:7  12:03:59 EARLY   index=0 isFirst",
                "[12:02:00, 12:04:00): TeamX:10 12:03:59 EARLY   index=1",
                "[12:02:00, 12:04:00): TeamX:18 12:03:59 EARLY   index=2",
                "[12:04:00, 12:06:00): TeamX:4  12:05:59 EARLY   index=0 isFirst",
                "[12:06:00, 12:08:00): TeamX:3  12:07:59 EARLY   index=0 isFirst",
                "[12:06:00, 12:08:00): TeamX:11 12:07:59 EARLY   index=1",
                "[12:06:00, 12:08:00): TeamX:12 12:07:59 EARLY   index=2"
            };
        }
    }
```

* `.triggering(Repeatedly.forever(AfterPane.elementCountAtLeast(1)))` : materialize/output the window result every time there is a new event
* note that the window size is still two minutes, but we might get multiple output (can be saved somewhere and polled) depending on if there is a new event 
* Drawback: can have bottleneck when processing a lot of keys (or a lot of events with different keys) -- to solve, we can introduce processing time delay.
### Example 4: add aligned two-minute processing-time boundaries/delays 
```java
 @Override
        public PCollection<String> expand(PCollection<KV<String, Integer>> input) {
            return input
                .apply(Window.<KV<String, Integer>>into(FixedWindows.of(TWO_MINUTES))
                       .triggering(Repeatedly.forever(AfterProcessingTime
                                                      .pastFirstElementInPane()
                                                      .alignedTo(TWO_MINUTES, Utils.parseTime("12:05:00"))))
                       .withAllowedLateness(Duration.standardDays(1000))
                       .accumulatingFiredPanes())
                .apply(Sum.integersPerKey())
                .apply(ParDo.of(new FormatAsStrings()));
        }

        // These panes are kind of funky relative to what's presented in the book, and I'm
        // not 100% sure why yet (it would help if Beam gave access to the processing time
        // at which a given pane was materialized). For now, I wouldn't pay too much attention
        // to this one. :-)
        @Override
        public String[] getExpectedResults() {
            return new String[] {
                "[12:00:00, 12:02:00): TeamX:5  12:01:59 EARLY   index=0 isFirst",
                "[12:00:00, 12:02:00): TeamX:14 12:01:59 ON_TIME index=1 onTimeIndex=0 isLast",
                "[12:02:00, 12:04:00): TeamX:18 12:03:59 EARLY   index=0 isFirst",
                "[12:02:00, 12:04:00): TeamX:18 12:03:59 ON_TIME index=1 onTimeIndex=0 isLast",
                "[12:04:00, 12:06:00): TeamX:4  12:05:59 EARLY   index=0 isFirst",
                "[12:04:00, 12:06:00): TeamX:4  12:05:59 ON_TIME index=1 onTimeIndex=0 isLast",
                "[12:06:00, 12:08:00): TeamX:12 12:07:59 EARLY   index=0 isFirst",
                "[12:06:00, 12:08:00): TeamX:12 12:07:59 ON_TIME index=1 onTimeIndex=0 isLast"
            };
        }
```

* `.alignedTo(TWO_MINUTES, Utils.parseTime("12:05:00"))))`: add the two minutes delay, starting at the processing time from 12:05:00 -- after this timestamp every two minutes we materialize the result, in between we still do aggregation but don't output the aggregation result 
* Drawback: all aggregation result is materialized at the same time for different window
* Use unaligned window to solve this issue
### Example 5: use unaligned two-minute processing-time boundaries/delays
```java
@Override
        public PCollection<String> expand(PCollection<KV<String, Integer>> input) {
            return input
                .apply(Window.<KV<String, Integer>>into(FixedWindows.of(TWO_MINUTES))
                       .triggering(Repeatedly.forever(AfterProcessingTime.pastFirstElementInPane().plusDelayOf(TWO_MINUTES)))
                       .withAllowedLateness(Duration.standardDays(1000))
                       .accumulatingFiredPanes())
                .apply(Sum.integersPerKey())
                .apply(ParDo.of(new FormatAsStrings()));
        }

        @Override
        public String[] getExpectedResults() {
            return new String[] {
                "[12:00:00, 12:02:00): TeamX:5  12:01:59 EARLY   index=0 isFirst",
                "[12:00:00, 12:02:00): TeamX:14 12:01:59 ON_TIME index=1 onTimeIndex=0 isLast",
                "[12:02:00, 12:04:00): TeamX:18 12:03:59 EARLY   index=0 isFirst",
                "[12:02:00, 12:04:00): TeamX:18 12:03:59 ON_TIME index=1 onTimeIndex=0 isLast",
                "[12:04:00, 12:06:00): TeamX:4  12:05:59 EARLY   index=0 isFirst",
                "[12:04:00, 12:06:00): TeamX:4  12:05:59 ON_TIME index=1 onTimeIndex=0 isLast",
                "[12:06:00, 12:08:00): TeamX:12 12:07:59 EARLY   index=0 isFirst",
                "[12:06:00, 12:08:00): TeamX:12 12:07:59 ON_TIME index=1 onTimeIndex=0 isLast"
            };
        }
```
* `.triggering(Repeatedly.forever(AfterProcessingTime.pastFirstElementInPane().plusDelayOf(TWO_MINUTES)))`: add the delay after seeing the every new event and the delay is two minutes
* The load is more evenly distributed (assuming the events arrived at the different time, and processing time has constant delay relative to the event time)

### How to know if we have process all events in a window

**Watermarks** are temporal notions of input completeness in the event-time domain. Worded differently, they are the way the system measures progress and **completeness relative to the event times** of the records being processed in a stream of events (either bounded or unbounded, though their usefulness is more apparent in the unbounded case). Think of watermark as a function: $F(P) \rightarrow E$ which $P$ is the processing time and output a $E$ event time. This function can predict event time based off processing time.

### Example 6: Using watermark
```java
PCollection<KV<Team, Integer>> totals = input
  .apply(Window.into(FixedWindows.of(TWO_MINUTES))
               .triggering(AfterWatermark()))
  .apply(Sum.integersPerKey());
```

* `AfterWatermark()` : the heuristic function that predict processing time given event time. 
* The difference between repeatedly triggers and watermarks is watermarks give us a way to reason about the completeness of our input.
* Drawbacks:
	* Too slow (usually happen on perfect watermark that trying to capture all late event): if there is a very late event being processed, the watermark will be triggered at a very late stage, and we might get the materialized result very late/slow
	* Too fast (usually happen on heuristic watermark that doesn't capture all events): When a heuristic watermark is incorrectly advanced earlier than it should be, it’s possible for data with event times before the watermark to arrive some time later, creating late data.
### Example 7: use watermark and repeated triggers together to capture event
Repeatedly updated triggers provide low-latency updates but no way to reason about completeness, and watermarks tell when it's ready to be materialized, then why not combine these two together.
```java
PCollection<KV<Team, Integer>> totals = input
  .apply(Window.into(FixedWindows.of(TWO_MINUTES))
               .triggering(AfterWatermark()
			     .withEarlyFirings(AlignedDelay(ONE_MINUTE))
			     .withLateFirings(AfterCount(1))))
  .apply(Sum.integersPerKey());
```
* The window size is 2 minutes: meaning every two minutes we create a window   
* Use watermarks: meaning to materialize a output whenever the heuristic function tell us there is a corresponding event triggered at the processing time
	* Add aligned delay of 1 minute: wait 1 more minutes to aggregate result for the event time (e.g. two consecutive events processed at very close time less than one minute, then this will not result in two materialize results because of the aligned delay) 
	* Add late firing: after the non-perfect finish, keep waiting (note that because of repeatedly trigger, we should already have non late event triggered) for exactly one more late event.
* What's good: both perfect and non-perfect heuristic watermarks give similar pattern of output
* What's still missing: in `.withLateFirings(AfterCount(1))` we still don't know how long to wait for the late event -- since we can't just wait forever
### Example 8: adding allowed lateness and watermark
**Lateness horizon**: wait for extra time to capture late event after non-perfect heuristic processing time  
```java
PCollection<KV<Team, Integer>> totals = input
  .apply(Window.into(FixedWindows.of(TWO_MINUTES))
               .triggering(
                 AfterWatermark()
                   .withEarlyFirings(AlignedDelay(ONE_MINUTE))
                   .withLateFirings(AfterCount(1))
               .withAllowedLateness(ONE_MINUTE))
 .apply(Sum.integersPerKey());

```
* `.withAllowedLateness(ONE_MINUTE)`: wait for one minutes after the watermark is materialized, after one minutes, we stop waiting and discard all the late events 

### What can we do after we get the results/panes
* *Discarding*: once a pane is materialized, we discard previous pane/result. So giving `[1,2,3,4]`, we output `[1,2,3,4]`
	* use case: when consumer needs to know each pane's result and them doing the accumulation  
	* Code snippet: 
```java
PCollection<KV<Team, Integer>> totals = input
  .apply(Window.into(FixedWindows.of(TWO_MINUTES))
               .triggering(
                 AfterWatermark()
                   .withEarlyFirings(AlignedDelay(ONE_MINUTE))
                   .withLateFirings(AtCount(1))
               .discardingFiredPanes())
  .apply(Sum.integersPerKey());
``` 
	
* *Accumulating*: once a pane is materialized, we accumulate the current pane with previous pane's result altogether.  Given `[1,2,3,4]`, we get `[1,3,6,10]`
	* use case: storing the accumulated result in database, e.g. HBase, Bigtable, etc.
* *Accumulating and retracting*: once a pane is materialized, only select certain amount of previous panes' values and then do accumulation. The *certain amount* doesn't need to be a fixed number, it can change based on needs. Given `[1,2,3,4]` and the sliding window size being fixed 2, we get `[1,3,5,7]` 
```java
PCollection<KV<Team, Integer>> totals = input
  .apply(Window.into(FixedWindows.of(TWO_MINUTES))
               .triggering(
                 AfterWatermark()
                   .withEarlyFirings(AlignedDelay(ONE_MINUTE))
                   .withLateFirings(AtCount(1))
               .accumulatingAndRetractingFiredPanes())
  .apply(Sum.integersPerKey());
```
This results (default case) in discarding late firing event, and generated two outputs -- one for regular accumulating and one for discarding late events.

