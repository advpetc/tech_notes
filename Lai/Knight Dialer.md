![Screen Shot 2020-05-23 at 4.06.25 PM.png](resources/74AB6AC5D113612CC9187F044CF0C55A.png =579x378)

e.g.
input: 1 output: 10

e.g.
input: 2 output: 20
1: 6, 8
2: 7, 9
3: 4, 8
4: 3, 9, 0
5: -
6: 1, 7, 0
7: 2, 6
8: 1, 3
9: 4, 2
0: 4, 6

e.g.
input: 3 output: 48

# DFS with memo

Time Complexity: O(n) -> size of memo, Space Complexity: O(n), But call stack is very large.

```c
#include <bits/stdc++.h>

using namespace std;
const int mod = 1e9 + 7, MAX = 10010;

string nxt[10] = {"46", "68", "79", "48", "390", "", "170", "26", "13", "42"};
int res = 0, n;
int memo[10][MAX];

int dfs(int pos, int hops) {
	if (memo[pos][hops] != 0)
		return memo[pos][hops];
	int cnt = 0;
	for (char i : nxt[pos]) {
		cnt += dfs(i - '0', hops - 1);
	}
	return memo[pos][hops] = cnt;
}

void solve() {
	for (int i = 0; i < 10; ++i)
		memo[i][0] = 1;
	
	for (int pos = 0; pos < 10; ++pos)
		res += dfs(pos, n - 1);
}

int main() {
	cin >> n;
	solve();
	cout << res % mod;
	return 0;
}
```

# DP with 2D matrix

memo[pos][hops]: # of solution when ends in "pos" in "hops" hops.
base case: memo[x][0] = 1

```c
#include <bits/stdc++.h>

using namespace std;
const int mod = 1e9 + 7;

string nxt[10] = {"46", "68", "79", "48", "390", "", "170", "26", "13", "42"};
#define ll long long
int main() {
  ll res = 0;
  int n;
  cin >> n;
  ll memo[10][n];
  for (int i = 0; i < 10; ++i) memo[i][0] = 1;
  for (int hops = 1; hops < n; ++hops) {
    for (int pos = 0; pos < 10; ++pos) {
      ll cnt = 0;
      for (char nei : nxt[pos]) {
        cnt %= mod;
        cnt += memo[nei - '0'][hops - 1];
      }
      memo[pos][hops] = cnt;
    }
  }
  for (int i = 0; i < 10; ++i) {
    res += memo[i][n - 1];
  }
  cout << res % mod;
  return 0;
}
```

# DP with constant space

only need to record last state, so just two array is fine.

```c
#include <bits/stdc++.h>

using namespace std;
const int mod = 1e9 + 7;

string nxt[10] = {"46", "68", "79", "48", "390", "", "170", "26", "13", "42"};

#define ll long long
int main() {
  ll res = 0;
  int n;
  cin >> n;
  ll prev[10], curr[10];
  for (int i = 0; i < 10; ++i) prev[i] = 1;
  for (int hops = 1; hops < n; ++hops) {
    for (int pos = 0; pos < 10; ++pos) {
      ll cnt = 0;
      for (char nei : nxt[pos]) {
        cnt %= mod;
        cnt += prev[nei - '0'];
      }
      curr[pos] = cnt;
    } 
    for (int pos = 0; pos < 10; ++pos) {
    	prev[pos] = curr[pos];
    	curr[pos] = 0;
    }
  }
  for (int i = 0; i < 10; ++i) {
    res += prev[i];
  }
  cout << res % mod;
  return 0;
}
```