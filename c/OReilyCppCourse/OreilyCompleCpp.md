# Complete C++

## Copying C strings

Remember to always have a left '\0' byte space at the end of the array.

-- Copying string

Copying C strings is done through:

```cpp
char *buff = new char[100];

// Copy string using safe version of strcpy which is strcpy_s
strcpy_s(buff, 100, 'Azandrew Sidoine');

```

## Basic Language facilities

> endl -> Flushes the buffer and add line to the stream handler

-- Data types

<cfloat> and <climits> header files provides some macros that defines the minimum and maximum range of number and pointers.

-- Console I/O input values\

Added Notes:
> std::cin - is an instance of the std::basic_istream
> std::cout - Provide an instance of the std::basic_ostream

> std::cin [std::istream]----> this class is used to read user input. It drops the character when a line break or space character is encontered.

---- Advantages

> It forces initialization
> Use direct initialization for array types
> It prevent narrowing conversions

To read an entire line, use the getLine method of the cin class. It can help to read from any input stream class:

> std::cin.getLine(buff, number_or_character, delimiter);

```cpp
#include <iostream>

int main()
{
    std::cout << " What is your name? ";

    char buff[255] = "";
    std::cin.getLine(buff, 100, '\n'); // Read input until the newline is enconter
}
```

-- Uniform initialization C++11

C++11 provides a unique way to initialize variables using {}. Prefer usage of uniform initialization for user defined types.

```cpp

#include <string>

// Before C++11
int value; // Uninitialized

int value = 1; // Copy initialization

std::string value_str("C++"); // Direct initialization for UDT

char char_arr[10]; // Unitialized

char char_arr2[10] = {'C', '+', '+'}; // Aggregate initialization & Copy initialization

// From C++11
int b1{}; // Variable is autoly initialized to default type (0)
int b3{5}; // Direct initialization

// Uniform unitialization of arrays
char buff[20]{"Hello World!"}

// Dynamic array initialization
int *ptr = new int{};

char *char_ptr = new char[10]{};

char *char_ptr = new char[10]{"Azandrew"};

// User defined types
T udt_val{}
Type udt_val2{v}
```

## Pointers

Good practices:

- Initialize pointer during declarations

-- Null pointer of C++11

It's a type safe pointer better than NULL macro of C language. Prefer usage of the [nullptr] over [NULL] macro.

> Note : Never attempt to read or write to nullptr


## Reference type (&variable)

It's an alternative name for a variable, and must always be initialized. It's bound to its referent, It can be used to modify a variable in directly (like pointer).

- But unlike pointer, it points to only one variable.
- A reference can not be null

## Const qualifier

[const] create a variable that will not change over program execution.

- Advantages

> When passing a value to a function by reference and don't want to change the variable apply [const] to it.

```cpp
const int CHUNK_SIZE = 512;

// ptr is a pointer to a constant integer
const int *ptr = &CHUNK_SIZE; // Creates a pointer to a constant value (The pointer itself is not a constant and it can point to another const variable)

// ptr is a constant pointer (Address cannot be changed) to a constant integer
const int *const ptr = &CHUNK_SIZE; // Creates a constant pointer to a constant value
```


## Auto type inference

In c, [auto] indicates storage class of a variable.
From C++11, [auto] indicates an automatic type inference from the initializer value.

```cpp
// <initializer> can be return value by a function, expression result, etc...
auto auto_var = <initializer>;
```

## Range based for loop

The range based for loop allows iteration over arrays and containers.

Advantages:

> They don't need index variable
> Each iteration returns an element
> Can be used with object that behave like range

```cpp
// Works like for in list of python and javascript
for (const auto &x : arr) {
    // Work with each item of the array
}
for (auto &x : arr) {
    // x varaibles are mutable
    // Work with each item of the array
}
```

## Function overloading

Function overloading is provided using name mangling which is generated depending on type & number of function arguments.

The consequent is C++ function are not callable from C code.

To prevent name mangling, C++ provide [`extern C`], that can be applied on global functions and variables, which supresses name mangling.

> Note : extern is only applied to one function in a set of overloaded functions.

```cpp
// Apply only during declaration
extern "C" void Print(const char* message);
```

## Inline functions

Inline function are function prefix with inline keyword. This may improve the performance but must be used with small functions and with care.

Note:
- Inline function must be defined in header files
- Request the compiler to replace the call with function body, making the overhead of function call to be avoided, no need for the compile for saving the return address on the stack.

