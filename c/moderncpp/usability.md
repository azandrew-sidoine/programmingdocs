# Modern Cpp (Language usability enhancement)

- Constants

-- `nullptr`

**Note**
C++ `does not allow` to implicitly convert `void *` to other types.
The type of `nullptr` is `nullptr_t`, which can be implicitly converted to any pointer or member pointer type, and can be compared equally or unequally with them.

**Warning**
`NULL` is different from `0` or `nullptr` therefore developpers must develop the habit of using `nullptr` when wrting C++ codes.

-- `constexpr`

`constexpr` helps compilers to optimize or make c++ codes more performant by computing the result of expression before runtime.

**Note**
`constexpr` compiles expressions or functions into constant results at compile-time.

**Note**
In C++, the length of an array must be a constant expression. `const` does not creates constant expression, only `constexpr` creates a constrant expression.

```cpp

#define LEN 10

constexpr int fibonacci(const int n) {
    return n == 1 || n == 2 ? 1 : fibonacci(n - 1) + fibonacci(n -2);
}

int main() {

    int list_1[10]; // Legal
    int list_2[LEN]; // Legal

    int l = 10;
    int list_3[l]; // Illegal

    const int l_2 = len + 1;
    int list_4[l_2]; // Illegal but ok for most compilers

    constexpr int l_constexpr = 1 + 2 + 4;
    int list_4[l_constexpt]; // Legal

    char arr_6[fibonacci(2)]; // legal
}
```

**Note**
C++11 provides `constexpr` to let the user explicitly declare that the function or object constructor will become a constant expression at compile time. It tells the compiler to check if an expression is constant at `compile-time`.

- Variables & Initializations

Variables can now be directly initialized in if and switch conditional block just like `for...loop`.

> if (std::vector<int>::iterator itr = std::find(v.begin() , v.end(), <VALUE>)) -> Just like in PHP.

**Note** Such variables exists only in the scope of `if`, `switch` or for block.

```cpp
#include <vector>
#include <algorithm>

int main() {

    std::vector<int> v = {1, 2, 3, 4};

    // Traditional C++
    std::vector<int>::iterator itr = std::find(v.begin(), v.end(), 2); // Creates a vector iterator
    // Fron C++17, can be converted to auto syntax
    auto itr = std::find(v.begin(), v.end(), 3);

    if (itr != v.end()) {
        *itr = 3;
    }

    // Moder C++
    if (const std::vector<int>::iterator itr = std::find(v.begin(), v.end(), 3); itr != v.end()) {
        *itr = 4;
    }

    // In for loop
    // Can be changed to auto from C++17
    for (std::vector<int>::iterator element = v.begin(), element != v.end(), element++) {
        // Print the element of the std::vector type
    }
}
```

- Initializers list

Uniform initialization allow C++ objects to be initilized as container object, array of primitive type

```cpp
#include <iostream>
#include <string>

class Point {

    private:
        double _x, _y = 0;

    public:
        Point(): _x(0), _y(0) {}

        Point(double x, double y): _x(x), _y(y) {}

        double getX() const {
            return _x;
        }

        double getY() const {
            return _y;
        }
};

int main() {

    // All instance are uniformly initialized
    Point p{0, 2};
    std::string str{"Hello World!"};
    int x{19};

    std::cout << "X: " << p.getX() << " Y: " << p.getY() << std::endl;
    std::cout << "String: " << str << std::endl;
    std::cout << "Number: " << x << std::endl;

    return 0;
}
```

```cpp
#include <initializer_list>
#include <vector>
#include <iostream>

class MagicFoo {
    public:
    std::vector<int> v;

    MagicFoo(std::initializer_list<int> list) {
        for (std::initializer_list<int>::iterator it = list.begin(); it != list.end(); ++it)
            v.push_back(*it);
    }
};
```

- Structured binding `std::make_tuple<T1, T2, ... Tn>()` & `std::tuple<T,T2,T3,...Tn>`

Structured bindings provide functionality similar to the multiple return values provided in other languages. It allows C++ programmers to return types like tuples, etc...

**Note**
From C++17, unpacking and manipulating tuples, returned values is make easier to work with. Prior, to `C++17` such manipulations required complex operations.

