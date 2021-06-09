## Data structure and algorithm using golang

Most questions are from Leetcode.

## Map

### Declaration

Declare a map using `m := make(map[int]int)`

### Check if exist

```go
func twoSum(nums []int, target int) []int {
	m := make(map[int]int) // map[key]value
  for k, v := range nums { // k: idx, v: value
    // check if targe - v is in the map
		if idx, ok := m[target-v]; ok {
			return []int{idx, k}
		}
		m[v] = k
	}
	return nil
}
```

## Linkedlist

Initialize a new struct object (a `ListNode`) using `head := &ListNode{Val: 0}`

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	head := &ListNode{Val: 0}
	n1, n2, carry, current := 0, 0, 0, head
  // no while loop in Go
	for l1 != nil || l2 != nil || carry != 0 {
		if l1 == nil {
			n1 = 0
		} else {
			n1 = l1.Val
			l1 = l1.Next
		}
		if l2 == nil {
			n2 = 0
		} else {
			n2 = l2.Val
			l2 = l2.Next
		}
		current.Next = &ListNode{Val: (n1 + n2 + carry) % 10}
		current = current.Next
		carry = (n1 + n2 + carry) / 10
	}
	return head.Next
}

```

## Casting

Down/Up casting:

```go
a, b = 0, 0
float64(a + b) / 2 // this will convert interger to float64
```

## Slice and Array

### Declaration of slice

Using `arr := make([]rune, 0)` to declare an array with `rune` (alias to `int32`) and with the size of`0`. 

### Declaration of array

Declare an 2d array with **length**:

!!! note
    the difference between slice and array is array need to provide a constant size

```go
c := [5][5]uint8{}
fmt.Println(c)
/*
[[0 0 0 0 0] [0 0 0 0 0] [0 0 0 0 0] [0 0 0 0 0] [0 0 0 0 0]]
*/
```



### Create 2d slice:

```go
a := make([][]uint8, dy) // dy is the number of rows
for i := range a { // have to write a loop to initialize the columns
    a[i] = make([]uint8, dx)
}
```

### Initialize slice with default values

if you have default values (composite literal):

```go
a := [][]uint8{
    {0, 1, 2, 3},
    {4, 5, 6, 7},
}
fmt.Println(a) // Output is [[0 1 2 3] [4 5 6 7]]


b := []uint{10: 1, 2} // first 10 values are 1s 
fmt.Println(b) // Prints [0 0 0 0 0 0 0 0 0 0 1 2]
```

### Append

```go
newS := make([]rune, 0)  // create an array
newS = append(newS, '#') // append to the end
for _, c := range s {
  newS = append(newS, c)
  newS = append(newS, '#') // add a # for each character
}
```

### Select

```go
primes := [6]int{2, 3, 5, 7, 11, 13}

var s []int = primes[1:4] // selected [3 5 7]

s := []int{2, 3, 5, 7, 11, 13}

// Slice the slice to give it zero length.
s = s[:0]
printSlice(s)

// Extend its length.
s = s[:4]
printSlice(s)

// Drop its first two values.
s = s[2:]
printSlice(s)
```

### Length and capacity of a slice

```go
s := []int{2, 3, 5, 7, 11, 13}
fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
```

