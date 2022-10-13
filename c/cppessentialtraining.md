# C++ Essential tranning

-- formaters definitions

%d -> Integer values
%u -> Unsigned integer values
%s -> For string values
%c -> For characters
%lu -> Long unnsigned integer
%lf -> Floating point
%Lf ->  Long double floats.
%08 -> Hex value format
%zd -> sizeof format

## Basic Syntax

```cpp

// Pre-processor directives usually start  with # symbol
#include <iostream>

// Including user  created  header   files
#include  "./relative/path/to/file"

// puts works like writeln/println() as it write a string to the  standard outputs
puts("Text to print...");
```

-- Comments

```cpp
//! The next part is a single line comment

// This is a single line comment

//! Next line is multi line
/**
 * Multi line comment
 */
```

-- Identifiers

C++14 and C++17  have 73 keywords along with  some  alternative tokens [and,or,and_eq,bitand,bitor,compl,xor_eq,xor,or_eq,not,not_eq].

Note: As c++ variable without initialization are undefined, it's advice  to initialize variable at declaration time to avoid  null pointer exceptions.

--- Private identifiers

- Naming convention : _private_identifier

--- Qualifiers

- const -> Use to defined constant or compile time constant.

-- Pointers

A variable is a type and named location in memory.

```cpp
int x;
x = 1;
int y = x; // Create  a copy of the  value of x into the memory location named y

// Defining pointers
int *y_prt;  // Create a pointer to a memory address that can hold integer values
y_ptr  = &y; // & reference operator that  return the address of the y.
y =  *y_prt; // *y_ptr return the value pointed to by y_ptr. It's called the value dereferencing.
```

-- References (C++ only)

The are like pointers with slight deference.  Pointers can point to multiple thing at time, while references point to a single variable through  program execution. Reference are  not type like pointers.

```cpp
    int x = 0;
    int *x_ptr = &x;
    int &y = x;

    y = 42;

    printf("Value  of x is %d \n", x);
    printf("Value  of x_prt is %d \n", *x_ptr);
    printf("Value  of y is %d \n", y);
```

-- Primitive  array

It's inherited from c-array. It's a fixed sized container of elements of same size.

```cpp
    int  list[ARRAY_SIZE];

    // Initializer list
    int array[4]  =  {1, 2, 3, 4};

    // Assigning values by index
    list[0] =  1;

    // Initializing array first index  value
    *list =  1;

    // Creating a pointer to an array. Note: This does not required reference (&) operator as array are passed by  reference.
    int  *list_ptr = list;

    ++list_prt; // This point to the next element of an array
    *(++list_ptr)  =  4; // Increment the  pointer to point to the next item in the list  and set it value  to 4. It's similar to ++list_ptr;  *list_ptr = 4;
```

--  Primitive string (Null terminated strings)

It's a cstring, that is an array of characters. they  must end with  a 0 at the end of the string or '\0'.

```cpp
char s[] = {'S', 't', 'r', 'i', 'n', 'g', 0};

printf("String is: %s\n", s);
```

-- Conditionals

C++ has  if...else statements and ternary  operator for hanndling conditions branching.

In C++ logical values  are  evaluated to  0 or 1, as a any  non zero value is evaluated as true.

```cpp
    bool result = condition ? rvalue1 : rvalue2;
```

-- Conditional branching (Switch)

Note: C++ case statements requires constant  values.

-- while and do...while loops

> break [statement] -> It breaks out  of the  loop;
> continue [statement] -> It branch back to the begining of the loop skipinng the execution after it.

-- Iterating with  for

```cpp
// C style for loop
for (int  i = 0; i < MAX_VALUE; ++i)
{
    // code to execute on each iteration
}

char string[] = "abcdefg";

for (char *string_ptr; *string_ptr; ++string_ptr)
{
    // Execute on each iteration while pointer point of non zero value;
}

// C++ style iteration (C++11 or later)
//  Range based  for loop, it's a compile time feature
int array[] = {1, 2, 3, 4, 5};
char  s[]  = "string";

for (int  i : array )
{
    // Work with each element of the integer
}
for (char c : s)
{
    if  (c == '\0')  {
        break;
    }
    // Work with each character
}
```

