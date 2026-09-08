# 0167. Two Sum II - Input Array Is Sorted

Given a **1-indexed** array of integers `numbers` that is already ***sorted in non-decreasing order\***, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return *the indices of the two numbers,* `index1` *and* `index2`*, **added by one** as an integer array* `[index1, index2]` *of length 2.*

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

 

**Example 1:**

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Example 2:**

```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

**Example 3:**

```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

 

**Constraints:**

- `2 <= numbers.length <= 3 * 104`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- The tests are generated such that there is **exactly one solution**.

## Analysis

Since the input array is sorted, to find the target sum we can use two pointers to reach the optimal complexity. The comparison condition works by comparing the current sum and the target: if the current sum is greater than the target, then we should minimize the sum, and the only way of doing so is by moving the bigger value (right pointer) to a smaller value (moving it to the left). Note that the left pointer can only move to the right and the right pointer can only move to the left, or the algorithm will fail (infinite loop due to a duplicate check).

* Time: $O(n)$
* Space: $O(1)$

## Code

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for (int l = 0, r = numbers.size() - 1; l < r;) {
            int curr = numbers[l] + numbers[r];
            if (target == curr) return {l + 1, r + 1};
            else if (target < curr) r --;
            else l ++;
        }
        return {};
    }
};
```

