## Cpp面试

> http://blog.providencezhang.cn/2019/02/18/lang-notebook/

decltype:有时我们希望从表达式的类型推断出要定义的变量类型，但是不想用该表达式的值初始化变量（初始化可以用auto）。为了满足这一需求，C++11新标准引入了decltype类型说明符，它的作用是选择并返回操作数的数据类型，在此过程中，编译器分析表达式并得到它的类型，却不实际计算表达式的值。

```c
int getSize();
int main(void)
{
    int tempA = 2;
    
    /*1.dclTempA为int.*/
    decltype(tempA) dclTempA;
    /*2.dclTempB为int，对于getSize根本没有定义，但是程序依旧正常，因为decltype只做分析，并不调用getSize().*/
    decltype(getSize()) dclTempB;
​
    return 0;
}
```

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

## Customize Hashing for your class

```c
#include <iostream>
#include <iomanip>
#include <functional>
#include <string>
#include <unordered_set>
 
struct S {
    std::string first_name;
    std::string last_name;
};
bool operator==(const S& lhs, const S& rhs) {
    return lhs.first_name == rhs.first_name && lhs.last_name == rhs.last_name;
}
 
// custom hash can be a standalone function object:
struct MyHash
{
    std::size_t operator()(S const& s) const noexcept
    {
        std::size_t h1 = std::hash<std::string>{}(s.first_name);
        std::size_t h2 = std::hash<std::string>{}(s.last_name);
        return h1 ^ (h2 << 1); // or use boost::hash_combine (see Discussion)
    }
};
 
// custom specialization of std::hash can be injected in namespace std
namespace std
{
    template<> struct hash<S>
    {
        std::size_t operator()(S const& s) const noexcept
        {
            std::size_t h1 = std::hash<std::string>{}(s.first_name);
            std::size_t h2 = std::hash<std::string>{}(s.last_name);
            return h1 ^ (h2 << 1); // or use boost::hash_combine
        }
    };
}
 
int main()
{
 
    std::string str = "Meet the new boss...";
    std::size_t str_hash = std::hash<std::string>{}(str);
    std::cout << "hash(" << std::quoted(str) << ") = " << str_hash << '\n';
 
    S obj = { "Hubert", "Farnsworth"};
    // using the standalone function object
    std::cout << "hash(" << std::quoted(obj.first_name) << ',' 
               << std::quoted(obj.last_name) << ") = "
               << MyHash{}(obj) << " (using MyHash)\n                           or "
               << std::hash<S>{}(obj) << " (using injected std::hash<S> specialization)\n";
 
    // custom hash makes it possible to use custom types in unordered containers
    // The example will use the injected std::hash<S> specialization above,
    // to use MyHash instead, pass it as a second template argument
    std::unordered_set<S> names = {obj, {"Bender", "Rodriguez"}, {"Turanga", "Leela"} };
    for(auto& s: names)
        std::cout << std::quoted(s.first_name) << ' ' << std::quoted(s.last_name) << '\n';
}
```

hash("Meet the new boss...") = 1861821886482076440
hash("Hubert","Farnsworth") = 17622465712001802105 (using MyHash)
                           or 17622465712001802105 (using injected std::hash<S> specialization) 
"Turanga" "Leela"
"Bender" "Rodriguez"
"Hubert" "Farnsworth"