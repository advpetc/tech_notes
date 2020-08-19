> https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem

```c
public class Solution {
    public List<Integer> slidingWindowTemplateByHarryChaoyangHe(String s, String t) {
        //init a collection or int value to save the result according the question.
        List<Integer> result = new LinkedList<>();
        if(t.length()> s.length()) return result;
        
        //create a hashmap to save the Characters of the target substring.
        //(K, V) = (Character, Frequence of the Characters)
        Map<Character, Integer> map = new HashMap<>();
        for(char c : t.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        //maintain a counter to check whether match the target string.
        int counter = map.size();//must be the map size, NOT the string size because the char may be duplicate.
        
        //Two Pointers: begin - left pointer of the window; end - right pointer of the window
        int begin = 0, end = 0;
        
        //the length of the substring which match the target string.
        int len = Integer.MAX_VALUE; 
        
        //loop at the begining of the source string
        while(end < s.length()){
            
            char c = s.charAt(end);//get a character
            
            if( map.containsKey(c) ){
                map.put(c, map.get(c)-1);// plus or minus one
                if(map.get(c) == 0) counter--;//modify the counter according the requirement(different condition).
            }
            end++;
            
            //increase begin pointer to make it invalid/valid again
            while(counter == 0 /* counter condition. different question may have different condition */){
                
                char tempc = s.charAt(begin);//***be careful here: choose the char at begin pointer, NOT the end pointer
                if(map.containsKey(tempc)){
                    map.put(tempc, map.get(tempc) + 1);//plus or minus one
                    if(map.get(tempc) > 0) counter++;//modify the counter according the requirement(different condition).
                }
                
                /* save / update(min/max) the result if find a target*/
                // result collections or result int value
                
                begin++;
            }
        }
        return result;
    }
}
```

## 438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of **lowercase English letters** only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

```c
class Solution {
public:
    vector<int> findAnagrams(string s, string p)
    {
        if (s.empty())
            return {};
        vector<int> res, m(256, 0);
        int left = 0, right = 0, cnt = p.size(), n = s.size();
        for (char c : p)
            ++m[c];
        while (right < n) {
            if (m[s[right++]]-- >= 1)
                --cnt;
            if (cnt == 0)
                res.push_back(left);
            if (right - left == p.size() && m[s[left++]]++ >= 0)
                ++cnt;
        }
    }
};
```

## 76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

```c
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> m;
        for (char c : t) {
            m[c]++;
        }
        int sz = m.size();
        string res;
        for (int i = 0, j = 0, cnt = 0; i < s.size(); ++i) {
            if (m[s[i]] == 1)
                cnt++;
            m[s[i]]--;
            while (m[s[j]] < 0) {
                m[s[j++]]++;
            }
            
            if (cnt == sz) {
                if (res.empty() || res.size() > i - j + 1)
                    res = s.substr(j, i - j + 1);
            }
        }
        return res;
    }
};
```

## 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

```c
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0, end = 0;
        vector<int> v(128, 0);
        int res = 0;
        for (int i = 0, j = 0; i < s.size(); ++i) {
            v[s[i]]++;
            while (v[s[i]] > 1) {
                v[s[j++]]--;
            }
            res = max(res, i - j + 1);
        }
        return res;
    }
};
```

## 30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

```c
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        if (s.empty() || words.empty()) return {};
        int n = s.size(), len = words[0].size(), total = words.size(), cnt = total;
        vector<int> res;
        unordered_map<string, int> counts;
        for (string s : words) counts[s]++;
        for (int i = 0; i < len; i++) {
            unordered_map<string, int> wordcnt = counts;
            cnt = total;
            for (int j = i; j + len <= n; j += len) {
                string cur = s.substr(j, len);
                if (wordcnt[cur]-- > 0) cnt--;
                if (j - total*len >= 0) {                  
                    string out = s.substr(j - total*len, len); // the word out side of current sliding window
                    if (++wordcnt[out] > 0) cnt++;
                }
                if (cnt == 0) res.push_back(j - (total-1)*len);                
            }
        }
        return res;
    }
};
```

