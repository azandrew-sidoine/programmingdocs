# Modern C++ (Smart Pointers) `<memory>`

## RAII (Resource Acquisition is Initalization) & Reference Counting

- Ref counting

**Note**
The basic idea is to count the number of dynamically allocated objects. Whenever you add a reference to the same object, the reference count of the referenced object is incremented once. Each time a reference is deleted, the reference count is decremented by one. When the reference count of an object is reduced to zero, the pointed heap memory is automatically deleted.

**Note**
Reference counting is not garbage collection.

They simulate basic data type pointer and offer automatic object destruction using desructor, or object methods.

## Pros

- Provides automatic memory management.
- Smart pointers often prevent memory leaks making memory deallocation automatic
- Prevents dangling pointers by waiting to destroy and object until it's no longer in used.

## Implementation

They are implemented as templated class introduced in C++11

- unique_ptr `std::unique<T>()` [`Perfect for data that must not be shared`]

It's a container for C raw pointer. It will destroy the internal referenced attribute when it goes out of scope. It's a smart pointer that prohibit other pointers to shared the internal object reference keeping code safe. To move the reference we use `std::move()`

**Note**
To create a unique pointer from C++14, we use `std::make_unique<T>()` while in C++11, use provide our own implementation:

```cpp
#include <memory>
#include <utility>

// Pre C++11
template <typename T, typename ... TArgs>
std::unique_ptr<T> make_unique(TArgs&& ... args)
{
    return std::unique_ptr<T>(new T( std::forward<TArgs>(args)... ));
}

// From C++ 14
std::unique_ptr<int> ptr = std::make_unique<int>(10);

// Pre C++11
std::unique_ptr<int> ptr = make_unique<int>(10);

// Moving the unique pointer
// Before moving we need to check if the pointer is not null
if (ptr)
    auto ptr2 = std::move(ptr);
```

--- Cons
unique pointers cannot be copied. They can only be moved arround.

--- std::move
It's used to tranfer ownership to another object of type `std::unique_ptr`

- shared_ptr `std::make_shared<T>()` [`Perfect to manage lifetime of a shared data`]

It's also a container for a raw pointer that maintains a reference count ownerrship (count of all `std::shared_ptr` that refer to the internal object). The internal object is destroyed when all copies of the `std::shared_ptr` have been destroyed.

```cpp
#include <memory>

int main()
{
    auto ptr = std::make_shared<int>(10);

    // Accessing the value of the shared pointer
    std::cout << *ptr << std::endl;

    // The shared pointer will be destructed before leving the scope

    int *p = ptr.get(); // Returns the raw pointer reference // Does not increment the ref count

    // creates or increment the reference count
    auto ptr2 = ptr; // Increment the ref count +1 

    ptr.reset(); // Decrement the ref count = Ref count == 1

    // Get the reference count
    std::cout << "Ref count: " << ptr.use_count() << std::endl;
    return 0;
}
```

- weak_ptr `std::make_weak<T>()` [``]

It's a container of `C` raw pointer, created from a `shared_ptr`. When a weak pointer is created or destroyed, it has no effect on referenced shared pointer. After all copies of a `shared_pointer` are destroyed, the weak pointer becomes a nullptr that can be garbage collected.

It's a weak reference to a shared memory.

**Note**
Weak pointers cannot be dereferenced. They can only be converted to shared pointers (and must always check if a weak pointer does not point to nullptr before using it).

**Note**
Make use of `std::weak_ptr` when twoo or more object point to themselves.

> `std::weak_ptr::expired()` -> Returns false if the resource is not yet released.
> `std::weak_ptr::lock()` -> Returns a std::shared_ptr to the original object when the resource is not released, or `nullptr` otherwise.
