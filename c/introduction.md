# Introduction to C++

## Comments

```c++
// This is a single line comment

/* This is a multi line comment */
```

## C++ standard namespace

```c++
// referencing or importing standard library

using namespace std;

//  Now the  standard library is  available

//
//  Printing and adding new line to output
std::cout  << "output" << std::endl;

// Reading user input
std::string variable;
std::cin >> variable;

// New line
std::cout  << "Hello  World!  \n";
```

## Variable definitions and Data  Types

> DataType variable_name[ = [default_value]];

- Int ---> C/C++ integer hold 4Bytes
- float  ---> C/C++ 4Bytes floating point values
- double  ---> C/C++ 8Bytes floating point values
- char ---> C/C++ 1byte character saving ASCII representation of the character
- string --->  Buffer array of C++ characters
- bool ---> 1bit data type for representing truthy values

Note: Comparing the c/c++ char, makes the computer compare their ascii value correspondants.

Note: As rule of thumb, initialize  variables as we declare them, cause the compiler does not clean pre-allocated memory values. Therefore it can happen that if the variable is not initialized, the compiler will assign garbaged values to it.

## Storage of data in memory

C++ offer a casting function that can be used calling `static_cast`:

```cpp
// Arithmetic operator

// Module % -> return the remainder of the division a by b
int remainder  =  std::static_cast<int>(a % b);  // Cast the modulo  value to integer.
// Math  functions
// ceil() -> highest  direct integer
// floor() -> lowest  direct integer
// abs()  -> integer number absolute function
// fabs() -> floating point number absolute function

// Random number generator
srand(time(0)); // Create a random number generator seeder since epoch
rand(); // Generate random generator
```

## C/C++ Constants

Declaration:

> <CONST> <DATA_TYPE> <VARIABLE> = <INITIALIZED_VALUE>;

```cpp
const int MAX_CONSTANT_NUMBER = 'Constant_Value';
```

Manipulating Input and Output:

> std::cout.setf() -> Set the standard output format

```cpp
// Inculde the manipulation library headers
#include <iomanip>

//  Set format output
std::cout.setf(ios::fixed);
std::cout.setf(ios::showpoint);

// Setting precision requires iomanip library
std::out << "Description"  << setprecision(2) << var <<> "\n";
```

## Working with Time <`cstdlib`>

Working with  time requires including c stanndard library

```cpp
#include  <cstdlib>

int main() 
{
    // Get  time since epoch
    int time = time(0);
}
```

## Arrays

Declaration:

> [<CONST_MODIFIER>] <DATA_TYPE> <VARIABLE>[SIZE] [= <INITIAL_VALUE>]

```cpp
string players[10];

// Declaring and initializing arrays
string players[3] = {"player_1", "player_3", "player_3"};

// Setting index of a n array
players[2]  = "Player_3_Updated";
```

Multi dimentionnal array

> [<CONST_MODIFIER>] <DATA_TYPE> <VARIABLE>[<X_DIMENSION_SIZE>][<Y_DIMENSION_SIZE>] [= <INITIAL_VALUE>]

Note:

```cpp
// Integer between 0 and max
// seedind rand
srand(time(0));
rand = (rand() % MAX_VALUE) + 1
```

## Decision Making

```cpp
if (conditions) {
    // Run code if condition is true
} else {
    // Else run the code if condition is false
}

// if... else if ... else
if (conditions)
{
    // Condition is true
} else if (conditions2)
{
    // Conditions 2 is true
}
else
{
    // Catch all statement
    // All above conditions are false
}

// Boolean operators / Logical operators
// < ; > ; <= ; >= ; == ; != 
// ! Not operator
// || (OR operator ) && (AND Operator)
```

## Switch statement

```cpp
switch (testing_varible):
{
    case Value_Case_1:
        // Execute the match statement
        break; // return can be used
    case Value_Case_2:
        // Execute the match statement 2
        break; // return can be used
    default:
        // Catch all statement
        break;
}
```

## For loop

```cpp
for (int i = 0; i < MAX_VALUE; i++)
{
    // Execute loop statement till i heightest integer less than MAX_VALUE
}
```

