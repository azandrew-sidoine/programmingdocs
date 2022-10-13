# Java Primitives & Operators

## Variables

Location in memory(storage area) holding a value/data can change during program execution.

```java
// <DATATYPE> variableName [= <VALUE>];

int memoryLimit = 1024;
// or
int memoryLimit;
memoryLimit = 1024;
```

### Literals & Types

* Boolean (DataType : boolean)
In Java, boolean literals are used to initialize boolean data types. They can store two values: true and false.

* Byte (Type: byte)

8-bit signed integer having value between -128 and 127.

* Short (Type: short)

16-bit singed integer having value between -32768 and 32767

* Integer (Type: int)

32-bit singed integer having value between -231 to 2^31 - 1.

An integer literal is a numeric value(associated with numbers) without any fractional or exponential part.

There are 4 types of integer literals in Java:

```java
// binary
int binaryNumber = 0b10010;
// octal 
int octalNumber = 027;

// decimal
int decNumber = 34;

// hexadecimal 
int hexNumber = 0x2F; // 0x represents hexadecimal
// binary
int binNumber = 0b10010; // 0b represents binary
```

* Long (Type: long)

32-bit singed integer having value between -2^63 to 2^63 - 1 or -2^64 to 2^64 - 1 for Java8 or Later.

* Floating-point Literals

* Double (Type: double)
    Double Precision floating point value. 64-bit floating-point.

* Float (Type: float)
    Double Precision floating point value. 32-bit floating-point.

A floating-point literal is a numeric literal that has either a fractional form or an exponential form. For example:

```java
double myDouble = 3.4;
float myFloat = 3.4F;

// 3.445*10^2
double myDoubleScientific = 3.445e2;
```

* Character

It's a 16-bit Unicode character. The minimum value of the char data type is `\u0000` (0) and the maximum value of the is `\uffff` .

Character literals are unicode character enclosed inside single quotes. For example:

```java
char letter = 'a';
```

Note: Java treats characters as integral types and the ASCII value.

* Strings

A string literal is a sequence of characters enclosed inside double-quotes. For example:

```java
String str1 = "Java Programming";
```

Note: For Data types, Java have 8 Primitives data types.

### Operators

* Arithmetic `+, -, /, *, %`

* Assignment `=, +=, -=, /=, *=, %=`

* Relational `==, !=, >, <, >=, <=`

* Logical `||, &&, !`

* Unary `++, --, +, -`

* Bitwise `<<, >>, >>>(unsigned Right shift), &, ^`

* Type comparison `a instanceof Type`

* Ternary `<EXPRESSION> ? <RESULT1> : <RESULT2>`
