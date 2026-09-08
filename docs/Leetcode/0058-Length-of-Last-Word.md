# 0058. Length of Last Word

Given a string `s` consists of some words separated by spaces, return *the length of the last word in the string. If the last word does not exist, return* `0`.

A **word** is a maximal substring consisting of non-space characters only.

 

**Example 1:**

```
Input: s = "Hello World"
Output: 5
```

**Example 2:**

```
Input: s = " "
Output: 0
```

 

**Constraints:**

- `1 <= s.length <= 104`
- `s` consists of only English letters and spaces `' '`.

## Analysis

Our goal is to find the first word that is either between two spaces or whose left character is a space. In order to do so, we just need to check from the rightmost position to the left; once we find a character that is not a space, we update our counter. If the counter is greater than one and we meet another space, that means we have already found our target string, and we can just return the counter. The worst case is when the whole string consists of spaces OR no space at all -- in such a case, we need to iterate the entire string from the end to the start.

* Time: $O(n)$
* Space: $O(1)$

## Code

```c++
class Solution {
public:
    int lengthOfLastWord(string s) {
        int res = 0;
        for (int i = s.size() - 1; i >= 0; --i) {
            if (res > 0 && s[i] == ' ') return res;
            if (s[i] != ' ') res ++;
        }
        return res;
    }
};
```

