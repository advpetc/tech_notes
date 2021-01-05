# Notes for reading *Caleb Doxsey - Introducing Go_ Build Reliable, Scalable Programs*

## `defer`, `panic`, and `recover` keywords

> [url](https://blog.golang.org/defer-panic-and-recover)

Some advantages for using `defer`:

* It keeps our Close call near our Open call so it’s easier to understand.
*  If our function had multiple return statements (perhaps one in an if and one in an else), Close will happen **before** both of them.
* Deferred functions are run even if a runtime panic occurs.

```go
func CopyFile(dstName, srcName string) (written int64, err error) {
    src, err := os.Open(srcName)
    if err != nil {
        return
    }

    dst, err := os.Create(dstName)
    if err != nil {
        return
    }

    written, err = io.Copy(dst, src)
    dst.Close()
    src.Close()
    return
}
```

If the call to os.Create fails, the function will return without closing the source file. This can be easily remedied by putting a call to src.Close before the second return statement, but if the function were more complex the problem might not be so easily noticed and resolved. By introducing defer statements we can ensure that the files are always closed:

```go
func CopyFile(dstName, srcName string) (written int64, err error) {
    src, err := os.Open(srcName)
    if err != nil {
        return
    }
    defer src.Close() // this will be called before line 4 if err != nil

    dst, err := os.Create(dstName)
    if err != nil {
        return
    }
    defer dst.Close() // this will be called before line 10 if err != nil

    return io.Copy(dst, src)
}
```



However, there are some pitfalls:

```go
func a() {
    i := 0
    defer fmt.Println(i)
    i++
    return
}
```

Instead of printing 1, it will print 0, although the `fmt.Println(i)` is being called after i++. `defer` will save the current state of the function — including local variable — to run before the very last line of the function.

```go
func b() {
    for i := 0; i < 4; i++ {
        defer fmt.Print(i)
    }
}
```

If there are multiple `defer`, the final order will be called as LIFO or like a stack: 0 defer first, so it's at the bottom of the stack, 1 second, so second place of the stack, etc. The final output will be 3 -> 2 -> 1 -> 0



It's a bit hard to understand, [stackoverflow](https://stackoverflow.com/questions/37248898/how-does-defer-and-named-return-value-work):

> 3. Deferred functions may read and assign to the returning function's named return values.

You can specify the return value and its type in the function signacture:

```go
func a() (i int) { // return 2 since it return nothing
    i = 2
    return
}

func b() (i int) {  // return 1 since it "override" what should be returned
    i = 2
    return 1
}
```

So

```go
 func c() (i int) {
    defer func() { i++ }()
    return 1
}
```

This deferred `func()` just specify the return value and type, and it got executed after 1 is returned 

## Receiver

```go
// instead of using &c to pass as reference to the function
func circleArea(c *Circle) float64 {
	return math.Pi * c.r * c.r
}
c := Circle{0, 0, 5}
fmt.Println(circleArea(&c))

// use receiver
func (c *Circle) area() float64 {
  return math.Pi * c.r * c.r
}

fmt.Println(c.area())
```

Has-a relationship with receiver

```go
type Person struct {
	Name string
}

type Android struct {
	// Person Person // this will work, but doesn't full utilize the has-a relationship
  Person 				// type, this is better, so that we can all a.Talk()
	Model  string
}
	
// has-a relationship using receiver
a := new(Android)
a.Person.Talk() // this will work
a.Talk()        // will work as well, since a person can talk, an android is a person, therefore an android can talk
```

## Interface

[url](https://gobyexample.com/interfaces)

To use interface, there is no specific keyword such as `extends` in Java or `implement` in C++, we just implement all the method.

```go
package main

import (
	"fmt"
	"math"
)

// interface
type Shape interface {
	area() float64
}

type MultiShape struct {
	shapes []Shape
}

// this two struct will implement Shape
type Circle struct {
	x, y, r float64
}

type Rectangle struct {
	x1, y1, x2, y2 float64
}

// aux functions
func distance(x1, y1, x2, y2 float64) float64 {
	a := x2 - x1
	b := y2 - y1
	return math.Sqrt(a*a + b*b)
}

func rectangleArea(x1, y1, x2, y2 float64) float64 {
	l := distance(x1, y1, x1, y2)
	w := distance(x1, y1, x2, y1)
	return l * w
}

// by implementinng the area() method (receiver), it will implement the Shape interface
func (c Circle) area() float64 {
	return math.Pi * c.r * c.r
}

// by implementinng the area() method (receiver), it will implement the Shape interface
func (r Rectangle) area() float64 {
	l := distance(r.x1, r.y1, r.x1, r.y2)
	w := distance(r.x1, r.y1, r.x2, r.y1)
	return l * w
}


func (m *MultiShape) area() float64 {
	var area float64
	for _, s := range m.shapes {
		area += s.area()
	}
	return area
}

func main() {
  multiShape := MultiShape{
    shapes: []Shape{
      Circle{0, 0, 5}, // in slice literal, cannot declare pointer
      Rectangle{0, 0, 10, 10},
    },
	}
	fmt.Println(multiShape.area())
}
```

In short, `Rectangle` and `Circle` both implement the `area()` method, so that they can all be categorized as `Shape` type.



Difference between method and function in Golang: method has a receiver, while function
doesn't have one. `func () a() float64 {}` vs `func a() float64 {}`

## Fast way to create an slice/array

```go
	fmt.Println(strings.Join([]string{"a", "b"}, "-"))
```

## Reuse variable

This will work:

```go
// err variable is reused
dir, err := os.Open(".")
if err != nil {
  return
}
defer dir.Close()
fileInfos, err := dir.Readdir(-1)
if err != nil {
  return
}
```

​	This will not work:

```go
// this will not work
err := 3
err := 4

a, b := 1, 2
a, b := 3, 2
```

and will throw

```
# command-line-arguments
./main.go:110:6: no new variables on left side of :=
```

## Read all the file recursively under specified directory

```go
import (
  "fmt"
	"os"
  "path/filepath"
)

func walkFolder() {
	filepath.Walk(".", func(path string, info os.FileInfo, err error) error {
		fmt.Println(path)
		return nil
	})
}
```

## Why use `go` keyword

[stackoverflow](https://stackoverflow.com/questions/26006856/why-use-the-go-keyword-when-calling-a-function)

In writing a go server: to see the difference in action, try connecting twice (at the same time) to your server. You will find that without the word go, you will not accept the second tcp connection until the first one is done.

## Use `flag` to parse input argument

```go
package main

import (
	"flag"
	"fmt"
	"math/rand"
)

func main() {
	// use -max flag, use "the max value" as the help message
	/* $ go run args.go -help will display:
	 *    Usage of /var/folders/84/zs57njyx4hx911_xchm8mp7c0000gn/T/go-build805909142/b001/exe/args:
	 *  -max int
	 *        the max value (default 6)
	 *	exit status 2
	 */
	maxp := flag.Int("max", 6, "the max value")
	flag.Parse()
	fmt.Println(Intn(*maxp))
}
```

## Import alias

```go
import m "golang-book/chapter8/math"
func main() {
  xs := []float64{1,2,3,4} avg := m.Average(xs)
}
```

Similar to Python's `import xyz as x`