## 30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.



Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

```c
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        if (s.empty() || words.empty()) return {};
        int n = s.size(), len = words[0].size(), total = words.size(), cnt = total;
        vector<int> res;
        unordered_map<string, int> counts;
        for (string s : words) counts[s]++;
        for (int i = 0; i < len; i++) {
            unordered_map<string, int> wordcnt = counts;
            cnt = total;
            for (int j = i; j + len <= n; j += len) {
                string cur = s.substr(j, len);
                if (wordcnt[cur]-- > 0) cnt--;
                if (j - total*len >= 0) {                  
                    string out = s.substr(j - total*len, len); // the word out side of current sliding window
                    if (++wordcnt[out] > 0) cnt++;
                }
                if (cnt == 0) res.push_back(j - (total-1)*len);                
            }
        }
        return res;
    }
};
```

## 159. Longest Substring with At Most Two Distinct Characters

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: tis "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: tis "aabbb" which its length is 5.

### Analysis

**Use left only**

Use ```map<char, int>``` to record the frequency of character in the range of left - i (inclusive). Once the keys is greater than 2, try moves left by 1 unit and update the map if the frequency is 0. Time: O(n), Space: O(1) because size if always 2 entry of key-value pair.

```c
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int res = 0, left = 0;
        unordered_map<char, int> m;
        for (int i = 0; i < s.size(); ++i) {
            m[s[i]]++;
            while (m.size() > 2) {
                if (--m[s[left]] == 0) m.erase(s[left]);
                ++left;
            }
            res = max(res, i - left + 1);
        }
        return res;
    }
};
```

**Use left and right** Space is optimized, but a little unintuitive.

Use two pointers to represent the window. If s[i] == s[i-1], there is no update to the count of distinct elements. If right is not equal to the current one, that means there is a update (+1) to the total count, so we stop and update our res with the current i - left (window is now left - i). Because it only allows two characters, we should skip the ith character and start from right + 1 as left.

```c
#include <bits/stdc++.h>

using namespace std;

int main() {
	cin >> s;
	int left = 0, right = -1, res = 0, sz = s.size();
	for (int i = 1; i < sz; ++i) {
		if (s[i] == s[i - 1]) continue;
		if (right >= 0 && s[right] != s[i]) {
			res = max(res, i - left);
			left = right + 1;
		}
		right = i - 1;
	}
	cout << max(res, sz - left);
	return 0;
}
```

### Variation: with K different words

if the character is in range of 'a' to 'z', then maintain a int array with size of 26.

```c
class Solution {
 public:
  string longest(string input, int k) {
    int n = input.size();
    int l = 0, r = 0, cnt = 0, len = 0;
    string res = "";
    int v[26];
    memset(v, 0, sizeof v);
    while (l < n - 1) {
      while (cnt < k && r < n) {
        if (v[input[r] - 'a']++ == 0) cnt++;
        r++;
      }
      if (cnt == k && len < r - l) { // case 1: cnt still in the range so, r doesn't overcount
        len = r - l;
        res = input.substr(l, len);
      } else if (len < r - l - 1) { // case 2: cnt is greater than k by 1, r overcount by 1
        len = r - l - 1;
        res = input.substr(l, len);
      }
      if (--v[input[l] - 'a'] == 0) cnt--;
      l++;
    }
    return res;
  }
};

```

```c
class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        int res = 0, left = 0;
        unordered_map<char, int> m;
        for (int i = 0; i < s.size(); ++i) {
            ++m[s[i]];
            while (m.size() > k) {
                if (--m[s[left]] == 0) m.erase(s[left]);
                ++left;
            }
            res = max(res, i - left + 1);
        }
        return res;
    }
};
```