```cpp
#include <iostream>
#include <tuple>

std::tuple<int, double, std::string> f() {
    return std::make_tuple(1, 2.3, "456");
}
int main() {
    auto [x, y, z] = f();
    std::cout << x << ", " << y << ", " << z << std::endl; return 0;
}
```

## Type inference

C++11 introduced `auto` and `decltype` (type derivation implementation) letting the compiler worry about type of variables.

- auto
  auto has been in C++ for a long time, but it always exists as an indicator of a storage type, coexisting with register. In traditional C++, if a variable is not declared as a register variable, it is automatically treated as an auto variable. And with register being deprecated (used as a reserved keyword in C++17 and later used, it doesn’t currently make sense), the semantic change to auto is very natural.

```cpp
int main() {
    // Before C++11
    // cbegin() returns vector<int>::const_iterator
    for(vector<int>::const_iterator it = vec.cbegin(); it != vec.cend(); ++it) {

    }

    // From C++11
    for (auto it = v.cbegin(); it != v.cend(); ++it) {
        // it -> pointer to values in the vector container
        // Simplify how to work with container algorithms
    }

    auto i = 10; // Infer type as integer

    auto int_array = new auto(10); // As array of int *
}
```

**Note**
Use auto with cares as it can end up making the code less readable.

**Note**
auto cannot be used to derive array types yet:

```cpp
auto auto_arr2[10] = {arr}; // illegal, can't infer array type
```

- decltype

The decltype keyword is used to solve the defect that the `auto` keyword can only type the variable. Its usage is very similar to `typeof`. `decltype` allow developpers to query for typeof an expression. It's mainly used to infer the typeof an expression, or a variable or a function.

> decltype<<EXPRESSION\_>>

```cpp
#include <type_traits>

int main() {
    auto x = 10;
    auto y = 3;

    decltype<x+y> z;
}
```

- Tail `type inference`

```cpp
template<typename R, typename T, typename U> R add(T x, U y) {
    return x+y;
}

// Using decltype
template<typename T1, typename T2>
decltype<x + y> add(T1 x, T2 y) { // Will not compile
    // Perform add operation
}

// To defines function return type, C++11 introduced a tail inference type wich uses auto to post the return type
template<typename T1, typename T2>
auto add(T1 x, T2 y) -> decltype<x + y> {
    // Performs add operation
}

// From C++14
// From c++14 there is no need for the trailing return type declaration
template<typename T1, typename T2>
auto add(T1 x, T2 y) {
    // Performs add operation
}
```

- decltype(auto)

In simple terms, `decltype(auto)` is mainly used to derive the return type of a forwarding function or package, which does not require us to explicitly specify the parameter expression of `decltype`. Consider the following example, when we need to wrap the following two functions

```cpp
std::string  lookup1();
std::string& lookup2();

std::string look_up_a_string_1() {
    return lookup1();
}

std::string& look_up_a_string_2() {
    return lookup2();
}

// C++11 compatible
// Compiler set the return type to return type of lookup1() function call
decltype(auto) look_up_a_string_1() {
    return lookup1();
}

// Compiler set the return type to return type of lookup2() function call
decltype(auto) look_up_a_string_2() {
    return lookup2();
}
```

## Control flow

- `if constexpr` `C++17`

```cpp
#include <iostream>

template <typename T>
auto print_type_info(const T& t) {
    if constexpr (std::is_integral<T>::value) { // Value is integer value
        return t + 1;
    } else {
        return t + 0.001;
    }
}
// Get compiled to
int print_type_info(const int& t) {
    return t + 1;
}
int print_type_info(const double& t) {
    return t + 0.001;
}

int main() {
    std::cout << print_type_info(5) << std::endl;
}
```

- Range based for loop

From C++ we can write for loops that are concise like Python for loops:

```cpp

int main() {

    std::vector<int> v = {1, 2, 3, 4, 5, 6};

    // Pre C++11
    for (std::vector<int>::iterator it = v.begin(); i != v.end(); ++it) {
        // ...
    }

    // From C++11
    for (auto element : v)
        // element is readonly

    // using reference iterator make the element at writable
    for (auto element& : v) {
        // element is writable
    }
}
```

