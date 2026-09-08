# 1345. Jump Game IV

Given an array of integers `arr`, you are initially positioned at the first index of the array.

In one step you can jump from index `i` to index:

- `i + 1` where `i + 1 < arr.length`.
- `i - 1` where `i - 1 >= 0`.
- `j` where `arr[i] == arr[j]` and `i != j`.

Return *the minimum number of steps* to reach the **last index** of the array.

Notice that you can not jump outside of the array at any time.

 

**Example 1:**

```
Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
```

**Example 2:**

```
Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
```

**Example 3:**

```
Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
```

 

**Constraints:**

- `1 <= arr.length <= 5 * 10^4`
- `-10^8 <= arr[i] <= 10^8`

## Analysis

This is a shortest-path problem in an unweighted graph, so BFS is the natural fit. Besides the `i - 1` and `i + 1` edges, every index shares an edge with every other index that holds the same value, which is where the difficulty lies: naively re-exploring the same-value group every time we visit one of its members can blow up to $O(n^2)$.

The fix is to pre-group indices by value with a hash map, and once we've expanded a value's entire group into the BFS queue, delete that entry from the map. This guarantees each same-value group is expanded exactly once across the whole search, no matter how many of its members we later visit.

* Time: $O(n)$, since each index and each value group is processed once.
* Space: $O(n)$ for the value-to-indices map, the visited array, and the queue.

## Code

```c++
class Solution {
public:
    int minJumps(vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) return 0;
        unordered_map<int, vector<int>> idx;
        for (int i = 0; i < n; ++i) idx[arr[i]].push_back(i);
        vector<bool> visited(n, false);
        queue<int> q;
        q.push(0);
        visited[0] = true;
        int steps = 0;
        while (!q.empty()) {
            int sz = q.size();
            for (int k = 0; k < sz; ++k) {
                int i = q.front();
                q.pop();
                if (i == n - 1) return steps;
                if (idx.count(arr[i])) {
                    for (int j : idx[arr[i]]) {
                        if (!visited[j]) {
                            visited[j] = true;
                            q.push(j);
                        }
                    }
                    idx.erase(arr[i]); // this value's group is fully expanded, never revisit it
                }
                if (i + 1 < n && !visited[i + 1]) {
                    visited[i + 1] = true;
                    q.push(i + 1);
                }
                if (i - 1 >= 0 && !visited[i - 1]) {
                    visited[i - 1] = true;
                    q.push(i - 1);
                }
            }
            steps++;
        }
        return -1; // unreachable; not expected given the problem's guarantees
    }
};
```
