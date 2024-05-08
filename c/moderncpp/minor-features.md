# Modern C++ (Minor feature)

## long long int

Provides a memory model with at least 64bits.

## noexcept (C++ 11)

One of the big advantages of C++ over C is that C++ itself defines a complete set of exception handling mechanisms.

```cpp
may_throw(); // May throw any exception
void no_throw(): noexcept; // Cannot throw an exception
```

**Note**
If a function or method marked with `noexcept` throws, the compiler use `std::terminate()` to immediatly terminate the program.

- noexcept as function

Returns true if the expresion or function call throws, else it return false

```cpp
void no_throw() noexcept {
    return;
}

int main()
{
    std::cout << std::boolalpha << "no_throw() noexcept? " << noexcept(may_throw()) << std::endl;
}
```

- Litteral

`C++11` provides the original string literals, which can be decorated with `R` in front of a string, and the original string is wrapped in parentheses:

```cpp
#include <iostream>
#include <string>

int main()
{
    // No need to escape \ character
    std::string str = R"(C:\Path\To\File)";
    std::cout << str << std::endl;
    return 0;
}
```

## Memory Alignment

C++ 11 introduces two new keywords, `alignof` and `alignas`, to support control of memory alignment.

- alignof
The alignof keyword can get a platform-dependent value of type std::size_t to query the alignment of the platform.

- alignas
To reshape the alignment of a structure.
