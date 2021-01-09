# K sum problem

## Find X-elements from an array such that their sum is equal to a target value

**things to clarify**:
1. return value or return true/false or return index
2. data size
3. duplication (assume no duplication)
4. sorted vs unsorted
5. data type: int
6. optimize for time or optimize for space

## P1: 2Sum

> https://leetcode.com/problems/two-sum/

### Solution 1 -- use hashmap

```c
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> checker; // val => index
        for (int i = 0; i < nums.size(); ++i) {
            int com = target - nums[i]; // find comlement
            if (checker.find(com) != checker.end())
                return {i, checker[com]};
            checker[nums[i]] = i;
        }
        return {};
    }
};
```

* Time: $O(n)$
* Space: $O(n)$

### Solution 2 (input array is sorted) -- two pointers

```c
class Solution {
public:
    bool twoSum(vector<int>& nums, int target) { // return true if exit, else false;
        for (int i = 0, j = nums.size() - 1; i < j;) {
            int curr = nums[i] + nums[j];
            if (curr == target) return true;
            else if (curr > target) j--;
            else i++;
        }
        return false;
    }
};
```

* Time: $O(n)$
* Space: $O(n)$ for sorting (aux array for merge sort, if using quick sort it will be $O(1)$)

### Solution 4 (unsorted, but goal is optimize for space, and the input array is **mutable**)

```c
class Solution {
public:
    bool twoSum(vector<int>& nums, int target) { // return true if exit, else false;
        for (int i = 0; i < nums.size(); ++i)
            for (int j = 0; j < nums.size(); ++j)
                if (nums[i] + nums[j] == target) return true;
        return false;
    }
};
```

* Time: $O(n^2)$
* Space: $O(1)$

### Variant 1: with duplicate and return all the index pairs

```c
class Solution {
 public:
  vector<vector<int>> allPairs(vector<int> array, int target) {
    unordered_map<int, vector<int>> idx;
    vector<vector<int>> res;
    for (int i = 0; i < array.size(); ++i) { // O(n)
      if (idx.count(target - array[i]))
        for (int j : idx[target - array[i]]) // O(n)
          res.push_back({j, i});
      idx[array[i]].push_back(i);
    }
    return res;
  }
};

```

* Time: $O(n^2)$
* Space: $O(n)$

### Variant 2: with duplicate and only return the unique pairs (not index)

```c
class Solution {
 public:
  vector<vector<int>> allPairs(vector<int> array, int target) {
    // write your solution here
    unordered_set<int> st;
    vector<vector<int>> res;
    bool counted = true;
    for (int a : array) {
      // 2 * a = target
      if (a + a == target && st.count(a)) {
        if (counted) {
          res.push_back({a, a});
          counted = false;
        }
      }
      // a + b = target
      else if (!st.count(a) && st.count(target - a)) 
        res.push_back({a, target - a});
      st.insert(a);
    }
    return res;
  }
};

```

e.g. if array = [2,2,2,3], target = 4, we just return [2,2]

* Time: $O(n)$
* Space: $O(n)$

## P2: 3Sum

Assume:
1. no duplicate
2. optimize for time
3. data size is small enough to fit into memory
4. unsorted

### Solution 1: reuse 2Sum

assume there the triplet is x + y + z = target, and x < y < z (since they are no duplicate).

1. start with x (try all element from a[0] - a[n]), try find y + z such that y + z = target - x
2. Use 2Sum to find the y + z


* Time: $O(n^2)$ -> outter loop + inner $O(n)$ 2Sum
* Space: $O(n)$

### Solution 2: sort then two pointers

```c
class Solution {
 public:
  vector<vector<int>> allTriples(vector<int> array, int target) {
    // write your solution here
    vector<vector<int>> res;
    int n = array.size();
    sort(array.begin(), array.end());
    for (int i = 0; i < n - 2; ++i) {
      if (i > 0 && array[i] == array[i - 1]) continue; // skip duplicate
      int curr = array[i], l = i + 1, r = n - 1;
      while (l < r) {
        if (curr + array[l] + array[r] == target) {
          res.push_back({curr, array[l], array[r]});
          l++, r--;
          while (l < r && array[l] == array[l - 1]) l++;
          while (l < r && array[r] == array[r + 1]) r--;
        } else if (curr + array[l] + array[r] < target) l++;
        else r--;
      }
    }
    return res;
  }
};

```

* Time: $O(n^2)$
* Space: $O(1)$ -- optimized space thus preferred

## 4Sum

Assume:
1. input is immutable
2. optimize for time
3. unsorted
4. fit into memory
5. no duplicate
6. return true/false

### Solution 1: two outter forloop then include a 2Sum

assume $a_1 + a_2 + a_3 + a_4 == target$, then fix $a_1$ and $a_2$ from two outter loops. Use 2Sum to find the pair such that the $sum == target - a_1 - a_2$

pseudocode:

```
define map<key = sum, value = <<two index>,<two index>, ... >>
for(i)
  for(j)
    curr pair<i, j>, pair_sum = a[i] + a[j]
    if target - pair_sum is in the map AND <i, j> is different from all the values pairs:
      return true
```

* Time: $O(n^3)$ -- the inner check could take $O(n)$ times
* Space: $O(n)$ -- each distinct i, j can have its own target value

### Solution 2: 4Sum = 2Sum + 2Sum

$a_1 + a_2 + a_3 + a_4 = target$, since there is no duplicate, we can assume $a_1 < a_2 < a_3 < a_4$. By using this property, we can just ignore the case when idx for latter element is smaller than prevous element's idx.

```c
class Solution {
 public:
  bool exist(vector<int> array, int target) {
    // write your solution here
    unordered_map<int, vector<int>> idx;
    int n = array.size();
    for (int i = 1; i < n; ++i) // right
      for (int j = 0; j < i; ++j) // left
        if (!idx.count(array[i] + array[j])) 
          idx[array[i] + array[j]] = {j, i}; // save <j, i> as j is always less than i
    for (int i = 0; i < n; ++i) // left
      for (int j = i + 1; j < n; ++j) { // right
        int curr = target - (array[i] + array[j]);
        if (idx.count(curr) && idx[curr][1] < i)
          return true;
      }
    return false;
  }
  
};

```