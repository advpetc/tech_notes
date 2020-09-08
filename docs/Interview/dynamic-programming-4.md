## Q1 Longest increasing subarray and subsequence

### Subarray

Given an unsorted array, find the length of the longest subarray in which the numbers are in ascending order. For example: if the input array is {7, 2, 3, 1, 5, 8, 9, 6}, the subarray with the most numbers in ascending order is {1, 5, 8, 9}  and the expected output is 4.

#### Using DP

- M[i]: length of the longest increasing subarray where the last element in the subarray is num[i].
- induction rule: 
  - M[i] = M[i-1] if num[i] <= num[i-1]
  - M[i] = M[i-1] + 1 else

##### Code

```c
#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

int num[N], n;

int main() {
	cin >> n;
	for (int i = 0; i < n; ++i) cin >> num[i];
	int gMax = 0;
	int dp[n];
	memset(dp, 0, sizeof dp);
	dp[0] = 1;
	for (int i = 1; i < n; ++i) {
		if (num[i - 1] < num[i]) dp[i] = dp[i - 1] + 1;
		else dp[i] = 1;
		gMax = max(gMax, dp[i]);
	}
	cout << gMax;
	return 0;
}
```

#### Using greedy search

Keep a global max to store the answer, and a local max to store the current max.
- if num[i] > num[i-1]: local max ++, global max = max(global max, local max)
- else: local max = 0
- return global max

##### Code

```c
#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

int num[N], n;

int main() {
	cin >> n;
	for (int i = 0; i < n; ++i) cin >> num[i];
	int lMax = 1, gMax = 0;
	for (int i = 0; i < n - 1; ++i) {
		if (num[i] < num[i + 1]) gMax = max(++lMax, gMax);
		else lMax = 1;
	}
	cout << gMax;
	return 0;
}
```

### Subsequence

Given an unsorted array, find the length of the longest subsequence in which the numbers are in ascending order. For example: if the input array is {7, 2, 3, 1, 5, 8, 9, 6}, the subarray with the most numbers in ascending order is {2, 3, 5, 8, 9}  and the expected output is 5.

#### Using DP

- M[i]: longest length of the subsequence ending with num[i]
- induction rule:
  - keep i-- to find the first element j from 0 to i - 1 that is less than num[i], and update M[i] = M[j] + 1

##### Code

```c
class Solution {
 public:
  int longest(vector<int> arr) {
    // write your solution here
    int n = arr.size(), res = 0;
    vector<int> m(n, 0);
    for (int i = 0; i < arr.size(); ++i) {
      int lMax = 0;
      for (int j = 0; j < i; ++j) {
        if (arr[j] < arr[i]) lMax = max(lMax, m[j]);
      }
      m[i] = lMax + 1;
      res = max(res, m[i]);
    }
    return res;
  }
};

```

#### Using DP + Bsearch

Keep an array called `lowest_ending`, `lowest_ending[i]` represents the LIS with length of i and the last element in the LIS is num[i]. So we can just return the size of the `lowest_ending` as the answer.
- Induction rule for updating `lowest_ending` array:
  - if `lowest_ending[i - 1] < num[i]` -- meaning `lowest_ending[i] = num[i]` because all the element in the front are less than num[i]
  - else: find the first `lowest_ending[j] >= num[i]`, so that we can update the `lowest_ending[j] = num[i]`

##### Code

```c
#include <iostream>

using namespace std;

const int N = 1010;
int n, cnt;
int w[N], f[N]; // w stores the input, f stores the lowest ending

int main() {
    cin >> n;
    for (int i = 0 ; i < n; i++) cin >> w[i];

    f[cnt++] = w[0];
    for (int i = 1; i < n; i++) {
        if (w[i] > f[cnt-1]) f[cnt++] = w[i];
        else {
            int l = 0, r = cnt - 1;
            while (l < r) {
                int mid = (l + r) >> 1;
                if (f[mid] >= w[i]) r = mid;
                else l = mid + 1;
            }
            f[r] = w[i];
        }
    }
    cout << cnt << endl;
    return 0;
}

作者：VictorWu
链接：https://www.acwing.com/solution/content/4807/
来源：AcWing
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

### Subsequence return the path

In addition to return the max lenght, return one of the path.

#### Using a index array to represent the previous element's index

- pre[i]: last element's index in subsequence where the last element of the subsequence is num[i].
- use the same method to get the length, but when updating the length also update the lastIdx that should point to the last element of the LIS.
- when recovering the path, use:

  ```cpp
  res[i] = arr[lastIdx];
  lastIdx = pre[lastIdx];
  ```
  
  to update.

##### Code

```c
class Solution {
 public:
  vector<int> longest(vector<int> arr) {
    // write your solution here
    int n = arr.size(), gMax = 0, lastIdx = -1;
    vector<int> pre(n, -1);
    vector<int> m(n, 0);
    for (int i = 0; i < n; ++i) {
      int lMax = 0, preIdx = i;
      for (int j = 0; j < i; ++j) {
        if (arr[j] < arr[i]) {
          if (lMax < m[j]) {
            preIdx = j;
            lMax = m[j];
          }
        }
      }
      m[i] = lMax + 1;
      pre[i] = preIdx;
      if (gMax < m[i]) {
        gMax = m[i];
        lastIdx = i;
      }
    }
    vector<int> res(gMax);
    for (int i = gMax - 1; i >= 0; --i) {
      res[i] = arr[lastIdx];
      lastIdx = pre[lastIdx];
    }
    return res;
  }
};
```

## Q2 Find subset of points to form positive slope

Given an array of coordinates of 2D points, how to find the **largest subset of points** in which any pair of points can form a line with positive slope.

### Conversion to LIS problem

In order to form a positive slope line: y = kx + b, where k has to be greater than 0. Using math, $k = \frac{\delta x}{\delta y}$.

- $\frac{x_1 - x_2}{y_1 - y_2} > 0$: meaning if $x_1 < x_2$ then $y_1 < y_2$.

Base on the above oberservation, we can first sort (ascending order) the points based on x value, so that we can choose any element points[i].x - points[j].x > 0 if i > j. Now the problem is reduced into how to choose j such that points[i].y - points[j].y > 0, which is equal to find the LIS of points.y in the sorted array.

#### Code

```c
class Solution {
 public:
  int largest(vector<pair<int, int> > points) {
    sort(points.begin(), points.end(), [](pair<int, int>& l, pair<int, int>& r){
      return l.first < r.first || (l.first == r.first && l.second > r.second);
    });
    vector<int> lowest_end; // record the lowest possible ending lis where the length is idx
    for (int i = 0; i < points.size(); ++i) {
      int sz = lower_bound(lowest_end.begin(), lowest_end.end(), points[i].second) - lowest_end.begin();
      if (sz >= lowest_end.size()) lowest_end.push_back(points[i].second);
      else lowest_end[sz] = points[i].second;
    }
    return lowest_end.size() == 1 ? 0 : lowest_end.size();
  }
};
```