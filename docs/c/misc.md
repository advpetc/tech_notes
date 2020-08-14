## mod

```c
1024 % 10;// = 4
-1024 % 10; //-4
```

## inf

use 0x3f3f3f3f if there is a need to do addition
else use 0x7fffffff

## Tuple

```c
// packing/unpacking tuples
#include <iostream>     // std::cout
#include <tuple>        // std::tuple, std::make_tuple, std::tie

int main ()
{
  int myint;
  char mychar;

  std::tuple<int,float,char> mytuple;

  mytuple = std::make_tuple (10, 2.6, 'a');          // packing values into tuple

  std::tie (myint, std::ignore, mychar) = mytuple;   // unpacking tuple into variables

  std::cout << "myint contains: " << myint << '\n';
  std::cout << "mychar contains: " << mychar << '\n';

  return 0;
}
```

## Operator

&: left & right in compiler doesn't have fix order (either left to right or right to left)

>>: neg divide isn't right -> e.g. -3 / 2 = 101 >> 1 = 110 = -2 which is wrong

set kth bit to zero: x & ~(1 << k)