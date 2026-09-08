# 0003. Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest substring** without repeating characters.

 

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Example 4:**

```
Input: s = ""
Output: 0
```

 

**Constraints:**

- `0 <= s.length <= 5 * 104`
- `s` consists of English letters, digits, symbols and spaces.

## Analysis

1. Method 1: keep a 128-length `int cnt` array. When moving the sliding window:
   1. If the current right's cnt == 0, we need to update our global result to see if it's greater than the current maximum window length.
   2. Otherwise, we need to move the left pointer to the right until `cnt == 0` (this is the only way, since our right pointer is always moving right, so there is no way to "delete" any character from the window).

2. Method 2: still use a 128-length `int` array, but we now use it to store the **last occurrence of the current character's index**.
   1. In each iteration, we first compare against the current window's left, because the last occurrence of the current character is going to bound our window (otherwise it will have at least a window with two duplicate characters).
   2. Update our index map with the most recent index.
   3. Update our global length.

* Time: $O(n)$
* Space: $O(128)$ or $O(n)$ depending on the range of characters

## Code 1

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        int cnt[128] = {0};
        for (int r = 0, l = 0; r < s.size(); ) {
            if (cnt[s[r]] == 0) {
                res = max(res, r - l + 1);
                cnt[s[r ++]] ++;
            } else {
                cnt[s[l ++]] --;
            }
        }
        return res;
    }
};
```

## Code 2

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> idx(128, -1);
        int left = -1, res = 0;
        for (int i = 0; i < s.size(); ++i) {
            left = max(left, idx[s[i]]);
            idx[s[i]] = i;
            res = max(res, i - left);
        }
        return res;
    }
};
```

