# Advance C++ programming

## C++ classes

--- Const safe methods
They are methods that can be called in constant context of the  class object. If the method will not modify class member, declare it as const safe  function.

```cpp
#include <cstdio>

class Class1
{
    int  _i = 0;
    public:
        void setValue(const int&);
        int  getValue() const; // Const safe method
}

// class member function definitions
void Class1::setValue(const int& i)
{
    _i  = i;
}
int  Class1::getValue() const
{
    return _i;
}
```

--- Class Constructors and Destructors

C++ destructors are prefixed by [~] operator. Each classes in C++ has at least on default contructor and  destructor that are iternally defines and call when object goes out of scope.

--- Namespace

It's like packages in Java and namespaces in PHP. They help encapsulate codes.

```cpp
// drewlabs header files
namespace drewlabs
{
    // Type definitions
}
```

--- Self referencing pointer

[this] in the context of a class reference the object  on wich method is called.

```cpp

class Class1
{
    int _i;
    public:
        int getValue()
        {
            return _i;
        }

        int getValueOverloaded()
        {
            // The call the  getValue of the current object
            return this->getValue();
        }
}
```

--- Operator overloading

Non-member operator overloading must not be  defined in the class context and must has both left  hand side and right hand side object defines.

```cpp
RType operator + (const LhsType&  lhs, const RhsType&  rhs)
{
    // Operators definitionss
}
```

---  Conversion operator

Note: std::to_string(type), convert a value of a given type to string

```cpp

class MyClass
{

    operator std::string() const;
}

MyClass::operator std::string() const
{
    // What to do if Myclass is being converted to a string
}

// Overloading the << operator
std::ostream & operator << (std::ostream& output, const MyClass& rhs)
{
    return output << std::string(rhs);
    // std::string() will call the overloaded string operator
}
```

--  Unary ++ and -- decrement operators

```cpp
class Number
{
    int value = 0;

    public:
        Number& operator ++();
        Number operator ++(int); // post fix increment
        Number& operator --();
        Number operator --(int); // post fix decrement
}

Number& Number::operator ++()
{
    value += 1;
    return this;
}
Number Number::operator ++(int)
{
    Number tmp = *this;
    value += 1;
    return temp;
} // post fix increment
Number& Number::operator --()
{
    value -= 1;
    return this;
}
Number Number::operator --(int)
{
    Number tmp = *this;
    value -= 1;
    return temp;
} // post fix decrement
```

--- Allocating and Deallocating memory

```cpp

// Creating oject with new
Class1 obj = new Class1;

//  In case of an array
Class1 objs  = new Class1[SIZE];

// Deleting or Freeing up memory
delete obj;

// In case of an array
delete [] objs;
```

--- Functors

Object that operates like function by overloading function operators.

```php

class MyCallable
{
    int _by  = 1;
    public:
        MyCallable(const int&);

        // Closure
        double operator () (const double&) const;

}

MyCallable MyCallable(const int& multiplier) : _by(mutiplier) { }

double MyCallable::operator () (const double& value) const
{
    return value * _by;
}
```

--- Class inheritance

```cpp

// Syntax for inheritance definitions
Class BaseClass
{
    private:
        BaseClass() {} // Make the class not able to be  instanciate
    // Class defintion
}

Class SubClass : <AccessModifier> BaseClass
{
    // Class definition
}

class Animal
{
    private:
        char* _state = "";
        Animal() {}
    protected:
        Animal(const char& state) : _state(state) {}
    public:
        // Public member definitions
        const char& getState()
        {
            return _state;
        }
}

class Dog : public Animal
{
    char* _name;
    public:
    // parent constructor must always be  called before member initializers
        Dog(const char& name, const char&  state): Animal(state), _name(name) {}

        hasState()
        {
            // Calling parent member function and data members
            Animal::getState();
        }
}
```

--- Accessing base class

There is no super keyword in  C++, use class context call to call base class members:

> BaseClass::memberName()

---  Friendship

Not that much requires. should be use with great  conscience.

--- Multiple inheritance

C++ support multiple ihneritance as it does not provide interfaces.


