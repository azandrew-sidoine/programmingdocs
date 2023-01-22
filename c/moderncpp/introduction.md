# Modern C++ (Introduction)

## Type comparison `std::is_same` <type_traits>

> C++ provides a `decltype`, from <type_traits> namesapce, which is used to return the type derivation of a given value/variable.
> std::is_same<Type1, Type2> -> Compare equality of 2 different types.

```cpp
#include <type_traits>

int main() {

    // Compares the declared type of NULL and 0
    if (std::is_same<decltype(NULL), decltype<0>>::value) {

    }
    if (std::is_same<decltype(NULL), decltype<std::nullptr_t>>::value) {

    }
}
```

## Deprecation

- String literal const is no longuer allowed to be assigned to a char \* pointer.

```cpp
main() {
    char *char_ptr = "Hello World!"  // [Deprecated]
    const char* char_ptr = "Hello World!"; // Ok
    // Automatically infer the string character type
    auto char_ptr = "Hello World!"; // Ok
}
```

- C++98 exception description, unexpected_handler, set_unexpected() and other handlers are deprecated. Use `noexcept` expression instead.

- Replace `auto_ptr` with `unique_ptr`

- `register` is deprecated, because does no longer have any pratical meaning.

- ++ on `bool` is deprecated

- If class has `destructor`, properties for which it generates copy constructor and copy assignment is deprecated.

- Deprecated c-style casting a.k.a `(Type)variable` is deperecated. Use `std::cast<Type>(...)`, `std::reinterpret_cast<Type>(...)` or `std::const_cast<Type>()` instead.

- From C++17, <ccomplex>, <cstdalign>, <cstdbool>, <ctgmatch>, etc are deprecated.

**Note**
For modern C++, `C++ is no more a superset of C` should be in mind of any C++ developper. For compatibility reason, always put `C` related codes
into a separate file header file and export any construct using `extern "C"` directive like below:

```c
// foo.h
#ifdef __cplusplus
extern "C" {
    #endif
    int add(int x, int y);
    #ifdef __cplusplus
}
#endif

// foo.c
int add(int x, int y)
{
    return x + y;
}

// main.cpp
#include "foo.h"
#include <iostream>
#include <functional>

using namespace std;

int main() {
    [out = std::ref(std::cout << "Result from C code: " << add(1, 2))](){
        out.get() << "\n;
    }();
    return 0
}
```

To compile the source code using make file:

```makefile
C = gcc # Binary variable to compile c codes, use the GCC compiler
CPP = clang++ # Binary variable to compile C++ code, use the clang++ compiler
SOURCE_C = foo.c # Main source code

OBJECTS_C = foo.o # Link the c code headers
SOURCE_CPP = 1.1.cpp # C++ Main input file
TARGET = 1.1 # Unknown
LDFLAGS_COMMON = -std=c++2a # Compiler flags and options

# Compiler execution flags
all:
    $(C)-c $(SOURCE_C)
    $(CPP) $(SOURCE_CPP) $(OBJECTS_C) $(LDFLAGS_COMMON) -o $(TARGET)
clean:
    rm -rf *.o $(TARGET)
```
