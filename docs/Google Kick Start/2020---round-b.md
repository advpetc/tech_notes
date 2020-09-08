## Bike Tour

Problem
Li has planned a bike tour through the mountains of Switzerland. His tour consists of N checkpoints, numbered from 1 to N in the order he will visit them. The i-th checkpoint has a height of Hi.

A checkpoint is a peak if:
It is not the 1st checkpoint or the N-th checkpoint, and
The height of the checkpoint is strictly greater than the checkpoint immediately before it and the checkpoint immediately after it.

Please help Li find out the number of peaks.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integer N. The second line contains N integers. The i-th integer is Hi.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of peaks in Li's bike tour.

Limits
Time limit: 10 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ Hi ≤ 100.

Test set 1
3 ≤ N ≤ 5.

Test set 2
3 ≤ N ≤ 100.

Sample

Input
 	
Output
 
4
3
10 20 14
4
7 7 7 7
5
10 90 20 90 10
3
10 3 10

  
Case #1: 1
Case #2: 0
Case #3: 2
Case #4: 0

  
In sample case #1, the 2nd checkpoint is a peak.
In sample case #2, there are no peaks.
In sample case #3, the 2nd and 4th checkpoint are peaks.
In sample case #4, there are no peaks.

### Analysis

In order to satisfy the requirement, on a peak, it has to be greater than two neighbours points -> it turns out we can just check for every points between 1 to n - 1, if nums[i] > nums[i - 1] && nums[i] > nums[i + 1], then we increment the counter by 1.

* Time: $O(n)$
* Space: $O(1)$

### Code

```c

// Problem : Bike Tour
// Contest : Google Coding Competitions - Round B 2020 - Kick Start 2020
// URL : https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6
// Memory Limit : 1024 MB
// Time Limit : 10000 ms
// Powered by CP Editor (https://github.com/cpeditor/cpeditor)

#include <bits/stdc++.h>

using namespace std;
int nums[110];
int main() {
  int T, n;
  cin >> T;
  for (int t = 0; t < T; ++t){
    cin >> n;
    int cnt = 0;

    for (int i = 0; i < n; ++i)
      cin >> nums[i];

    for (int i = 1; i < n - 1; ++i) {
    	if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) cnt++;
    }

    printf("Case #%d: %d\n", t + 1, cnt);
  }
}

```

## Bus Routes

Problem
Bucket is planning to make a very long journey across the countryside by bus. Her journey consists of N bus routes, numbered from 1 to N in the order she must take them. The buses themselves are very fast, but do not run often. The i-th bus route only runs every Xi days.

More specifically, she can only take the i-th bus on day Xi, 2Xi, 3Xi and so on. Since the buses are very fast, she can take multiple buses on the same day.

Bucket must finish her journey by day D, but she would like to start the journey as late as possible. What is the latest day she could take the first bus, and still finish her journey by day D?

It is guaranteed that it is possible for Bucket to finish her journey by day D.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the two integers N and D. Then, another line follows containing N integers, the i-th one is Xi.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the latest day she could take the first bus, and still finish her journey by day D.

Limits
Time limit: 10 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ Xi ≤ D.
1 ≤ N ≤ 1000.
It is guaranteed that it is possible for Bucket to finish her journey by day D.

Test set 1
1 ≤ D ≤ 100.

Test set 2
1 ≤ D ≤ 10^12.

Sample

Input
 	
Output
 
3
3 10
3 7 2
4 100
11 10 5 50
1 1
1

  
Case #1: 6
Case #2: 99
Case #3: 1

  
In Sample Case #1, there are N = 3 bus routes and Bucket must arrive by day D = 10. She could:
Take the 1st bus on day 6 (X1 = 3),
Take the 2nd bus on day 7 (X2 = 7) and
Take the 3rd bus on day 8 (X3 = 2).

In Sample Case #2, there are N = 4 bus routes and Bucket must arrive by day D = 100. She could:
Take the 1st bus on day 99 (X1 = 11),
Take the 2nd bus on day 100 (X2 = 10),
Take the 3rd bus on day 100 (X3 = 5) and
Take the 4th bus on day 100 (X4 = 50),

In Sample Case #3, there is N = 1 bus route and Bucket must arrive by day D = 1. She could:
Take the 1st bus on day 1 (X1 = 1).

