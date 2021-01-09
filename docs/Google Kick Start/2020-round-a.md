# 2020 Round A

## Allocation

There are N houses for sale. The i-th house costs Ai dollars to buy. You have a budget of B dollars to spend.

What is the maximum number of houses you can buy?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a single line containing the two integers N and B. The second line contains N integers. The i-th integer is Ai, the cost of the i-th house.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum number of houses you can buy.

Limits
Time limit: 15 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ B ≤ 105.
1 ≤ Ai ≤ 1000, for all i.

Test set 1
1 ≤ N ≤ 100.

Test set 2
1 ≤ N ≤ 105.

Sample

Input
 	
Output

3
4 100
20 90 40 90
4 50
30 30 10 10
3 300
999 999 999


Case #1: 2
Case #2: 3
Case #3: 0


In Sample Case #1, you have a budget of 100 dollars. You can buy the 1st and 3rd houses for 20 + 40 = 60 dollars.
In Sample Case #2, you have a budget of 50 dollars. You can buy the 1st, 3rd and 4th houses for 30 + 10 + 10 = 50 dollars.
In Sample Case #3, you have a budget of 300 dollars. You cannot buy any houses (so the answer is 0).

### Analysis

To buy the maxmimum amount of houses, we can greedy buy the ones with the smallest cost first, and until we reach to the point when there is no money left to buy the next higher cost house, we can stop.

Prove by replacement:
assume the solution is A = {a1, ..., ak} where ai represents the house cost you choose for the max amount.
assume the optimal solution is O = {oi, ..., om} where oi represents the true solution.
assume oj is not presented in A
we want to prove that A == O

pick an ai that is in A, and replace it with oj. oj is not in A, so oj is less than ai. since size of B is the same, the solution is still the most optimal one. keep doing this until there is A == O.

### Code

#### sort with nlog n

```c
/*
 * allocation.cpp
 * Copyright (C) 2020 Haoyang <peter@peterchen.xyz>
 *
 * Distributed under terms of the MIT license.
 */
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[])
{
    int T, N, B;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N >> B;
        vector<int> costs(N, 0);
        for (int j = 0; j < N; ++j) {
            cin >> costs[j];
        }
        sort(costs.begin(), costs.end()); // nlog n
        int cnt = 0;
        for (int k = 0; k < N; ++k)
            if (B >= costs[k]) {
                B -= costs[k];
                cnt++;
            } else break;
        cout << "Case #" << i << ": " << cnt << endl;
    }
    return 0;
}

```

#### count sort with n

because 1 ≤ Ai ≤ 1000, we can use count sort

```c
/*
 * allocation.cpp
 * Copyright (C) 2020 Haoyang <peter@peterchen.xyz>
 *
 * Distributed under terms of the MIT license.
 */
#include <bits/stdc++.h>

using namespace std;

const int n = 1010;
int A[n];

int main(int argc, char* argv[])
{
    int T, N, B;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N >> B;
        memset(A, 0, sizeof A);
        int v;
        for (int i = 0; i < N; ++i) {
            cin >> v;
            A[v]++;
        }
        int cnt = 0;
        for (int i = 1; B > 0 && i <= 1000; ++i) { // i is house price
            int curr = min(B / i, A[i]); // case when there are less than you can buy
            cnt += curr;
            B -= curr * i;
        }
        cout << "Case #" << i << ": " << cnt << endl;
    }
    return 0;
}

```

## Plates

Dr. Patel has N stacks of plates. Each stack contains K plates. Each plate has a positive beauty value, describing how beautiful it looks.

Dr. Patel would like to take exactly P plates to use for dinner tonight. If he would like to take a plate in a stack, he must also take all of the plates above it in that stack as well.

Help Dr. Patel pick the P plates that would maximize the total sum of beauty values.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the three integers N, K and P. Then, N lines follow. The i-th line contains K integers, describing the beauty values of each stack of plates from top to bottom.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum total sum of beauty values that Dr. Patel could pick.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ K ≤ 30.
1 ≤ P ≤ N * K.
The beauty values are between 1 and 100, inclusive.

Test set 1
1 ≤ N ≤ 3.

