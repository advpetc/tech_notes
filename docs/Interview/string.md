## Reverse

Reverse "I love yahoo" to "yahoo love I"

1. reverse entire string: "oohay evol I"
2. reverse each word: "yahoo love I"

### Trick

Right shift a given string by n characters.

Assumptions

The given string is not null.
n >= 0.
Examples

"abc", 4 -> "cab"

```c
class Solution {
 public:
  string rightShift(string s, int n) {
    // write your solution here
    if (!n || s == "") return s;
    reverse(s.begin(), s.end());
    int shift = n % s.size();
    reverse(s.begin() + shift, s.end());
    reverse(s.begin(), s.begin() + shift);
    return s;
  }
};
```

## Replacement

Replace "student" to "stuXXt" -> replace all "den" to "XX" Note that replacement may have different size

Use two pointers method
+ If p.size() > replaced part: 
  1. add space to the end of the original string (buffer zone)
  2. start from right to left to replace (replace in reversed order)
+ If p.size() < replaced part
  1. start from left to right. replace if met and continue on

> https://app.laicode.io/app/problem/649

```c
// TODO
for (int i = 0, j = 0; i < n; ++i) {
    if (s[i] == p[j]) {
        j++;
        s[i] = p[j];
    }
}
```



