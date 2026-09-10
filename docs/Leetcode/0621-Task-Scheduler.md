# 0621. Task Scheduler

You are given an array of CPU `tasks`, each represented by letters `A` to `Z`, and a cooling time, `n`. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: **identical** tasks must be separated by at least `n` intervals due to cooling time.

​Return the **minimum number of intervals** required to complete all tasks.

 

**Example 1:**

```
Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.
```

**Example 2:**

```
Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.
```

**Example 3:**

```
Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
```

 

**Constraints:**

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter.
- `0 <= n <= 100`

## Analysis

The key insight is that the schedule's length is dictated entirely by the **most frequent** task(s). Suppose the highest frequency among all tasks is `maxFreq`. We can lay out `maxFreq - 1` "blocks" of the most frequent task, each block followed by a cooldown window of `n` slots, and then place the final occurrence at the end — that skeleton alone takes `(maxFreq - 1) * (n + 1) + 1` slots.

If there's more than one task tied for `maxFreq` (say `numMax` of them), each of those extra ties needs one more slot appended at the very end, giving `(maxFreq - 1) * (n + 1) + numMax`.

Every other, less-frequent task can always be slotted into the idle gaps of this skeleton without ever violating the cooldown constraint (a short proof by contradiction: if a lower-frequency task couldn't fit anywhere, it would have to appear more often than `maxFreq`, which contradicts our choice of `maxFreq`). So this frame length is a hard lower bound on the schedule.

The only other lower bound is simply `tasks.size()`, since we can never finish faster than one interval per task even with zero idling — this bound "wins" once there are enough distinct tasks to fill every cooldown gap with no idle time at all. The answer is therefore the larger of the two.

* Time: $O(n)$ to count task frequencies, where $n$ is the length of `tasks`.
* Space: $O(1)$, since the frequency table is bounded by the 26 uppercase letters.

## Code

```c++
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> cnt(26, 0);
        for (char t : tasks) cnt[t - 'A']++;
        int maxFreq = *max_element(cnt.begin(), cnt.end());
        int numMax = count(cnt.begin(), cnt.end(), maxFreq);
        int frameLength = (maxFreq - 1) * (n + 1) + numMax;
        return max((int)tasks.size(), frameLength);
    }
};
```
