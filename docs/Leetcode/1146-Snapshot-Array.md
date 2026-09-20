# 1146. Snapshot Array

Implement a SnapshotArray that supports the following interface:

- `SnapshotArray(int length)` initializes an array-like data structure with the given length. **Initially, each element equals 0**.
- `void set(index, val)` sets the element at the given `index` to be equal to `val`.
- `int snap()` takes a snapshot of the array and returns the `snap_id`: the total number of times we called `snap()` minus `1`.
- `int get(index, snap_id)` returns the value at the given `index`, at the time we took the snapshot with the given `snap_id`

 

**Example 1:**

```
Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
```

 

**Constraints:**

- `1 <= length <= 5 * 10^4`
- `0 <= index < length`
- `0 <= val <= 10^9`
- `0 <= snap_id <` (the total number of times we call `snap()`)
- At most `5 * 10^4` calls will be made to `set`, `snap`, and `get`.

## Analysis

To save space, we shouldn't record the **whole** array each time we take a snapshot. Instead, we only keep track of the entries that were updated. However, this causes a problem:

1. Set `index1` at `snapId1` to a value.
2. Read `index2` at `snapId1`.

Since only `index1` was updated at `snapId1`, we didn't store any value for `index2` at `snapId1`. Instead, we should use the old value from `snapId0` (or, more generally, the value before `snapId1`). This means we need to find the biggest stored snapId that is smaller than or equal to the snapId we are querying. This works because snapIds are recorded in increasing order as the operations are made.

For each index, we keep a sorted map from `snap_id` to `value`, which is only written when the value changes. Every index starts with `{0: 0}` (snapId 0, value 0), and `id` is the id of the next snapshot to be taken, so a `set` made now belongs to snapshot `id`. If `set` is called on the same index several times before the next `snap()`, the later call simply overwrites the earlier one.

```text
Naive: copy the whole array at every snap()

  snap 0:  [5, 0, 0]
  snap 1:  [6, 0, 0]
  snap 2:  [6, 7, 0]        -> length x snapCount cells

This solution: only store the changes, per index (snap_id -> value)

  index 0:  { 0 -> 5,  1 -> 6 }
  index 1:  { 0 -> 0,  2 -> 7 }
  index 2:  { 0 -> 0 }      -> length + number of set() calls
```

The diagram above comes from this sequence of operations (length = 3):

```text
  set(0, 5)   snap() = 0   set(0, 6)   snap() = 1   set(1, 7)   snap() = 2
  id = 0      id -> 1      id = 1      id -> 2      id = 2      id -> 3
```

To answer `get(index, snap_id)`, we look for the last key in `data[index]` that is smaller than or equal to `snap_id`:

```text
get(1, 1):   data[1] = { 0 -> 0, 2 -> 7 }

  keys:       0            2
  values:     0            7
              ^            ^
              |            |
        it-- (answer)   upper_bound(1)  (first key > 1)

  answer = 0

get(0, 2):   data[0] = { 0 -> 5, 1 -> 6 }

  keys:       0            1            end()
  values:     5            6
                           ^            ^
                           |            |
                     it-- (answer)   upper_bound(2)  (no key > 2)

  answer = 6
```

In C++, `upper_bound(x)` returns an iterator to the first key that is **strictly greater** than `x` (`lower_bound(x)` is the one that returns the first key that is greater than or equal to `x`). Since we want the last key that is smaller than or equal to `snap_id`, we move the iterator **back** one position after calling `upper_bound`. This is always safe, because every index starts with the key `0` and `snap_id >= 0`, so `upper_bound` can never return `begin()`.

* Time: $O(length)$ for initialization, $O(\log k)$ for `set`, $O(1)$ for `snap`, and $O(\log k)$ for `get`, where $k$ is the number of entries stored for that index (at most the number of `set` calls made on it).
* Space: $O(length + S)$, where $S$ is the number of `set` calls, since only the updated entries are stored (instead of $O(length \times snapCount)$ when copying the whole array on every snapshot).

## Code

```c++
class SnapshotArray {
private:
    vector<map<int, int>> data; // data[index]: snap_id -> value, only stored when the value changes
    int id;                     // id of the next snapshot

public:
    SnapshotArray(int length) {
        data.assign(length, {{0, 0}});
        id = 0;
    }

    void set(int index, int val) {
        data[index][id] = val;
    }

    int snap() {
        return id++;
    }

    int get(int index, int snap_id) {
        auto it = data[index].upper_bound(snap_id); // first key > snap_id
        --it;                                       // last key <= snap_id
        return it->second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */
```