### Analysis

Decouple the question: the question is asking from day 1 to day D (could be very big), what is the maximum number that from current number to D, all the num[i] can be divisible.

From the example, we can find we can greedy search from day D backward to day 1. However, we can still do faster than that.

We can use binary search to decrease the search space by half everytime we find a valid day, say day mid.
1. if day mid works, then we can discard 1 to day mid - 1.
2. if day mid isn't working, then we should discard day mid to day D.

Now the problem becomes how to efficiently check if day works. We find if day x won't work for a num[i], the minimal steps to increase x is by adding the modulus reminder to current day. e.g. to make 3 + x divisible by 4, the smallest x is 1 (getting 1 by 4 - 3 % 4). We can do so for all the days from num[0] until to the last nums. Finally, we just need to check if the answer is less or equal than our range.

* Time: $O(log_2{D} \times n)$
* Space: $O(1)$

### Code

```c
// Problem : Bus Routes
// Contest : Google Coding Competitions - Round B 2020 - Kick Start 2020
// URL :
// https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf
// Memory Limit : 1024 MB
// Time Limit : 10000 ms
// Powered by CP Editor (https://github.com/cpeditor/cpeditor)

#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int T, n;
ll d;
ll num[1010];

bool works(ll mid) {
  for (int i = 0; i < n; ++i) {
    if (mid % num[i] != 0) 
    	mid += (num[i] - mid % num[i]);
  }
  return mid <= d;
}
	
int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> n >> d;
    for (int i = 0; i < n; ++i) cin >> num[i];
    ll l = 0, r = d;
    while (l < r) {
      ll m = (l + r + 1) >> 1;
      if (works(m))
        l = m;
      else
        r = m - 1;
    }
    printf("Case #%d: %llu\n", t, l);
  }
  return 0;
}
```

## Robot Path Decoding

Problem
Your country's space agency has just landed a rover on a new planet, which can be thought of as a grid of squares containing 109 columns (numbered starting from 1 from west to east) and 109 rows (numbered starting from 1 from north to south). Let (w, h) denote the square in the w-th column and the h-th row. The rover begins on the square (1, 1).

The rover can be maneuvered around on the surface of the planet by sending it a program, which is a string of characters representing movements in the four cardinal directions. The robot executes each character of the string in order:
N: Move one unit north.
S: Move one unit south.
E: Move one unit east.
W: Move one unit west.
There is also a special instruction X(Y), where X is a number between 2 and 9 inclusive and Y is a non-empty subprogram. This denotes that the robot should repeat the subprogram Y a total of X times. For example:
2(NWE) is equivalent to NWENWE.
3(S2(E)) is equivalent to SEESEESEE.
EEEE4(N)2(SS) is equivalent to EEEENNNNSSSS.

Since the planet is a torus, the first and last columns are adjacent, so moving east from column 109 will move the rover to column 1 and moving south from row 109 will move the rover to row 1. Similarly, moving west from column 1 will move the rover to column 109 and moving north from row 1 will move the rover to row 109. Given a program that the robot will execute, determine the final position of the robot after it has finished all its movements.

Input
The first line of the input gives the number of test cases, T. T lines follow. Each line contains a single string: the program sent to the rover.

Output
For each test case, output one line containing Case #x: w h, where x is the test case number (starting from 1) and w h is the final square (w, h) the rover finishes in.

Limits
Time limit: 10 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
The string represents a valid program.
The length of each program is between 1 and 2000 characters inclusive.

Test set 1
The total number of moves the robot will make in a single test case is at most 104.

Test set 2
No additional constraints.

Sample

Input
``` 
4
SSSEEE
N
N3(S)N2(E)N
2(3(NW)2(W2(EE)W))
```

  
Output
```
Case #1: 4 4
Case #2: 1 1000000000
Case #3: 3 1
Case #4: 3 999999995
```

  
In Sample Case #1, the rover moves three units south, then three units east.

In Sample Case #2, the rover moves one unit north. Since the planet is a torus, this moves it into row 109.

In Sample Case #3, the program given to the rover is equivalent to NSSSNEEN.

In Sample Case #4, the program given to the rover is equivalent to NWNWNWWEEEEWWEEEEWNWNWNWWEEEEWWEEEEW.

### Analysis

By observation, 