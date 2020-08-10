## String

### `substr` Space: $O(n)$, Time: $O(n)$

s.substr(pos, n) 

Return a string containing n characters from s starting at pos. pos defaults to 0. n defaults to a value that causes the library to **copy** all the characters in s starting from pos.

```c
string s("hello world");
string s2 = s.substr(0, 5); // s2 = hello
string s3 = s.substr(6);    // s3 = world
string s4 = s.substr(6, 11);// s4 = world
string s5 = s.substr(12);   // throws an out_of_range exception
```

