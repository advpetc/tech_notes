# Learning notes from [geektutu](https://geektutu.com/post/quick-golang.html)

## Array and Slice

Array:

```go
var arr [5]int // declare 1-d array
var arr [5][5]int // declare 2-d array
var arr = [5]int{1, 2, 3, 4, 5}
var arr = [...]int{1,2,3,4} // compiler will count the array elements for you
```

Slice:

Slice is just a pointer that is pointing to the underlying array

```go
var slice = []int{1, 2, 3} // note that there is nothing inside the []
```

Can also use `make` to declare a slice:

```go
slice := make([]int, 4, 5) // with size of 4 and capacity of 5
slice := make([]int, 4) // with size of 4 and capacity equals to size (4)
```

Appending two slices:

```go
append([]int{1,2}, []int{3,4}...) // don't forget the ... at the end
```

## Map

Declare a map:

```go
m1 = make(map[string]int)
```

## Enum

There is no `enum` in Go, but it uses `const` to represent:

```go
type Gender int8
const (
	MALE   Gender = 1 // variable name, type, assigned value
	FEMALE Gender = 2
)

gender := MALE

switch gender {
case FEMALE:
	fmt.Println("female")
case MALE:
	fmt.Println("male")
default:
	fmt.Println("unknown")
}
// male
```

## Defer and recover

Use `defer` and `recover` when as `try` and `catch`:

```go
func get(index int) (ret int) {
	defer func() {
		if r := recover(); r != nil { // it will be called after the panic occurs
			fmt.Println("Some error happened!", r)
			ret = -1
		}
	}()
	arr := [3]int{2, 3, 4}
	return arr[index]
}

func main() {
	fmt.Println(get(5))
	fmt.Println("finished")
}
```

## Struct

Use **method** to call struct instance:

```go
type Student struct {
	name string
	age  int
}

func (stu *Student) hello(person string) string {
	return fmt.Sprintf("hello %s, I am %s", person, stu.name)
}

func main() {
	stu := &Student{
		name: "Tom",
	}
  // this will also work, now studnet 
  stu := Student{
    name: "Tom", 
  }
	msg := stu.hello("Jack")
	fmt.Println(msg) // hello Jack, I am Tom
}
```

In Go, a function can return the reference of a local variable:

```go
func myFunction() (*MyStructType, error) {
    var chunk *MyStructType = new(HeaderChunk)

    ...

    return chunk, nil
}


func myFunction() (*MyStructType, error) {
    var chunk MyStructType

    ...

    return &chunk, nil // this will work
}
```

Quoted from Golang:

**How do I know whether a variable is allocated on the heap or the stack?**

From a correctness standpoint, you don't need to know. Each variable in Go exists as long as there are references to it. The storage location chosen by the implementation is irrelevant to the semantics of the language.

The storage location does have an effect on writing efficient programs. When possible, the Go compilers will allocate variables that are local to a function in that function's stack frame. However, if the compiler cannot prove that the variable is not referenced after the function returns, then the compiler must allocate the variable on the garbage-collected heap to avoid dangling pointer errors. Also, if a local variable is very large, it might make more sense to store it on the heap rather than the stack.

In the current compilers, if a variable has its address taken, that variable is a candidate for allocation on the heap. However, a basic escape analysis recognizes some cases when such variables will not live past the return from the function and can reside on the stack.

## Package

If function/interface/type/method/statement is capitalized, then these will be accessible from other files in the other package(s). If not capitalized, then it will not be accessible.

## Trick

Use empty interface to represent any type:

```go
func main() {
	m := make(map[string]interface{})
	m["name"] = "Tom"
	m["age"] = 18
	m["scores"] = [3]int{98, 99, 85}
	fmt.Println(m) // map[age:18 name:Tom scores:[98 99 85]]
}
```