--  The standard output

```cpp
//  C++ standard library object cout from the iostream for working  with std out
// While puts, printf from C standard library 
std::cout << "Hello World!";
```


## Data types

- int  (commonly 32bits integer) value -2,147,483,648 to  2,147,483,647
- unsigned int (Commonly  32 bits)  -> Range  0 to 4,294,967,295

-- Primitive types

---  Integers

---- [unsigned] char -> minimum character required to set character values (8its in modern  systems). Unsigned by  default.
---- [unsigned] short int -> It may be same a int (16its)
---- [unsigned] int ->  default integer  datatype (32bits) on  modern system
---- [unsigned] long int -> Double the  size of the default integer type (64bits or 32  bits)
---- [unsigned] long long int -> it may double the  size of int (64bits)

Note: If int  is  omitted, the  variable is still consider a short, long, long long  int.

C-defined data types  for integers requires <cstdint> library provide fixed  size integers:

```cpp
int8_t  x; //  uint8_t  for  unsigned (8bits)
int16_t  x; //  uint16_t  for  unsigned (16bits)
int32_t  x; //  uint32_t  for  unsigned (32bits)
int64_t  x; //  uint64_t  for  unsigned (64bits)
```

Note: [sizeof] return the sizeof the integer in  term of bits.

Note:  

```cpp
//  Using 0 in front of an  int variable value makes  if  octal (base8)
int octal_64 = 0223;

// Using  0x in front of the variable value, creates a base16 value (Hexadecimal)
int hexa_64  =  0x0093;

// Unsigned values
unsigned int x =  147U;
// Unsigned long values
unsigned long int x =  147UL;
// Unsigned long long values
unsigned long int x =  147ULL;
// Unsigned long values
long int x =  147L;
// Unsigned long long values
long long int x =  147LL;
```

--- Floating (representing real values)

One should be careful when working with  floating  point number, with issues  with precisions.

```cpp
float f;
double df; // Double precision floating  point
long double ldf;  // 128 bits  // on 80bits (on IEEE standard) will be used  or on  some  system 64bits

f = 5e20 ; // Scientific notation  of  the  floating point number
```

--- C-string (Null Terminated  array of characters)

C-strings are null terminated string that may differ from the C++ object string type.

```cpp
char cstring[] = "Litteral String";

// Const Pointer to a character array
const char *cchar = "Litteral String"; // Pointer to an array that can not be changed

for (uint32_t i = 0; cchar[i]; ++i) {
    // Print or do something with the string
}
```

---- Escape characters

Note: Escape characters -> Each escape sequence begin with [\] character.

Example: \n, \", \', \\

\nnn -> octal nnn
\xnnn -> hexa nn
\unnnn -> Unicode code Points

---- Qualifiers

They are used to adjust quality of an object or a variable.

> CV qualifiers [`const, volatile, mutable`]
>> const -> for immutable data type
>> volatile -> variable that may be change by another process (threading)
>> mutable -> makes data writable from a const function call

> Storage duration qualifier [`static, register, extern`]
>> static -> variable scope behond the execution block where they are defined. They are store globally. Their lifetime is the lifetime of the program. Used to create shared memory variables.

>> register -> They are saved in processor memory
>> extern -> They are defined in separate translation unit linked at compile time.

```cpp
// Create a static compile time constant
const static x = value;

// Creating a const mutable variable
```

-- References

Note: Prefer  usage of const reference to a avoid side effects

```cpp
// This func does not update the value of i param passed in
const int& func(const int& i  ) {
    // Here we set i to a new value in order to modify it
    int _i = i;
    return ++_i;
}
```

--- Structs (For creating user defined type)

In C++, structs can include function members as well, to allow them to be threated as class.

```cpp
struct Employee {
    int id;
    const char* name;
    const char* role;
};

int main() {

    Employee p = {42, "Jack", "Administrator"};
    Employee* p2 = &p;

    // Accessing using member access operator
    printf("Employee details: ID - %d, Name: %s, Role: %s", p.id, p.name, p.role);

    // Accessing using pointer access operator
    printf("Employee2 details: ID - %d, Name: %s, Role: %s", p2->id, p2->name, p2->role);
}
```