```cpp
inline int func(int i)
{
    return i * i;
}
```

## Function pointers


```cpp

void func(int lhs, char rhs)
{

}

int main()
{
    // Creating a function pointer
    void(*fncptr) (int, char) = func;
}
```

Note: `atexit()` -  runs a function when the program exit or is exiting.

## Namespace

They helps prevent name clashes. They named declarative region used for declaring types.

```cpp

namespace [<name>] {
    // (namespace, class, functions, constants, etc...)
}

namespace drewlabs {
    void func()
    {
        printf();
    }
}

namespace azlabs {
    void func()
    {
        printf('Hello World!');
    }
}
```

## Memory management

C/C++ programs are provided with #ts types of memory areas:

- stack > Allocated automatically for local variables
- data > For global and static data
- heap > Allocated at runtime

Note:
    All memory is taken from the process address space

- C/C++ provide support for memory allocation at runtime (dynamic memory allocation)

NB:
    Memories allocated on the heap must be manage by the programmer (freeing/deleting, allocating memory)

C Functions for dynamic alloc:

```cpp
malloc() // Allocate raw memory on the heap and return a pointer to the memory
calloc() // Allocate memory on the heap and init it to zero
realloc() // Allocate larger chunk of memory for an existing allocation
free() // Deallocate/releases the memory allocated
```

--- Dynamic mem alloc in C++

C++ provides 2 operators for allocating and deallocating memory dinamically.


```cpp
// Syntax
<Type> *<variable> = new <Type>(optional args);
// Deallocation
delete <variable>

// Example
int *intptr = new int(0);
// Deallocating memory
delete intptr;
```

Allocating memory for arrays is a bit different:

```cpp

<Type> *<variable> = new <type>[size];

delete []<variable>;

// Example
int *arr = new int[5]{1, 2, 3, 4, 5}; // Allocate memory for 5 integers
// Deallocating memory
delete []arr;
arr = nullptr;
```

Allocating for 2 dimension arrays:

```cpp
int *rows = new int[10];
int *columns = new int[7];

int **matrix = new int *[2];
matrix[0] = rows;
matrix[1] = columns;

// Assiging values to the matrix cells
matrix[0][1] = 45;

// Deleting 2D arrays

delete []rows;
delete []columns;

delete []matrix;
```


## Classes and Objects

### C++ Classes


```cpp
class <name>
{
    <modifiers>:
        <member variables>; // Properties
        <member functions>; // Methods
};
```

### Classes Constructor and Destructors

Destructor are unique and can't be overloaded.

```cpp

class <name> {

<modifier>:
    <name>() {} // Default constructor // Implicit constructed if user does not provide

    <name>(<params>) {} // Constructors with parameters

    ~<name>() {} // Destructor definition
};
```

### Structures for creating UDT

Default access modifiers are public by defaults.

- C++ structs are used to represent simple abstract types such as point, vector3D, etc... In which property must be public
- C++ structs are also used for function objects


## Non-static Data members Initializers

- These ensures that the members are initialized with values.
- They can be used to initialize any type
- Compiler autoly generates initialization code

```cpp

class <Class>
{
    <modifiers>:
        <Type> <var1>{<initializer>};
        <Type2> <var2>{<initializer>};
}
```

Cons:

Not possible to define non-static members with <auto>.

### <this> Pointer.

<this> reference current object and has meaning only in member functions.
- It's a constant that we cannot assign to.

### Constant member function

They are method of a class thst are qualified with the const keyword.

Note:
- Const member func, cannot change value of the member variables
- Useful for creating readonly functions
- Const object can invoke only const member functions
- In const member func, we can only invoke const member functions


```cpp

class <Class>
{
    <modifier>:
        <Type> const_func() const;
};

<Type> <Class>::const_func() const {

}
```

### Static member varibales

> They are class member register in the global registry. 

> They are not part of the class and only one copy of it exists.

```cpp

class <Class>
{
    static <Type> <static_var>;
};

// Accessing static variables

<Class>::<static_var> = <value>;
```


### Static member function

> They are function that belongs to the class and not to the object.

> They do not receive the <this> keyword, and therefore can not access non-static members of the class

> They are invoked directly through class name

```cpp
class <Class>
{
    static <Type> <static_func>([<params>]);
};


<Type> <Class>::static_func([<params>])
{
    // Access only class static members
}
// Accessing static variables

<Class>::<static_func>();
```

### Copy constructor

- Used to create a copy of an object state into another object
- Default constructors copy values
- User defined implmentation requires pointer for members