## Templates `Black magic of C++`

`C++ templates` have always been a `special art of the language`, and templates can even be used `independently as a new language`.
The philosophy of the template is to `throw all the problems` that can be processed at `compile time` into the compile time, and only deal with those core dynamic services at runtime, to greatly optimize the performance of the runtime.

- Extern Templates

`In traditional C++`, templates are `instantiated by the compiler only when they are used`. In other words, as long as a fully defined template is encountered in the code compiled in each `compilation unit (file)`, it will be instantiated. This results in an `increase in compile time due to repeated instantiations`. Also, we have no way to tell the compiler not to trigger the instantiation of the template.

To this end, `C++11` introduces `an external template` that extends the syntax of the original manda-tory compiler to `instantiate a template at a specific location`, allowing us to explicitly tell the compiler when to instantiate the template:

```cpp
template class std::vector<bool>; // force instantiation

extern template class std::vector<double>; // should not instantiate template in current file
```

- The ">"

From C++11, `>>` is treated as template not `right shift` operator when encontered in template syntax.

```cpp
std::vector<std::vector<int>> matrix; // This is perfectly valid syntax
```

- Type alias templates

**Note**
C++ templates are used to generated types. Because templates are not actual types:

```cpp
template<typename T, typename K>
class MyClass {

    private:
        T dark;
        K key;
}

template<typename T>
typedef MyClass<std::vector<T>, std::string> FakeClass; // Is illegal

// To create a type alias for templates, C++11 introduced the using on types

template<typename T>
using FakeClass =  MyClass<std::vector<T>, std::string>; // Legal

// Using can also be used on other concrete type definitions
using Process = int(*)(void *); // typedef int (*process)(void*) -> Function pointer
// Not that the using syntax just remove the pointer naming required by exisiting codes

int main() {
    Process myProcess; // Provide initialization
}
```

- Variadic templates
  `In traditional C++,` both a class template and a function `template could only accept a fixed set of template parameters` as specified.

From C++11, variadic list of template typename can be specified:

```cpp
template<typename... Ts> class MyClass;
```

**Note**
Since it is arbitrary, a template parameter with a number of 0 is also possible:

```cpp
class MyClass<> nothing;
```

or to force at least a certain number of parameters:

```cpp
template<typename TRequired, typename TRequired2, typename... Ts> class MyClass;
```

```cpp
// An example
template<typename... Args> void printf(const std::string &str, Args... args);

//
template<typename... Ts>
void template_func(Ts... args) {
    std::cout << sizeof(args) << std::endl; // Returns the number of argument passed to the function
}
```

- sizeof...

`sizeof...` operator allow template function to query for a number of arguments passed to a template function.

```cpp
#include <iostream>

template <typename... T>
void my_func(T... args) {
    std::cout << "Total number of arguments: " << sizeof...(args) << std::endl;
}

int main() {

    my_func(2, 4, "Hello World!");
}
```

- Recursive template function
  Using template with overloading techniques, we can recursively loop through each argument of a template function:

```cpp

template<typename T0>
void print(T0 value) {
    std::cout << value << std::endl;
}

template<typename T0, typename... T>
void print(T0 value, T... args) {
    std::cout << value << std::endl;
    if constexpr (sizeof...(t) > 0) {
        print(args...);
    }
}
```

- Fold Expression `C++17`

In C++ 17, this feature of the variable length parameter is further brought to the expression, consider the following example:

```cpp
#include <iostream>

template<typename ...T>
auto sum(T ... t) {
    return (t + ...); // Returns the computed reduce function of the sum of integers
}

int main() {
    std::cout << sum(1,2,3,4,5,6,7) << std::endl;
}
```

- Non-Type template parameters

**Note**
The allow developper to pass value as template parameter instead of simply classes.

The example below shows a template class that allows different litteral to be template parameters, i.e non-type template parameters:

```cpp
template<typename T, int size>
class buffer_t {
    public:
        T& alloc();
        void free(T& item);

    private:
        T data[size];
}

buffer_t<int, 100> buf; // 100 as template parameter
```

