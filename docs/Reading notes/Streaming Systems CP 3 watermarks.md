> Reading notes for Streaming Systems by Tyler Akidau

## Chapter 3: Watermarks

* **In flight**: event has been received but not completed.
* **Watermarks**: is a monotonically increasing timestamp of the oldest work not yet completed
	* **Completeness**: If the watermark has advanced past some timestamp T, we are guaranteed by its monotonic property that no more processing will occur for on-time (nonlate data) events at or before T. Therefore, we can correctly emit any aggregations at or before T. In other words, the watermark allows us to know when it is correct to materialize a window.
	* **Visibility**: If a message is stuck in our pipeline for any reason, the watermark cannot advance. Furthermore, we will be able to find the source of the problem by examining the message that is preventing the watermark from advancing.
* Notice that the distinguishing feature is that *perfect watermarks* ensure that the watermark accounts for all data, whereas *heuristic watermarks* admit some late-data elements.
### When to use heuristic watermarks

Consider an example where users play a mobile game, and their scores are sent to our pipeline for processing: you can generally assume that for any source utilizing mobile devices for input it will be generally impossible to provide a perfect watermark. Due to the problem of devices that go offline for extended periods of time, there’s just no way to provide any sort of reasonable estimate of absolute completeness for such a data source. You can, however, imagine building a watermark that accurately tracks input completeness for devices that are currently online, similar to the Google Pub/Sub watermark described a moment ago. Users who are actively online are likely the most relevant subset of users from the perspective of providing low-latency results anyway, so this often isn’t as much of a shortcoming as you might initially think.

### Pipeline stages
Different stages are typically necessary every time your pipeline groups data together by some new dimension. For example, if you had a pipeline that consumed raw data, computed some per-user aggregates, and then used those per-user aggregates to compute some per-team aggregates, you’d likely end up with a three-stage pipeline:
1. One consuming the raw, ungrouped data
2. One grouping the data by user and computing per-user aggregates
3. One grouping the data by team and computing per-team aggregates

### Understanding Watermark Propagation

An example: 
Compute user engagement level by calculating per-user session length. There are two datasets, one for mobile scores, and one for console scores. 

```java
PCollection<Double> mobileSessions = IO.read(new MobileInputSource())
  .apply(Window.into(Sessions.withGapDuration(Duration.standardMinutes(1)))
               .triggering(AtWatermark())
               .discardingFiredPanes())
  .apply(CalculateWindowLength());

PCollection<Double> consoleSessions = IO.read(new ConsoleInputSource())
  .apply(Window.into(Sessions.withGapDuration(Duration.standardMinutes(1)))
               .triggering(AtWatermark())
               .discardingFiredPanes())
  .apply(CalculateWindowLength());
```
1. Window by gapping 1 minutes: collection score every 1 minute
2. Then trigger the watermark (or collect the result) with the default `AtWaterMark()` trigger
3. We don't track all the previous pane's scores, so we use `discardingFiredPlanes()` every time we receive a result from the trigger. So for each window, we start from zero to accumulate the result/score
4. Finally, we transform with `CalculateWindowLength()` to transform the number of scores as the output (effectively, computing the per-user session length by treating the size of the current window as the value of that window)

**Then we combine the two results together**  
```java
PCollection<Float> averageSessionLengths = PCollectionList
  .of(mobileSessions).and(consoleSessions)
  .apply(Flatten.pCollections())
  .apply(Window.into(FixedWindows.of(Duration.standardMinutes(2)))
               .triggering(AtWatermark())
  .apply(Mean.globally());
```
1. We widen the gap to 2 minutes, so that we allow more results in a single window
2. We then apply the same default `AtWatermark()` trigger
3. We use `Mean.globally()` to get the mean values for the two scores, and use that values as the new result for each window

![[Watermarks-chained.png]]
Notice that: 
* The output watermark for each of the Mobile Sessions and Console Sessions stages is at least as old as the corresponding input watermark of each, and in reality a little bit older. This is because in a real system computing answers takes time, and we don’t allow the output watermark to advance until processing for a given input has completed.
* The input watermark for the Average Session Lengths stage is the minimum of the output watermarks for the two stages directly upstream.