```cpp
class BaseClass1
{
    protected:
        BaseClass1() {}
}


class BaseClass2
{
    protected:
        BaseClass2() {}
}

// Multiple inheritance
class DerivedClass: public BaseClass1, public BaseClass2
{
    public:
        DerivedClass(): BaseClass1(), BaseClass2() {}
}
```

--- Polymorphism

In  order to make a class method overloadable, prefix it with virtual. Therefore, must create a virtual destructor

```cpp
class BaseClass1
{
    protected:
        BaseClass1() {}

    public:
        virtual double getValue();
        virtual ~BaseClass1() {}
}


class BaseClass2
{
    protected:
        BaseClass2() {}
}

// Multiple inheritance
class DerivedClass: public BaseClass1, public BaseClass2
{
    public:
        DerivedClass(): BaseClass1(), BaseClass2() {}
        double getValue()
        {
            return _value;
        }
}
```

## Smart pointers

It's a class that use operator overloading to provide efficient memory management. It's a bare metal wrapper arrounnd C pointers.

--- Unique pointer

It's a king of pointer that can not be copy, it has only one copy  of the pointer.

Note: Unique pointer must always be passed by reference as they don't provide a copy mechanism.

```cpp
// ... replaces the list of arguments for demonstration purpose
std::unique_ptr<MyClass> variable(new MyClass(...));

// C++17
auto variable = std::make_unique<MyClass>(...);

// Resetting a unique pointer
// Reset the address to null, destroying it or setting it to a new object
variable.reset([new MyClass(...)]);

// moving pointer to a new object
var1.move(var2);

// Getting value of the unique pointer
var2->value();

// Release
variable.release();// Pointer is null, but object is  not destroyed
```

--- Shared Pointers

Works like Unique_Ptr but provide copy functionality.

```cpp
// ... replaces the list of arguments for demonstration purpose
// the deleter can be a class, a function pointer or a lambda expressions
std::shared_ptr<MyClass> var1(new MyClass(...), deleter);

// C++17
auto var1 = std::make_shared<MyClass>(...);

// Resetting a unique pointer
// Reset the address to null, destroying it or setting it to a new object
var1.reset([new MyClass(...)]);

// Copying pointer to a new object
auto var2  = var1;  // Calling object copy constructor

// Getting value of the shared pointer
var2->value();

// Release
// Garbage collector will automatically destroy the pointer when object goes out of scopes
```

--- Weak pointer

A specialize shared pointer that is not counted in the ref counnt of the shared pointers.
For pointers that does not affect the life time of the value it point to.

Note: Weak pointer are useful to prevent circular references, or when need to point to something that may or may not exists.

```cpp

// C++17
auto var1 = std::make_shared<MyClass>(...);

// creating a weak pointer
auto var2  = std::weak_ptr<MyClass>(var1);

// Getting value of the shared pointer
// First must lock the pointer with the lock method

void displayPtrValue(const std::weak_ptr<MyClass>& param) {
    // Weak pointer count
    size_t  count =  param.use_count();
    // calling lock return the shared pointer 
    if (auto sp = param.lock()) {
        // Get the value
        sp->value();
        // Get  the reference count
        sp->use_count();
    }
}

// Release
// Garbage collector will automatically destroy the pointer when object goes out of scopes
```

--- Choosing a smart pointer

By default use [shared_ptr]. If the  object to point to might not exists, use [weak_ptr]. Prefer usage of [unique_ptr] when the relationship is one-to-one.

## Move semantic

--- lvalue & rvalue

> lvalue  = rvalue

--- Std::move

C++ standard for performing move semanntic. It works onn object declared for working with rvalue reference type.

```cpp
// Requires <utility> header file
template <typename T>
void swap(T& a, T& b)
{
    // Move the value a point to into a temporary variable
    T _tmp(std::move(a));
    a = std::move(b);
    b = std::move(_tmp);
}
```

--- Move constructor

It one want to take advanntage of the move semantic utilities, one must add a move constructor the class definition.

When declaring a move constructor, always remember to add a nexcept keyword at the end to prevent compiler to stuck on on the object if it definition is not provided.

```cpp
class ClassName
{
    public:
        // Move constructor
        ClassName(ClassName &&) noexcept;
}
```