-- Rule of 3 (Copy constructor + =Operator + Destructor) (3)

* When a developper implements a copy constructor, it must provide a destructor and a copy asignment operator

### Delegating Constructor (C++11)

- Allow a constructor to invoke another constructor
- Replacement for common initialization
- Reduces duplicate initialization codes in multiple constructor

```cpp

class <Class>
{
    <Class>(): <Class>([<params>])
    {

    }

    // Delegated constructor that initialize members of the class 
    <Class>([<params>])
    {
        // Initialization code
    }
}

```

### Default and Deleted functions

From C++11 there is a <default> keyword that triggers the compiler to generate a default constructor if a parameterized constructor is defined.

```cpp
class <Class>
{

    <modifier>:
        <Class>()  = default; // Implicitly generate the default constructor
};
```

### L-values, R-values and R-values references

L-value                         R-value
- They has names (variable)     - Don't have names (result of expressions / expressions/temp values)
- Can be assign values          - Can't be assigned vales
- L-values persist state        - R-values does not persist beyond expression
- Func returning by reference,  - Function returning by value return r-values
return an l-value
- Reference to l-value          - R-value reference are reference to r-value (C++11)
(Called l-value reference)

- R-value reference are added to C++11 to implement move semantic
- R-value reference are reference to temporary variables
- They are created with <&&> operator, and can't point to an l-value

```cpp

int &&r1 = 10; // R-value reference to 10
int &&r2 Add(4, 6); // Add func return an R-value, and therefore can create temp R-value reference
int&& r3 = 7 + 2; // Expression return temporary

// Function accept an l-value reference
void Print(int& x) {

}

// Same function accepting a const l-value reference
void Print(const int& x) {
    
}

// Function accepting r-value references
void Print(int&& x) {
    
}
```

### Move semantic

In copy semantic copy is implemented through copy constructor, and copy the state of the object passed as parameter.

In order to avoid waste of memory done by the internal copy, we can simply move the temporary variable passed as parameter, and that is done through move semantic.

Note: Rules of (3) become rule of (5), as if we implement copy semantic, we must implement move semantic.

```cpp

// Implementation of the move constructor

```

## Copy elision

It's a techinic used by the compiler to eliminate temporary object.
Most compilers implement it internally.

```cpp
int main() {
    Integer a = 3; // Compiler call the parameterized constructor internally
    // Integer a = Integer(3);
}
```

Note:
    Be careful to accessing moved objects.

## std::move

It forces the compiler to perform a move operation the object instead of copying

## Operator overloading

Provides ways to implement primitive operators, and allow UDT to take advantages of the primitive operators.

- Operator overloading implemented as memer function accept 1 argument for binary operators and 0 argument for unary operator.

- Operator overloading implemented as non-memer function accept 2 argument for binary operators and 1 argument for unary operator.

```cpp
// Syntax of the operator overloading
<Type> operator <#>(<arguments>)
```

-- Function call operator overloading

```cpp

class <Class>
{
    <Type> operator ()();  
};

operator <Class>::()
{

}
```

-- Friend keyword

Operator or function declared as fiend, will access private property of the class

```cpp

class <Class>
{
    friend <Type> func_();

    friend <Type> operator <#>();
}

<Type> func()
{

}
```

--- Smart pointers basics

In C++ prefer smart pointer from basic pointer

--- Operator overloading

> Associativity, precedence & arity(operand count) does not change
> Operator functions should not be static except for <new> & <delete>
> One argument should be user defined type
> If a binary operator accept primitive as first operand use global function overload
> Not all operators can be overloaded : ., >:, .* sizeof

--- Type conversion

To cast variable explicitly:

    - basic -> basic
    - basic -> user-defined
    - user-defined -> basic
    - user-defined -> user-defined

In C++ prefer usage of [static_cast<Type>] cause it check for doability of the variables.

```cpp

// C style cast
(<Type>)<expresion>;

// C++ style cast
<Type> lvalue = static_cast<Type>(<expresion>);

// Alternative to c style cast
reinterpret_cast<Type>(<expression>);

// Const cast
<Type> lvalue = const_cast<Type>(<expression>); // Cast an create a const variable
```

--- Converting from UDT to primitive type

Note:

Using explicit on the operator, force class user to explicitly perform the cast instead of the compiler.

```cpp


class <Class>
{
    [explicit] operator <primitive_type>() [const];
}

<primitive_type> r = static_cast<primitive_type>(t)
```


## Smart Pointers