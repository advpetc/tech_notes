# 0341. Flatten Nested List Iterator

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the `NestedIterator` class:

- `NestedIterator(List<NestedInteger> nestedList)` Initializes the iterator with the nested list `nestedList`.
- `int next()` Returns the next integer in the nested list.
- `boolean hasNext()` Returns `true` if there are still some integers in the nested list and `false` otherwise.

Your code will be tested with the following pseudocode:

```
initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
```

If `res` matches the expected flattened list, then your code will be judged as correct.

 

**Example 1:**

```
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
```

**Example 2:**

```
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
```

 

**Constraints:**

- `1 <= nestedList.length <= 1000`
- The values of the integers in the nested list is in the range `[-10^6, 10^6]`.

## Analysis

`NestedInteger` gives us three operations: `isInteger()`, `getInteger()`, and `getList()`. Rather than eagerly flattening the whole structure in the constructor, we lazily flatten it using a stack, expanding a nested list only when we actually need to look past it.

We initialize the stack by pushing every top-level element in reverse order, so the first element ends up on top. `hasNext()` does the real work: it repeatedly looks at the top of the stack, and if that top element is itself a list rather than an integer, it pops it and pushes its children back on in reverse order, effectively "unwrapping" one level. It keeps unwrapping until the top of the stack is a genuine integer (in which case we return `true`) or the stack is empty (`false`). `next()` can then simply pop and return the integer that's guaranteed to be sitting on top, since `hasNext()` is expected to be called first per the problem's test harness.

* Time: `next()` and `hasNext()` are $O(1)$ amortized, since each nested list is unwrapped exactly once across the whole lifetime of the iterator; the total work across all calls is $O(n)$ where $n$ is the total number of integers and lists.
* Space: $O(n)$ for the stack in the worst case (e.g. a list nested `n` levels deep).

## Code

```c++
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

class NestedIterator {
public:
    stack<NestedInteger> stk;

    NestedIterator(vector<NestedInteger> &nestedList) {
        for (int i = nestedList.size() - 1; i >= 0; --i)
            stk.push(nestedList[i]);
    }

    int next() {
        int val = stk.top().getInteger();
        stk.pop();
        return val;
    }

    bool hasNext() {
        while (!stk.empty()) {
            NestedInteger cur = stk.top();
            if (cur.isInteger()) return true;
            stk.pop();
            const vector<NestedInteger>& list = cur.getList();
            for (int i = list.size() - 1; i >= 0; --i)
                stk.push(list[i]);
        }
        return false;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```
