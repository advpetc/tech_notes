# Book notes for `Design Data Intensive Apps` 

## Foundations of Data Systems

### Reliable, Scalable, and Maintainable Applications

* *Reliability*: The system should continue to work correctly even in the face of adversity.

* *Scalability*: As the system grows (data volume, traffic volume, or complexity), there should be reasonable ways of dealing with that growth.
* *Maintainability*: Over time, many different people will work on the system (engineering and operations, both maintain the current behavior and adapting the system to new use cases), and they should all be able to work on it *productively*.

### Reliability

In reality, it's not feasible to tolerate all the possible kind of faults. Therefore, it is usually best to design fault-tolerance mechanisms that prevent faults from causing failures.



* Hardware Fault: hard disks crash (prevent: setup RAID config), RAM becomes faulty, power grid has a blackout, etc. Hardware faults usually as being random and independent (one would not cause the other).
* Software Errors: usually correlate with each other (tend to cause many more system failures than uncorrelated hardware faults).
* Human Errors

### Scalability

Describe the system's ability to cope with increased load. Use *load parameters* to describe load.



Example: Twitter 

1. Post tweet: 4.6k requests/sec on average and 12k requests/sec at peak
2. Home timeline; 300k requests/sec

So Twitter needs to handle the "fan-out" rate (# of requests to other services that we need to make in order to serve one incoming request).

1. Approach 1: For `post`  request, it's simply "join" two tables:

```sql
select tweets.*, users.* from tweets
	join users on tweets.sender_id = users.id
	join follows on follows.followee_id = users.id
	where follows.follower_id = current_user
```

2. Approach 2: For checking `home timeline`, we can maintain a cache. When a user makes a new post, look up all the people who follow that user, and insert the new tweet into each of their home timeline caches. The request to read the home timeline is then cheap, because its result has been computed ahead of time.

Because the rate of `post` is much smaller than check `home timeline`, so it's more sensible to use approach 2. In reality, Twitter uses the combination of the above two methods: for celebrity they use approach 1, since each celebrity has a lot of followers and the cost for writing all the pieces to caches is numerous.

#### Describe Performace

Averge response time is not a good metric if you want to know your "typical" response time, because it doesn't tell you how many users actually experienced that delay. Usually it's better to use *percentiles*: sort the response by time in ascending time, and the median is the halfway point or called *50th percentile*. High percentiles of response time directly affect users' experience of the service. Amazon describes response time requirements for internal services in terms of the 99.9th percentile, even though it only affects 1 in 1,000 requests.