Test set 2
1 ≤ N ≤ 50.

Sample

Input
 	
Output

2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10


Case #1: 250
Case #2: 180


In Sample Case #1, Dr. Patel needs to pick P = 5 plates:
He can pick the top 3 plates from the first stack (10 + 10 + 100 = 120).
He can pick the top 2 plates from the second stack (80 + 50 = 130) .
In total, the sum of beauty values is 250.

In Sample Case #2, Dr. Patel needs to pick P = 3 plates:
He can pick the top 2 plates from the first stack (80 + 80 = 160).
He can pick no plates from the second stack.
He can pick the top plate from the third stack (20).
In total, the sum of beauty values is 180.

### Analysis

dp[N][P]: from first n stacks, with p plates, the maximum beauty values
dp[i][j] = max(dp[i][j], val[k] + dp[i - 1][p - k])

for choosing current stack's top k plates, you need to give up the previous stacks k plates, so the previous state is dp[i - 1][p - k]
the answer is dp[N][P]

### Code

```c
/*
 * plates.cpp
 * Copyright (C) 2020 Haoyang <peter@peterchen.xyz>
 *
 * Distributed under terms of the MIT license.
 */
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[])
{
    int T;
    int N, K, P; // n: # of stacks, k: # of items for each stack, # total to be
                 // borrowed
    cin >> T;
    for (int t = 0; t < T; ++t) {
        cin >> N >> K >> P;
        int dp[N + 1][P + 1]; // from 0-N, the max value for P plates
        memset(dp, 0, sizeof dp);
        for (int i = 1; i <= N; ++i) {
            int val[K + 1];
            memset(val, 0, sizeof val);
            for (int j = 1; j <= K; ++j) {
                cin >> val[j];
            }
            // calculate preSum
            for (int k = 1; k <= K; ++k) {
                val[k] = val[k - 1] + val[k];
            }
            for (int p = 1; p <= P; ++p) {
                for (int k = 0; k <= min(p, K); ++k) {
                    dp[i][p]  = max(dp[i][p], val[k] + dp[i - 1][p - k]);
                }
            }
        }
        cout << "Case #" << t << ": " << dp[N][P] << endl;
    }
    return 0;
}

```

## Workout

Tambourine has prepared a fitness program so that she can become more fit! The program is made of N sessions. During the i-th session, Tambourine will exercise for Mi minutes. The number of minutes she exercises in each session are strictly increasing.

The difficulty of her fitness program is equal to the **maximum difference** in the number of minutes between any two consecutive training sessions.

To make her program less difficult, Tambourine has decided to add up to K additional training sessions to her fitness program. She can add these sessions anywhere in her fitness program, and exercise any positive integer number of minutes in each of them. After the additional training session are added, the number of minutes she exercises in each session must still be strictly increasing. What is the minimum difficulty possible?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the two integers N and K. The second line contains N integers, the i-th of these is Mi, the number of minutes she will exercise in the i-th session.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum difficulty possible after up to K additional training sessions are added.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
For at most 10 test cases, 2 ≤ N ≤ 105.
For all other test cases, 2 ≤ N ≤ 300.
1 ≤ Mi ≤ 109.
Mi < Mi+1 for all i.

Test set 1
K = 1.

Test set 2
1 ≤ K ≤ 105.

Samples

Input 1
 	
Output 1

1
3 1
100 200 230

Case #1: 50


Input 2
 	
Output 2

3
5 2
10 13 15 16 17
5 6
9 10 20 26 30
8 3
1 2 3 4 5 6 7 10

Case #1: 2
Case #2: 3
Case #3: 1

Sample #1
In Case #1: Tambourine can add up to one session. The added sessions are marked in bold: 100 150 200 230. The difficulty is now 50.

Sample #2
In Case #1: Tambourine can add up to two sessions. The added sessions are marked in bold: 10 11 13 15 16 17 18. The difficulty is now 2.

In Case #2: Tambourine can add up to six sessions. The added sessions are marked in bold: 9 10 12 14 16 18 20 23 26 29 30. The difficulty is now 3.