---  Bitfields

They help in saving space while creating object.

```cpp
// This  helps in saving space while creating object
struct Preferences {
    bool likMusic: 1; // 1 is the bit field representing 1 bit
    bool hasHair: 1; // 1 is the bit field representing 1 bit
    bool hasInternet: 1; // 1 is the bit field representing 1 bit
    unsigned int numOfChild: 4; // 4 is the bit field representing 4 bits
};
```

--- Enumeration

The make good alternatives to preprocessors constants.

```cpp
// Definitions
// enum Enum_Name : DType  {[...values]};
enum Card_Suit : uint8_t  {SPD, HRT, DIA, CLB}; // Create consecutive integer  values
enum Card_Rank : uint8_t  {ACE = 1, DEUCE = 2, JACK = 11, QUEEN, KING}; // QUEEN =  12 and KING = 13

```

--- Unions

Data structure for using same memory space for different types.

```cpp
union ipv4 {
    unint32_t i32;
    struct {
        unint8_t a;
        unint8_t b;
        unint8_t c;
        unint8_t d;
    } octets;

}
```

--- Typedef

Helps in providing alias for a type in a statically  type language.
By convention end C++ types definitions with  [_t]

```cpp
// Defining type using type definition
typedef unsigned char points_t;
typedef unsigned char rank_t;

// Using type definitions
struct Score {
    points_t p;
    rank_t r;
};
```

--- Void

Represent lack of value for return type and function parameters.

```cpp
// In C func() can takes argument during call, while in func( void ) does not
// In C++ func() is like func( void ) [compatibility with C language] which in both case does not take arguments
void func( void ) {
    puts("Do something"); // 
}
```

--- Auto type

Begining with C++ for defining variable that get it type from a r_value of the right side expression. It's like := in go.

```cpp
#include <cstdio>
# include <string>
# include <typeinfo>

string func()
{
    return string('');
}

int main()
{
    auto x = func();

    printf("C string representation of x %s", x.c_str);

    if (typeid(x) == typeid(string))
    {
        puts('x is a string');
    }
}
```

--- Unambiguous null pointer constant

[nullptr], in C++ is defined as a null pointer constant or a null pointer value, that helps solving issue with function amiguity when overloading fuctions. It's a pointer of any value.

```cpp
#ifndef NULL
#define NULL (0LL) /* Common C++ definition */
#endif

void f (int i) {
    printf("Value of i is %d\n", i);
}

void f (const char* s) {
    printf("the pointer is %p\n", s);
}
```

--- Classes (For creating user defined type)

--- Pointers (Statically  type variable pointing to a memory  address)

### Operators

--- C++ operators

```cpp
// Integer like exponentiation function
#include <cstdint> // for std::int_fast64_t
 
// note: exp must be non-negative
std::int_fast64_t pow(int base, int exp)
{
    std::int_fast64_t result{ 1 };
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }
 
    return result;
}
```

> [+, -, %, /, *] (Arithmetic operators)
> [=] (Assignment operator)
> [+=, -=, %=, *=] (Compound assignment operator)
> [++, --] (Incremental & Decremental operators)
> [==, <=, >=, <, >] (Relational operators) for comparing relative values
> [&&, ||, !] (Logical operators for testing logical conditions)
> (|, &, ~(bitwise of), <<(left shift), >>(right shift)) (Bitwise operators for performing bit manipulation)

```cpp
// Convert uint8 integer to a binary representation
const char* u8_to_cstr(const uint8_t& x)
{
    static char buff[sizeof(x) * 8 + 1];
    for (char& c : char) {
        c = 0; // Reset the buffer
    }
    char* buf_ptr = buf;
    for (uint8_t bitmask = 0b10000000; bitmask; bitmask >>= 1) {
        *(buf_ptr++) = x & bitmask ? '1' : '0';
    }
    return buf;
}
```

> [lhs ? "true": "false"] (Ternary conditional operator)

