# Majority Element with k times

Given an integer array of length L, find all numbers that occur more than 1/K * L times if any exist.

Assumptions

The given array is not null or empty
K >= 2
Examples

A = {1, 2, 1, 2, 1}, K = 3, return [1, 2]
A = {1, 2, 1, 2, 3, 3, 1}, K = 4, return [1, 2, 3]
A = {2, 1}, K = 2, return []

## Analysis

We can apply the same method usng in 2 and 3 times. General steps:
1. To have occurred more than 1/k * n times, we can only have k - 1 elements (so that k * (1/k * n) <= n).
2. Then we can limit the mapping has a size of at most k - 1
3. Do the checking for each element in the array: 
  1. if exist in the map, just incremenet the counter by 1
  2. else
        1. if the map is full, we decreament all the other couting, and if any of the counter reaches zero, we erase that mapping
            2. if map isn't full, we just add one mapping of the new element to the map.
4. Do the final check to see if all the keys in the map has the appeared more than 1/k * n times.

## Code

```c
class Solution {
 public:
  vector<int> majority(vector<int> array, int k) {
    // write your solution here
    unordered_map<int, int> cnt;
    for (int a : array) {
      if (cnt.count(a)) cnt[a]++;
      else {
        if (cnt.size() == k - 1) {
          for (auto& p : cnt) {
            if (--p.second == 0)
              cnt.erase(p.first);
          }
        } else if (cnt.size() < k - 1) {
          cnt[a] = 1;
        }
      }
    }
    unordered_map<int, int> check;
    vector<int> res;
    int target = array.size() / k;
    for (int a : array) {
      if (cnt.count(a))
        ++check[a];
    }
    for (auto p : check)
      if (p.second > target) res.push_back(p.first);
    return res;
  }
};
 
```