In Case #3: Tambourine can add up to three sessions. The added sessions are marked in bold: 1 2 3 4 5 6 7 8 9 10. The difficulty is now 1. Note that Tambourine only added two sessions.

### Analysis

1. **Priority Queue**: Find an array that record the gaps every two sessions. Call it gaps[N-1]. To add one session, the new one should be between the one that has the greatest gap. However, we cannot do that all at once for the first greatest gap. Instead, we should do it "greedily". When adding the one, we need to find a way to get the **updated** max gap from the total gaps. In order to do so, we need to use priority queue. The top of the queue will store the maxmium gap. To keep update the gap, we don't want to manually modify the default gap, but to add a "cnt" which will be divied by the gap. When making the comparsion, the real gap value is gap default value / cnt.
2. **Binary Search**: Our goal is to find the most difficult gap, and try to minimize it as much as possible. It now becomes a search problem. The gap is in between 1 ~ a[n-1]-a[0], and for each gap, we calculate the desire "cuts" to satisfy k. To calculate the desire "cuts", we should find the gap between each one, and then ceil(gap / most difficult gap) - 1 (check line 21 from solution 2). If the "cuts" is less than K, that means we have room to lower our difficulty by using the unused "cuts", so our search range is decreased by half from 1 ~ mb, else it will be mb + 1 ~ rb.

### Code

#### Priority Queue

```c
#include <bits/stdc++.h>

using namespace std;
struct node {
    int sum, cnt;
    node() {}
    node(int sum, int cnt)
        : sum(sum)
        , cnt(cnt)
    {
    }
    bool operator<(const node& b) const
    {
        int x = (sum / cnt) + (sum % cnt > 0); // sort by averged out by cnt
        int y = (b.sum / b.cnt) + (b.sum % b.cnt > 0);
        return x < y;
    }
};
int main(int argc, char* argv[])
{
    int T;
    int N, K;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N >> K;
        int m[N];
        memset(m, 0, sizeof m);
        for (int n = 0; n < N; ++n) {
            cin >> m[n];
        }
        int gap[N - 1];
        memset(gap, 0, sizeof gap);
        for (int i = 0; i < N - 1; ++i) {
            gap[i] = m[i + 1] - m[i];
        }
        if (K == 1) {
            sort(gap, gap + N - 1);
            if (N == 2)
                printf("Case #%d: %d\n", i, (gap[0] + 1) / 2);
            else
                printf(
                    "Case #%d: %d\n", i, max((gap[N - 2] + 1) / 2, gap[N - 3]));
        } else {
            priority_queue<node> q;
            for (int i = 0; i < N - 1; ++i) {
                q.push(node(gap[i], 1));
            }
            for (int i = 0; i < K; ++i) {
                auto p = q.top();
                q.pop();
                q.push(node(p.sum, p.cnt + 1)); // add one to split it
            }
            auto p = q.top();
            int res = (p.sum / p.cnt) + (p.sum % p.cnt > 0);
            printf("Case #%d: %d\n", i, res);
        }
    }
    return 0;
}

```

#### Binary search

```c
#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define ar array

int n, k, a[100000];

void solve()
{
    cin >> n >> k; // n: size of a, k: # of total insertions
    for (int i = 0; i < n; ++i)
        cin >> a[i];

    int lb = 1, rb = a[n - 1] - a[0]; // total difference
    while (lb < rb) {
        int mb = (lb + rb) / 2; // guess the most optimal difference is mb
        int k2 = 0;
        for (int i = 1; i < n; ++i) {
            int d = a[i] - a[i - 1];
            k2 += (d + mb - 1) / mb - 1; // # of all inserted class if mb is the optimal
        }
        if (k2 <= k) // if less than k, we can potentially decrease the difficulity
            rb = mb;
        else // or we have to increase the difficulity
            lb = mb + 1;
    }
    cout << lb << "\n";
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t, i = 1;
    cin >> t;
    while (t--) {
        cout << "Case #" << i << ": ";
        solve();
        ++i;
    }
}
```

## Bundling

Pip has N strings. Each string consists only of letters from A to Z. Pip would like to bundle their strings into groups of size K. Each string must belong to exactly one group.

