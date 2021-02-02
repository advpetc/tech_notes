# Struct

## Anonymous Struct

```go
monica := struct {
		firstName, lastName string
		salary              int
		fullTime            bool
	}{
		firstName: "Monica",
		lastName:  "Geller",
		salary:    1200,
	}
	
	fmt.Println(monica)
```

## Anonymous Field

```go
type Data struct {
	test string
	int
	bool
}

func main() {
	sample1 := Data{"Monday", 1200, true}
	sample1.bool = false
	
	fmt.Println(sample1.test, sample1.int, sample1.bool) // note that sample1.string will raise error
}
```

## [Tag](https://medium.com/golangspec/tags-in-golang-3e5db0b8ef3e)

Tags are formatted as concatenation of `key:"value"` pairs.

(Un)marshaling;

```go
import (
    "encoding/json"
    "fmt"
)
func main() {
    type T struct {
       F1 int `json:"f_1"`
       F2 int `json:"f_2,omitempty"`
       F3 int `json:"f_3,omitempty"`
       F4 int `json:"-"`
    }
    t := T{1, 0, 2, 3}
    b, err := json.Marshal(t)
    if err != nil {
        panic(err)
    }
    fmt.Printf("%s\n", b) // {"f_1":1,"f_3":2}
}
```