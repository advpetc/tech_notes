Search for a target number in a bitonic array, return the index of the target number if found in the array, or return -1.

A bitonic array is a combination of two sequence: the first sequence is a monotonically increasing one and the second sequence is a monotonically decreasing one.

Assumptions:

The array is not null.
Examples:

array = {1, 4, 7, 11, 6, 2, -3, -8}, target = 2, return 5.

## Analysis

Use arr[m] and arr[m - 1] to find the order of the array for l ~ m or m ~ r

+ if m > m - 1: l ~ m is in increasing order
  1. if target is greater than m, then search the (m, r]
  2. else: search in l ~ m in **increasing order**
+ if m <= m - 1: m ~ r is in decreasing order
  1. if target is greater than m, then search the [l, m)
  2. else: search in m ~ r in **decreasing order**

Depending on the order, change according for the binary search function

# Code

```c
class Solution {
 public:
    int bsearch(vector<int> a, int target, int l, int r)
    {
        bool dir = a[l] <= a[r];
        while (l < r) {
            int m = (l + 0ll + r) >> 1;
            if (target == a[m])
                return m;
            else if (target < a[m])
                dir ? r = m : l = m + 1;
            else
                dir ? l = m + 1 : r = m;
        }
        return -1;
    }

    int search(vector<int> a, int target)
    {
        // write your solution here
        int n = a.size();
        int l = 0, r = n - 1;
        while (l < r) {
            int m = (l + 0ll + r) >> 1;
            if (target == a[m])
                return m;
            if (a[m] > a[m - 1]) { // increasing from l to m
                if (target > a[m]) // m-1 < m < target
                    l = m + 1;
                else { 
                    int res;
                    if ((res = bsearch(a, target, l, m)) != -1) // l <= target <= m
                        return res;
                    else if ((res = bsearch(a, target, m + 1, r)) != -1) // m + 1 <= target <= r
                        return res;
                    else
                        return -1;
                }
            } else { // decreasing from m - 1 to r
                if (target > a[m]) // target > m > m - 1
                    r = m;
                else {
                    int res;
                    if ((res = bsearch(a, target, l, m)) != -1) // l <= target <= m
                        return res;
                    else if ((res = bsearch(a, target, m + 1, r)) != -1) // m + 1 >= target >= r
                        return res;
                    else
                        return -1;
                }
            }
        }
        return -1;
    }

};

```