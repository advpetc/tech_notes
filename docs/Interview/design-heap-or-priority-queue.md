# Property for a heap (min heap for example)

1. Complete Tree
  - root = i => left = i * 2 + 1, right = i * 2 + 2 
  - left/right = i => root = (i - 1) / 2
  - the transferred array (0-based) is unique => the transferred tree is unique
2. Any child is greater than its parent (top one/root node is the smallest one)
3. Left and Right child don't have any relationship (not bst) -> cannot search in $O(N \times log(N))$
4. Advantage of using an array: root -> children and child -> root or child -> grandfather easily

## Operations

1. Trickle Up (offer/push)
  - adding new element to the tail

```c
while ((i - 1) / 2 >= 0 && arr[i] < arr[(i - 1) / 2]) {
  swap(arr[i], arr[(i - 1) / 2]);
  i = (i - 1) / 2;
}
```

2. Trickle Down (poll/pop)
  - remove the root of the tree

```c
#define (left) (i * 2 + 1)
#define (right) (i * 2 + 2)
int i = 0;
while (left < arr.size() && (arr[i] > arr[left] || arr[i] > arr[right])) {
  int tmp;
  if (arr[left] < arr[right]) tmp = left; 
  else tmp = right;
  swap(arr[i], arr[tmp]);
  i = tmp;
}
```

## Heap Sort

sort the array by regarding the array as a heap:
keep "polling/pop" and place the biggest/smallest one to the front

1. heapify (trickle down from n to 0): $O(n)$
2. n times poll/pop: $O(n \times log(n))$

**However, it's not a preferrable sorting algorithm**

1. runtime overhead
2. poor locality (a lot of swap that addresses are not nearby)
3. hard to parallelize/distribute