> [new, delete] (Dynamic memory operator) -> Specific to C++
Note: Every object initialized with new must be delete with delete otherwise program must leak memory.

> (type) (Type casting operator for taking a value from one type to another type explicitly)

Note: Types being casted must be compatible

> sizeof(object) (Use for determining the size of an object in bytes)

```cpp
size_t = sizeof(x);
printf("Size of x is %zd\n", x);
```

> typeid(object) (Returns a type info oject defined in <typeinfo> for getting the type of an object)

```cpp
struct Point {
    int8_t x;
    int8_t y;
};

int main()
{
    Point origin = {0, 0};
    Point next = {0, -10};
    printf("type is %s\n", typeid(Point));

    if (typeid(origin) == typeidof(next)) {
        // do something
    }
}
```

> () -> / -> * -> + -> - (operators precedence)

### C++ Functions

Function create a modular approach in implementations. Function create local scope for it parameter unless passed by reference.

--- Creating function

```cpp
// Function declaration in header file
r_type func_name(p_type parameter_list);

// Defining a function
r_type func()
{
    // function definition
    // Return value after logic execution
    return r_value; // optional for void return functions
}
```

--- Storage class and functions

Storage  quantifier of a function variable is automatic, and will live temprorary on the stack created during function execution. If one want to persist the state  of the variable use the [static] storage modifier.

Also, auto is not allowed in functions other that [main()] from C++11.

--- Function return values

Returning larger objects:

```cpp
#include <string>

// When returning reference, default action should be to declare the  return type as const reference and later remove it require to change  the  return value
const string& func()
{
    const static string s = "This is func()";
    return s;
}

int main()
{
    // Do something with the func()
}
```

--- Using function pointer

It create a reference type to a function

```cpp

#include <string>
const string& func()
{
    const static string s = "This is func()";
    return s;
}

int main()
{
    string (*pfuncs[])() = {func, func};
    string* pfunc() = func; // This is like creating a closure in PHP
    // calling the function
    printf("Function pointer  result is %s", pfunc());
}
```

--- Variadic function

Requires <cstdarg> library

```cpp
#include <stdarg>

double func_average(const int count, ...)
{
    // Get the variadic parameters passed to the function
    va_list args;
    double result = 0.0;
    // Create a counter using count arg
    va_start(args, count);
    // Loop through each item and get range from the type
    for (auto i = 0; i < count; ++i) {
        result += var_arg(args, double);
    }
    // End looping
    va_end(args);
    return result / 5;
}

int message(const char* fmt, ...)
{
    // Get the variadic parameters passed to the function
    va_list args;
    va_start(args, fmt);
    int result = vfprintf(std::stdout, fmt, args);
    put("");
    va_end(args);
    return result;
}
```

### Classes and objects

C++ classes derives from C++ structs, with the difference that data members in classes are private  by default while being public in Structs.

Use struct when the data structure has only data members and classes when data structure has behaviour (function) members.

```cpp
// Define in class header definitions
class ClassName
{
    private:
        // Private members declarations
        int x;
        int y;
    public:
        // Class default constructurs
        ClassName();
        void setX(int value);
        int getX() [const];
};

// class behaviours definitions
void ClassName::setX(int value)
{
    x = value;
}

int ClassName::getX() [const]
{
    return x;
}
```

--- Const member functions

```cpp
class ClassName
{
    public:
        double MethodName();
        double MethodName() const; // Create a const safe  method that create an immutable getter
}

int main()
{
    // As a rule of thumb const safe method will always being call and non const method will be call only by non const instances.
    const ClassName c; // create an immutable object
    c.MethodName(); // Calls the const safe method
}
```

--- Class constructors and destructors

