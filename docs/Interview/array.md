## Array Deduplication 1

Given a sorted integer array, remove duplicate elements. For each group of elements with the same value keep only one of them. Do this in-place, using the left side of the original array and maintain the relative order of the elements of the array. Return the array after deduplication.

{1, 2, 2, 3, 3, 3} → {1, 2, 3} keep one if there is a duplication

### Analysis

1. idx: (0, idx] is the processed array (return array[0:idx])
2. condition 1: check if equal to previous element
3. condition 2: put the non-duplicated element into the correct spot

### Code

```c
class Solution {
 public:
  vector<int> dedup(vector<int> array) {
    // write your solution here
    if (array.empty()) return {};
    int idx = 1;
    for (int i = 1; i < array.size(); ++i) {
      if (array[i] == array[i - 1]) continue;
      array[idx++] = array[i]; // 1,2,2: first 2 will be placed but not the second 2
    }
    return vector<int>(array.begin(), array.begin() + idx);
  }
};

```

## Array Deduplication 2

Given a sorted integer array, remove duplicate elements. For each group of elements with the same value keep at most two of them. Do this in-place, using the left side of the original array and maintain the relative order of the elements of the array. Return the array after deduplication.

{1, 2, 2, 3, 3, 3} → {1, 2, 2, 3, 3} keep two duplicated

### Analysis

1. idx: (0, idx] is the processed array (return array[0:idx])
2. condition 1: check if equal to last two from the top of the stack
3. condition 2: put the non-duplicated element into the correct spot

e.g. {1,2,2,3,3,3}
i = 2 => 1, 2, 2 (keep second 2, since i - 2 = 0 -> num[0] != num[2])
i = 5 => 1, 2, 2, 3, 3 (discard the third 3, since i - 2 = 3 -> num[3] == num[5])

### Code

```c
class Solution {
 public:
  vector<int> dedup(vector<int> array) {
    // write your solution here
    if (array.size() <= 2) return array;
    int j = 2;
    for (int i = 2; i < array.size(); ++i) {
      if (array[i] != array[j - 2]) continue;
      else array[j++] = array[i];
    }
    return vector<int>(array.begin(), array.begin() + j);
  }
};

```

## Array Deduplication 1

Given a sorted integer array, remove duplicate elements. For each group of elements with the same value do not keep any of them. Do this in-place, using the left side of the original array and and maintain the relative order of the elements of the array. Return the array after deduplication.

{1, 2, 2, 3, 3, 3} → {1}

{1,1,2,3,3,5,5,5,2} -> {2,2}

### Analysis

If the top of stack is equal to current element, set the flag to true AND don't update the stack. If the flag is true and current element isn't the same as the top of the stack, unset the flag and use the current element as the new top of the stack, since the old top has a duplicated element already. If the current element isn't equal to the top of stack and the flag isn't true, we can normally proceed it to put the current element at the top of the stack. The meaning of flag is for checking any ongoing element other than current duplicated element on the stack, we keep it on the stack temporarily and replace it with the first element that is not equal to the duplicated element. Finally, if the flag is true, it means we should discard the last element since it is duplicate but we still keep it on the stack.

### Code

```c
class Solution {
 public:
  vector<int> dedup(vector<int> array) {
    // write your solution here
    if (array.size() <= 1) return array;
    int j = 0;
    bool flag = false;
    for (int i = 1; i < array.size(); ++i) {
      if (array[i] == array[j]) flag = true;
      else if (flag) {
        array[j] = array[i];
        flag = false;
      } else array[++j] = array[i];
    }
    if (flag) j--;
    return vector<int>(array.begin(), array.begin() + j + 1);
  }
};

```

## Array Deduplication IV

Given an unsorted integer array, remove adjacent duplicate elements repeatedly, from left to right. For each group of elements with the same value do not keep any of them.

Do this in-place, using the left side of the original array. Return the array after deduplication.

Assumptions

The given array is not null
Examples

{1, 2, 3, 3, 3, 2, 2} → {1, 2, 2, 2} → {1}, return {1}

### Analysis

Now the job is consectively deduplicate with the top of the stack.

1. check if current top is equal to current element, if not equal, put the current element onto the stack.
2. if equal to the top, then we need to consectively deduplicate the same adjacent elements, and pop the element from the top of the stack (`slow--`).

### Code

```c
class Solution {
 public:
  vector<int> dedup(vector<int> a) {
    int slow = 0, fast = 0, n = a.size();
    while (fast < n) {
      if (slow == 0 || a[slow - 1] != a[fast]) a[slow++] = a[fast++];
      else {
        int curr = fast + 1;
        while (curr < n && a[curr] == a[fast]) curr++;
        slow--;
        fast = curr;
      }
    }
    return vector<int>(a.begin(), a.begin() + slow);
  }
};

```