Note: If no move contructor is define, compiler will use the copy constructor a fallback.

```cpp
// Example of the rational class

class Rational
{
    int  _n  =  0; int _d = 0;
    static const int _bufsize = 120;
    mutable char* _buf = nullptr;

    public:
        Rational(): _n(0), _d(1) { reset(); }
        Rational(const int& n): _n(n), _d(1) {}
        Rational(const int& n, const int& d): _n(n), _d(d) {}
        Rational(const Rational& rhs) : _n(rhs.numerator()), _d(rhs.denominator()) {}

        // Adding move constructor
        Rational(Rational&&) noexcept;
        ~Rational();

        numerator() const
        {
            return _n;
        }
        denominator() const
        {
            return _d;
        }

        // pubblic methods
        void  reset();

        // Operators overloading defitions
        Rational&  operator = (const Rational&);
        Rational&  operator + (const Rational&) const;
        Rational&  operator - (const Rational&) const;
        Rational&  operator * (const Rational&) const;
        Rational&  operator / (const Rational&) const;
        operator std::string () const;
        std::string string() const;
        const char*  c_str() const;
}

Rational::~Rational()
{
    reset();
}

// pubblic methods
void  Rational::reset()
{
    _n = 0; _d = 1;
    if (_buf) {
        delete [] _buf;
    }
    _buf = nullptr;
}

// Operators overloading defitions
Rational&  Rational::operator = (const Rational& rhs)
{
    if (this != &rhs) {
        _n = rhs.numerator();
        _d = rhs.denominator();
    }
    return *this;
}
Rational&  Rational::operator + (const Rational& rhs) const
{
    return Rational((_n * rhs.denominator()) + (_d * rhs.numerator()), _d * rhs.denominator());
}
Rational&  Rational::operator - (const Rational&) const
{
    return Rational((_n * rhs.denominator()) - (_d * rhs.numerator()), _d * rhs.denominator());
}
Rational&  Rational::operator * (const Rational&) const
{
    return Rational(_n * rhs.numerator(), _d * rhs.denominator());
}
Rational&  Rational::operator / (const Rational&) const
{
    return Rational(_n * rhs.denominator(), _d * rhs.numerator());
}
Rational::operator std::string () const
{
    return string();
}
std::string Rational::string() const
{
    return std::string(c_str());
}
const char*  Rational::c_str() const
{
    if (!_buf) {
        _buf = new char[_bufsize]();
    }
    snprintf(_buf, _bufsize, "%d/%d", _n, _d);
    return _buf;
}

// Move constructor
Rational::Rational(Rational&& rhs) noexcept
{
    _n(std::move(rhs.numerator()));
    _d(std::move(rhs.denominator()));
    rhs.reset();
}
```

Note: std::move makes the sure to call the move constructor of the given object.

--- Move assignment operator

To create a move assignment operator, use the rvalue reference as parameter of the = operator.

```cpp
Rational&  operator = (Rational&&) noexcept;
```

--- Rule of five

If overriding copy constructor of a class, one will need to provide a destrutor, a move constructor and a copy and swap assignment operator as define in Rational class implementation.

## Lambda Expressions C++11

Lambda is an anonymous function while a closure is a block of statement inline.

Note: A lambda expression create a closure [When assigning or passing a lambda as param we create closure].

```cpp
class Ftitle
{
    char lastc;

    public:
        Ftitle() : lastc(0) {}
        char operator () (const char&); 
}

char Ftitle::operator () (const char& c)
{
    const char r = (lastc == '' || lastc == 0) ? toupper(c) : tolower(c);
    lastc = c;
    return r;
}

// In the main.cpp
#inlude <cstdio>
#inlude <algorithm>

int main()
{
    char lastc = 0;
    char s[] = "Big light in stay to appear in east";
    transform(s, s + strnlen(s, _maxlen), s, Ftitle());
    puts(s);

    // Using lambda instead of a class
    // [&lastc] is like use(&lastc) in php
    // But in c++ the [] is always required even if we are not passing anything
    // -> is a function return operator similar to => in js
    transform(s, s + strnlen(s, _maxlen), s, [&lastc](const char& c) -> char {
        const char r = (lastc == '' || lastc == 0) ? toupper(c) : tolower(c);
        lastc = c;
        return r;
    });
    return 0;
}
```