The score of a group is equal to the length of the longest prefix shared by all the strings in that group. For example:
The group {RAINBOW, RANK, RANDOM, RANK} has a score of 2 (the longest prefix is 'RA').
The group {FIRE, FIREBALL, FIREFIGHTER} has a score of 4 (the longest prefix is 'FIRE').
The group {ALLOCATION, PLATE, WORKOUT, BUNDLING} has a score of 0 (the longest prefix is '').

Please help Pip bundle their strings into groups of size K, such that the sum of scores of the groups is maximized.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the two integers N and K. Then, N lines follow, each containing one of Pip's strings.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum sum of scores possible.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ N ≤ 105.
2 ≤ K ≤ N.
K divides N.
Each of Pip's strings contain at least one character.
Each string consists only of letters from A to Z.

Test set 1
Each of Pip's strings contain at most 5 characters.

Test set 2
The total number of characters in Pip's strings across all test cases is at most 2 × 106.

Samples

Input 1

2
2 2
KICK
START
8 2
G
G
GO
GO
GOO
GOO
GOOO
GOOO

Output 1

Case #1: 0
Case #2: 10


Input 2
 	
1
6 3
RAINBOW
FIREBALL
RANK
RANDOM
FIREWALL
FIREFIGHTER

Output 2

Case #1: 6

Sample #1
In Case #1, Pip can achieve a total score of 0 by make the groups:
{KICK, START}, with a score of 0.

In Case #2, Pip can achieve a total score of 10 by make the groups:
{G, G}, with a score of 1.
{GO, GO}, with a score of 2.
{GOO, GOO}, with a score of 3.
{GOOO, GOOO}, with a score of 4.

Sample #2
In Case #1, Pip can achieve a total score of 6 by make the groups:
{RAINBOW, RANK, RANDOM}, with a score of 2.
{FIREBALL, FIREWALL, FIREFIGHTER}, with a score of 4.

### Analysis

Assume each bundle has prefix as $P_i$, and the $CNT_i$ represents the number of strings shares that prefix. 
Assign k string to the bundle, now we have $CNT_i \% k$ string left. 
Do the same thing for preifx $P_{i + 1}$ which has a $CNT_{i+1} < CNT_i$, now we have $CNT_{i + 1} \% k$ left. 
Keep this procedure until $CNT_j \% k == 0$ which means all the string have assigned to a particular bundle.

Now the problem becomes finding the total count. 
Split into n/k groups, and each group has k strings. Use trie to find the common prefix. 
Each trie node has 26 children nodes, and one cnt int for counting the number of prefix exist by the current node. 
Insert: insert into trie and update the cnt for each ending character node. 
Query: just search from the root of the trie and traverse through the last level of the trie, because all the nodes from root has a count that represent the occurance of word that is ended with node character.

### Code

```c
#include <bits/stdc++.h>
using namespace std;
 
#define endl "\n"
#define int long long

const int N = 1e5 + 5;

typedef struct data
{
	data* bit[26];
	int cnt = 0;
}trie;

trie* head;

void insert(string &s)
{
	trie* cur = head;
	for(auto &it:s)
	{
		int b = it - 'A';
		if(!cur->bit[b])
			cur->bit[b] = new trie(); // create new node if not exist
		cur = cur->bit[b]; // proceed through next character
		cur->cnt++; // end with current character
	}
}

int n, k;
string s[N];

int query(trie* cur)
{
	if(!cur)
		return 0;
	int ans = (cur -> cnt / k); // there are k words each, so there are k times repeat counts
	for(int i = 0; i <= 25; i++)
		if(cur -> bit[i])
			ans += query(cur -> bit[i]); // proceeds to next level and check the count
	return ans;
}
 
int main()
{
	int t;
	cin >> t;
	int tc = 0; 
	while(t--)
	{
		head = new trie();
		tc++;
		cin >> n >> k;
		for(int i = 1; i <= n; i++)
		{
			cin >> s[i];
			insert(s[i]);
		}
		int ans = query(head);
		cout << "Case #" << tc << ": " << ans << endl;
 	}	
	return 0;
}
```