# Maximum Product Subarray

https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# How many subarrays in total?

There are $N^2$ subarrays. You can choose 1 out of N for the start of the subarray, and also 1 out of N for the end of the subarray, so in total it will be $N^2 / 2$ (divide by two because of duplicates).

# DFS with memo $O(n^2)$

`map<int,int>` where key is the end and value is the product, create the map every time when start changes.

# DP $O(n)$ with space $O(n)$

max_dp[i]: from 0-i, the maximum product
min_dp[i]: from 0-i, the minimum product

**base case:**
1. max_dp[0] = max(0, array[0]) // you can choose itself or nothing
2. min_dp[0] = min(0, array[0])

**induction:**
max_dp[i] = max(min_dp[i] * array[i], max_dp[i-1] * array[i], array[i])
where min_dp[i] * array[i] is for calculating the case when both min_dp and array[i] are neg
where max_dp[i] * array[i] is for calculating the case when both max_dp and array[i] are pos

```c
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int max_dp[n], min_dp[n];
        memset(max_dp, 0, sizeof max_dp);
        memset(min_dp, 0, sizeof min_dp);
        int res = INT_MIN;
        for (int i = 0; i < n; ++i) {
            if (i == 0) {
                min_dp[i] = nums[i];
                max_dp[i] = nums[i];
            }
            else {
                max_dp[i] = max(max(min_dp[i-1] * nums[i], max_dp[i-1] * nums[i]), nums[i]);
                min_dp[i] = min(min(min_dp[i-1] * nums[i], max_dp[i-1] * nums[i]), nums[i]);
            }
            res = max(res, max_dp[i]);
        }
        return res;
    }
};
```

# Optimize DP with $O(1)$ space

max_dp: from 0-i, the maximum product
min_dp: from 0-i, the minimum product

**base case:**
1. pre_max_dp = array[0] // you can choose itself or nothing
2. pre_min_dp = array[0]

**induction:**
max_dp = max(min_dp * array[i], pre_max_dp * array[i], array[i])
where min_dp * array[i] is for calculating the case when both min_dp and array[i] are neg
where max_dp * array[i] is for calculating the case when both max_dp and array[i] are pos

```c
class Solution {
    public:
        int maxProduct(vector<int>& nums) {
            int size = nums.size();
            if (size == 0) { return 0; }
            int oldMin = nums[0];
            int oldMax = nums[0];
            int ret = nums[0];
            for (int i = 1; i < size; ++i) {
                int newMax = max(nums[i], nums[i] > 0 ? oldMax * nums[i] : oldMin * nums[i]);
                int newMin = min(nums[i], nums[i] > 0 ? oldMin * nums[i] : oldMax * nums[i]);
                ret = max(ret, newMax);
                oldMin = newMin;
                oldMax = newMax;
            }
            return ret;
        }
};

```

