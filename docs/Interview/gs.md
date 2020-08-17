## Balanced Array

```c
#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

int num[N];
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> num[i];
  }
  int presum[n];
  memset(presum, 0, sizeof presum);
  for (int i = 0; i < n; ++i) {
    if (i == 0) presum[i] = num[i];
    else presum[i] += num[i] + presum[i - 1];
  }
  for (int i = 0; i < n; ++i ) {
    if (presum[i] - num[i] == presum[n - 1] - presum[i]) {
      cout << i << endl;
      return 0;
    }
  }
  cout << -1;
}

```