# Smart Pointer

> https://www.educative.io/edpresso/what-are-smart-pointers

## Definition

Smart pointers are just classes that wrap the raw pointer and overload the -> and * operators; this allows them to offer the same syntax as a raw pointer.

C++11 has three types of smart pointers that are defined in the `<memory>` header of the Standard Library. They are:

- `std::unique_ptr`: only itself can reference it, if you want to copy, call `std::move(ptr)`
- `std::shared_ptr`: allow multiple references, keep track of the reference with **reference counting**, when the count == 0, the object is destroyed. Using `ptr.std::reset()` to destroy one reference to the ptr pointer.
- `std::weak_ptr`: std::weak_ptr models temporary ownership: when an object needs to be accessed only if it exists, and it may be deleted at any time by someone else, std::weak_ptr is used to track the object, and it is converted to std::shared_ptr to assume temporary ownership. If the original std::shared_ptr is destroyed at this time, the object's lifetime is extended until the temporary std::shared_ptr is destroyed as well.

> Another use for std::weak_ptr is to break reference cycles formed by objects managed by std::shared_ptr. If such cycle is orphaned (i,e. there are no outside shared pointers into the cycle), the shared_ptr reference counts cannot reach zero and the memory is leaked. To prevent this, one of the pointers in the cycle can be made weak. [cppreference.com](https://en.cppreference.com/w/cpp/memory/weak_ptr)