```cpp
class Point
{
    double _x, _y;
    public:
        // Default constructor 
        Point() const;
        // Copy constructor 
        Point(const Point&) const;
        // Constructor with parameter
        Point(const double&, const double&) const;
        // Class destructor
        ~Point();

        // Function members
        double getX();

        double getY();
}

// Class implementations

Point::Point() const: _x(0), _y(0);

// Copy constructor 
Point::Point(const Point& p) const
{
    _x = p.getX();
    _y = p.getY();
}

// Constructor with member initializer
// _privateMember(param)
Point::Point(const double& x, const double& y) const : _x(x), _y(x);

// Function members
double Point::getX()
{
    return _x;
}

double Point::getY()
{
    return _y;
}

Point::~Point()
{
    // class destructor
}

int main()
{
    const p = ne
}
```

--- Operators overloading

```cpp
class Rational
{
    private:
        int _n =  0;
        int _d = 1;
        
    public:
        Rational(int d, int d); _n(n), _d(d) {}

        // Copy constructor
        Rational(const Radical& r) : _n(r.numerator()), _d(r.denominator()) {}

        // Destructor
        ~Rational() { _n = 0; _d = 1; }
        // Numerator getter method
        int numerator()
        {
            return _n;
        }

        // Denominator getter method
        int denominator()
        {
            return _n;
        }
        // Member functions

        // Operator overloading
        // The assignment operator overloading should not be constant as it modifies the object
        Rational & operator = (const Rational& rhs)
        {
            if (this != rhs) {
                _n = rhs.numerator();
                _d = rhs.denominator();
            }
            // The this keyword is a reference to the current object
            return *this;
        }

        Rational & operator * (const Rational& rhs) const
        {
            return Relational {_n * rhs.numerator(), _d * rhs.denominator()};
        }

        Rational & operator / (const Rational& rhs) const
        {
            return Relational {_n * rhs.denominator(), _d * rhs.numerator()};
        }

        // ...etc
}
```

--- Non member functions overloading

```cpp
Rational operator + (const Rational& lhs, const Rational& rhs)
{
    return Rational{lhs.denominator() * rhs.numerator(), lhs.numerator() * rhs.denominator()};
}
```

### C++ Templates

C++  approach to genneric programming.

--- Function templates

```cpp
template <typename T>
T func(T param) {
    // Do somethinng with the function
}
```

--- Function templates

```cpp
template <typename T>
class Classe {
    T items[];
    // Do somethinng with the function
}

template <typenname T>
Classe<T>::Classe()
{
 // classe constructor
}
```

## Standard Library

C++ includes most C standard library with a prefix c to differenntiate references.

--- Standard file I/O

```cpp
#include <cstdio>

constexpr int MAX_STRING = 1024;
constexpr int REPEAT = 5;

int main()
{
    const char* filename = "Textfile.txt";
    const char* str = "Literal string to be written";

    // Create an input stream
    FILE* fw = fopen(filename, "w"); // File modes range from w(Destroy content and create file if not exists), w+(Destroy content and create file if not exists), r(Read from start, fails if file does not exists), a(Append to file, create if not exists), a+(Open file for read/write, write at and end and create file), b(Binary mode)
    for(int i=0; i < REPEAT; i++)
    {
        // fputs for writing data to a file pointer
        fputs(str, fw);
    }
    // Close the fw handle
    fclose(fw);

    // Reading file content
    char buff[MAX_STRING];
    // Open file for reading
    FILE* fr = fopen(filename, "w");
    // fgets() for reading file content
    while(fgets(buff, MAX_STRING, fr)) [
        fputs(buff, stdout);
    ]
}
```

--- Reading and writing file in bynary mode

When writing binnary files, one should use "wb" file open mode

> use fwrite instead of fputs when writing binary files
> use fread instead of fgets for writing.

Use b flags for performing binary read and write operations when will support ms windows while writing non text data  to files.

--- File managements

```cpp

#include <cstdio>

int main()
{
    static const char* filename = "Textfile1";
    static const char* filename2 = "Textfile2";
    //  Creating file
    // File is created  where the executable is located
    FIlE f_handle = (filename, "w");
    // Renaming files
    rename(filename, filename2); // return 0 or 1
    // Deleting files
    remove(filename2); // return 0 or 1
    fclose(f_handle);
}
```

--- Unformatted character I/O

> fputs(data, stream); // Send data to the specify output