## While condition loop

Test conndition in the expression of the while statement before executing statement code.

```cpp
while (condition)
{
    // Execute statement
    // Remember to change loop control variable to avoid infinite looping
}

int index = 0;
while (index < MAX_VALUE)
{
    // Do something
    index++;
}
```

## do...While Loop

It's a post loop function. Condition is tested after the loop statement execute at least once.

```cpp

do
{
    // Handlers implementation
} while (condition);

string password = '';
do
{
    printf("Enter your password > ");
    std::cin >> password;
} while(password != old_password);

```

## Functions

- cctype library

> isdigit(char) -> checks if character is a digit value
> isalpha(char) -> checks if character is a alphanumeric value
> isupper(char) -> checks if character is an upper case value
> islower(char) -> checks if character is an lower case value

- cstring library

> toupper()
> tolower()

### Creating functions

```cpp
<RType> FunctionName(parameter list)
{
    // Function body
}

void printReceipt(string param1, float param2)
{

}
```

### Function prototype

```cpp
<RValueType> FunctionName(parameter_list);

// in function prototypes, the param name is not that much required
<RValueType> FunctionName(Type [param], Type [param2]);
```

Note: In C/C++ simple types or user defined types are passed by value. Arrays are passed by value.

Passing by reference create a shared pointer to a value.

## File I/O

Required use of fstream library.

```cpp
#include <iostream>
#include <fstream>

int main()
{
    // Create a pointer to an input file
    ifstream input;

    // Create a pointer to output file
    ofstream output;

    // Open a  new file and set it pointer to the pointer created
    input.open("path/to/file");

    // Testing if the file opened
    if (input.fail())
    {
        // Do something if the failed opening file
    }
    string supply[ARRAY_SIZE];
    string qty[ARRAY_SIZE];
    while(input >> supply[i] >> qty[i])
    {
        // do something with the read data
        i++;
    }

    // Closing the opened file
    input.close();

    /// Writing output files
    // if the file does not exist, it will create the file, else
    // the file will be overriding unless app is specified
    // write is done using the << indirection operator
    output.open("path/to/file", ios::app);
    output.close();
}
```

## Data Structures

### Structs

Arrays allows in storing same type data in on building block, while structs allows to create a block of related data of #ts types.

Multiple pieces of data put in one memory block.

```cpp
// Declaring struct
struct DataTypeName
{
    // members of the structure
};

// Example of declaration
struct Student
{
    string name;
    float gpa;
};
// Creating a variable of type student struct
Student student;

// Assigning value to members or properties

student.name = "Student name";

// Creating array of structs, array declaration
Student students[ARRAY_SIZE];

// Accessing struct indexes
students[0].name = "First item name";

// we cannot print an entire struct
std::cout << student; // wrong
```

Note: "." operator separate object and it data members.

### C++ Classes

```cpp
class ClassName
{

    // Private access modifier
    private:
    // Private  properties definitions
        float  property;

    // Public access modifier
    public:
        // public members definitions
        ClassName(); // Constructor definition

        // Class object behaviours
        RValueType MethodName(parameters_lists);
};

// Class definition example
class BankAccount
{
    private:
        float balance;
        string type;

    public:
        // Default constructor
        BankAccount();

        void Deposit(float);
        void WithDrawl();
        float GetBalance();
};

// Class behaviours definitionns
BankAccount::BankAccount()
{
    balance = 0;
    type = "UNKNOWN";
}

float BankAccount::GetBalance()
{
    return balance;
}

float BankAccount::Deposit(float value)
{
    balance += value;
    return;
}
```

### C++ Pointers

```cpp
// Pointers declaration
int *p; // The * indicate the pointer that hold the address of the variable it point to

// Declare and initialize a variable
int v1 = 0;
// Pointing pointer to a variable reference
p = &v1;

// Printing the pointer require usage of the * variable

// Update the value of the address p point to
*p = 45;

std::cout << *p; // Print the value of the variable p point to
```

### Linked List

```cpp
struct Node
{
    int data;
    Node *link;
};
Typedef  Nod* nodePtr;

```