C++17 introduces this feature, and we can indeed use the auto keyword to let the compiler assist in the completion of specific types of derivation:

```cpp
template<typename T, auto size>
class buffer_t {
    public:
        T& alloc();
        void free(T& item);

    private:
        T data[size];
}

template<auto value>
void foo() {
    std::cout << value << std::endl;
}

int main() {
    buffer_t<int, 100> buf; // Infered buffer size to int

    //
    foo<10>(); // Value as int
}
```

## Object oriented

- Delegate constructor

C++11 introduces the concept of a delegate construct, which allows a constructor to call another constructor in a constructor in the same class, thus simplifying the code:

```cpp
class Base {
    private:
        unin16_t _value;
        unin16_t _value2;

    public:
        Base(): _value1(1) { }
        Base(int value): Base() { _value2 = value; } // Delegate base constructor
}
```

- Ihneritance contructor

`In traditional C++`, constructors need to pass arguments one by one if they need inheritance, which leads to inefficiency. `C++11 introduces the concept of inheritance constructors using the keyword using`:

```c++
class Base {
    private:
        unit16_t _value, _value2;

    public:
        Base(): _value(1) { }
        Base(int value): Base() { _value2 = value; } // Delegate base constructor
};

class Subclass : public Base {
    public:
        using Base::Base; // Inheritance base constructor
}
```

- Explicit virtual function

In traditional C++, it is often prone to accidentally overloading virtual functions:

```c++
// Base class
struct Base {
    virtual void foo();
};

// Subclass : inheritance
struct SubClass: Base {
    void foo();
};
```

-- override
When overriding a virtual function, introducing the override keyword will explicitly tell the com- piler to overload, and the compiler will check if the base function has such a virtual function, otherwise it will not compile.

**Warning**
override keyword forces the presence of the overriden method on the base class, else a compile time error is generated.

```c++
// Base class
struct Base {
    virtual void foo(int);
};

// Subclass : inheritance
struct SubClass: Base {
    virtual void foo(int) override; // legal
    virtual void foo(int) override; // illegal, no virtual function in base class
};
```

-- final
final is to prevent the class from being continued to inherit and to terminate the virtual function to continue to be overloaded.

```c++
// Base class
struct Base {
    virtual void foo(int) final;
};

// Subclass : inheritance
struct SubClass final: Base {
}; // legal

struct Subclass2 : SubClass { // Illegal

}

// Subclass : inheritance
struct SubClass: Base {
    virtual void foo(int) final; // Illigal foo() is final in base class
}; // legal
```

-- Explicit `delete` & `default` function

**Note**
`In traditional C++`, if the programmer does not provide it, the compiler will default to generating default `constructors, copy constructs, assignment operators, and destructors` for the object. Besides, C++ also defines operators such as new delete for all classes. This part of the function can be overridden when the programmer needs it.

**UseCase**
Also, the default constructor generated by the compiler cannot exist at the same time as the user- defined constructor. If the user defines any constructor, the compiler will no longer generate the default constructor, but sometimes we want to have both constructors at the same time, which is awkward:

C++11 provides a solution to the above requirements, allowing explicit declarations to take or reject functions that come with the compiler:

```c++
class Magic { 
    public:
        Magic() = default; // explicit let compiler use default constructor
        Magic& operator=(const Magic&) = delete; // explicit declare refuse constructor 
        Magic(int magic_number); // Parameter constructor
}
```

- Strongly typed enumerations

In traditional C++, enumerated types are not type-safe, and enumerated types are treated as integers, which allows two completely different enumerated types to be directly compared (although the compiler gives the check, but not all).

C++11 introduces an enumeration class and declares it using the syntax of enum class:

```c++
enum class my_enum: unsigned int {
    value1,
    value2,
    value3 = 100,
    value4 = 100
}
// This enumeration is type safe

if (my_enum::value3 == my_enum::value4) { // True

}

// Overriding << opertor on the enumeration type
#include <iostream>

template<typename T>
std::ostream& operator<< (typename std::enable_if<std::is_enum<T>::value, std::ostream>::type& stream, const T& e ) {
    return stream << std::static_cast<typename std::underlying_type<T>::type>(e);
}
```