```cpp
#include <cstdio>

constexpr int BUFSIZE = 256;

int main()
{
    static char buff[BUFSIZE];
    // write to the standard output
    fputs("Prompt> ",  std::stdout);
    // Ensure that  streams that are send to output are written properly
    fflush(std::stdout);
    // Reading from standard input and set the buffer
    fgets(buff, BUFSIZE, stdin);
    // Write to the standard output
    fputs(buff, std::stdout);
    return 0;
}
```

--- Formatted character I/O

> fprintf(output_stream, format, variadic_parameters);
> printf(format, variadic_parameters); // Write to standard output

--- C String functions

Requires <cstring> headers to be  include:

> strncpy(source, dest, MAX_BUFFER_SIZE); // Copies up to MAX_BUFFER_SIZE - 1 content from source to dest
> strncat(dest, source, MAX_CHAR_TO_CONCATENATE); // Concatenate strings
> strnlen(source, MAX);
> strcmp(lhs, rhs); // Returns 0 if strings are equals and < 0 if rhs greater lhs and > 0 if lhs greater than rhs
> strchr(source, character); // Find position of a character  in  a string. Return a nullptr when not found
> strstr(source, needle); // Find a position of a substring in a string. Return a nullptr when not found

--- Handling system errors

Requires <cerrno> header provide error number for system call errors

> perror(prefix); // Return the error generated by a given call
> strerror(errorno); // Requires <cstring> header file. Return the error as string

### C++ Standard Template Library

C++ standard Template Library provide container for handling complex data structures:

> vector dynamic array like container
> list, set, dequeu, queue, etc...
> iostream library
> string library

---  Vectors
Requires <vector> header which provide vector type and methods.

```cpp
#include <vector>

int main()
{
    const vector<int> v = {1, 2, 3, 4, 5};

    // Looping using iterators
    // v.begin() and v.end() returns an vector<T>::iterator
    for (auto i = v.begin(); i < v.end(); ++i) {
        // do something
    }

    // Vector indexes are zero based
    // Access element at a given index
    std::cout << v.at(4) << std::endl;
    // Array index access
    std::cout << v[4] << std::endl;

    // Range  base  for loop
    for (int& i : v) {
        // Do something with the index
    }

    // Insering at index
    v.insert(v.begin() + 2, 42);

    // Get the size if the vector
    printf("%zd\n", v.size());

    // Remove  item from an index
    v.erase(v.begin() + 2);

    // Push item back
    v.push_back(48);

    // Get the element at the back
    std::cout << v.back(); << std::endl;

    // initialize from c-arrays
    const static size_t size = 10;
    int array[size] = {1, 2, 3, 4, 5, 6, 7, 8, 10};
    vector<int>  v2 = vector<int>(array, array + size);

}
```

--- Strings

Requires the <string> header which provide C++ string type and methods

```cpp
#include  <string>

int main()
{
    string s1 = "String Literal";
    string::iterator it;

    // Getting string length
    // size() is general to most container classes.
    std::cout << s1.size(); << std::endl;
    std::cout << s1.length(); << std::endl;

    // strings concatenation (Make use of the + operator)
    const s2 = s1 + ":" + " Hello World!";

    // comparing 2 strings
    // String class override ==, <, >, <=  operator for comparison
    std::cout << s1 == s2 ? "YES" : "NO" << std::endl;

    // Loop through each character
    for (const char  : s1) {
        // Do something with character
    }

    // Cleanning characters from position
    std::cout << s1.erase(s1.begin());


    // Replacing characters from position
    std::cout << s1.replace(5, 2, "ain't");

    // substrings
    std::cout << s1.substr(5, 2);

    // Find string or character at position
    std::cout << s1.find("string");

}
```

--- I/O streams

Required <iostream> header which provide features for working with innput and output streams.

--- Exception handling

```cpp
class Exception : public exception
{
    const char* msg;
    Exception();

    public:
        Exception(const char* s) throw () : msg(s) {}
        // override exception handlers
        const char* what() const throw() { return msg; }
}

int main()
{
    // Catching the exception
    try {
        // Code definition
    } catch (Exception e) {
        // Exception handling code
    }
}
```