--- Lambda captures

They are thing enclosed in []:

> [var] Capture by value
> [&var] Capture by reference
> [=] Capture all variables by value (Cannot modify outside lambda)
> [&] Capture all variables by reference
> [&, var] Capture all variable by reference except var by value
> [&var,var2] Capture all variables by reference and var2 by value

--- Polymorphic lambdas C++14

```cpp
// Should be use with care
auto fp = [](const auto &n ) -> auto { return n * 4; };
```

## C pre-processor directives

Compilation = Preprocessor -> Compiler -> Optimizer -> Linker

--- Macors as Constants

> #define <CONSTANT_NAME> <CONSTANT_VALUE>

```cpp
#include <cstdio>

// Defining constant
#define BUF_SIZE 128 // Prefer constexpr int BUF_SIZE = 128;

#define GREETING "Hello World!" // Prefer constexpr const char* GREETING = 128;

int main()
{
    char s[BUF_SIZE]; // Using the macro for defining buffer size
}
```

--- Including files

They are used to include header files in source code files.

```cpp
#include  <system_header_file>
#include  "project_libraries_header_file"
```

--- Conditional compilation

> [#if] Check if some condition
> [#ifdef] or [#if defined(MACRO)] Check if some macro is defined
> [#ifndef] or [#if !defined(MACRO)] Check if some macro is not defined
> [#undef] Unset the MACRO definition
> [#else] Else to [#if]
> [#elif] Else if another condition
> [#endif] Clause the conditional

```cpp
#ifndef CONDITIONAL_H_
#define CONDITIONAL_H_

#ifdef _NUMBER
#undef _NUMBER
#endif

#ifdef _FOO
#define _NUMBER 47
#else
#define _NUMBER 2
#endif

#endif /* CONDITIONAL_H_ */
```

--- Defining MACROS

> #define TIME(a, b) ( a * b) // Create a macro function

```cpp
#define MAX_OF(a, b) (a > b ? a : b)

int main()
{
    int five = 5;
    int seven = 7;
    printf("MAX of 5 and 7 is ", MAX_OF(5, 7));
}
```

--- Unit Testing in C++


## C++ variadic functions

```cpp
template<typename T>
T rcatenate(T v)
{
    return v;
}

template<typename T, typename... Args>
T rcatenate(T initial, Args... args)
{
    return rcatenate(agrs...) + " " + initial;
}

int main()
{
    std::string s1 = "biz", s2 = "fox", s3 = "wiz";
    std::string result = rcatenate(s1, s2, s3);
    // Print the result
    return 0;
}
```

## Template metaprogramming TMP (C++17)

It a complete functionnal programming laguage that does not have loop, and branching, instead we use recursion annd specialization

```cpp
// Generic multiplication
template<typenname T>
T cube(const T&  value)
{
    return value * value * value;
}

// Meta programming version
// param is immutable
// This is executed at compile time
template<int param>
struct Cube{
    enum {
        // lvalue  is return when call Cube(parameter)
        value = param * param * param
    };
};

// Regular factorial implementation
int factorial(const int in, const int out)
{
    if (in > 1) {
        return factorial(in - 1, out * in);
    }
    return out;
}

//  Template metaprogramming
template<int in, int out>
// Recursive part of the function
struct Factorial : Factorial<in - 1, in * out> {};

// Branching or specialization part
// The specialization is evaluate first, whenever value is 1, return the value, else  Call the recursive template
template<int out>
struct Factorial<1, out> {
    enum {
        value = out
    };
};

// Fibonacci
template<int n>
struct Fibonacci {
    enum {
        value = Fibonacci<n - 1>::value + Fibonacci<n - 2>::value
    }
};

template<>
struct Factorial<0> {
    enum {
        value = n
    };
};

template<>
struct Factorial<1> {
    enum {
        value = n
    };
};

int  main()
{
    // ::value  return the result of the Factorial call 
    std::cout << Factorial<<4>>::value << std::endl;
}
```

## RxCpp framework
