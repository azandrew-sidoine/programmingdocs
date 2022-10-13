# Rust Programming Langugae

## Installation & Tools

Rust comes with a shell script for installing the tools required for developpement:

> curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh

**Note**
You will also need a linker, which is a program that Rust uses to join its compiled outputs into one file. It is likely you already have one. If you get linker errors, you should install a C compiler, which will typically include a linker. A C compiler is also useful because some common Rust packages depend on C code and will need a C compiler.

* Rustup
It's a command line tool for managing (updating, uninstalling, etc...) rust.

> rustup doc - Opens a local documentation on your computer

* Rust compiler (rustc)
It's like a C compiler usec in compiling and linking rust source code into an executable

* Rust formatter (rustfmt)
It's a command line tool used in formatting rust source code, for them to be rust standard compliant.

## First rust program

Rust source code must be located in a `.rs` extension file.

```rs
fun main() {
    println!("Hello World!");
}
```

Compiling program is done by:

> rustc main.rs - Here we assume the filename is main.rs

**Note**
    As for C/C++ programming rust program starts from a `main()` function which is the main entry point of the program.

**Note**
    Rust macros:
    using `!` in rust programming language means one is calling a macro. Rust macros don't follow same rules as rust functions.

## Cargo

Cargo is Rust’s build system and package manager. Most Rustaceans use this tool to manage their Rust projects because Cargo handles a lot of tasks for you, such as building your code, downloading the libraries your code depends on, and building those libraries.

> cargo --version # Returns the version of the cargo build
> cargo new <PROJECT_NAME> [--vcs=git|mercurial] # Create a new cargo project
> cargo buil [--release] # Build a rust package. The `release` flag build the package for production (optimized).
> cargo run # Run a rust application. It rebuild the source files if they have changed
> cargo check # This command quickly checks your code to make sure it compiles but doesn’t produce an executable
> cargo update # To update dependencies

**Note**
Git files won’t be generated if you run cargo new within an existing Git repository; you can override this behavior by using cargo new --vcs=git.

* TOML (Cargo.toml)

This file is in the TOML (Tom’s Obvious, Minimal Language) format, which is Cargo’s configuration format.

Cargo expects your source files to live inside the `src` directory. The top-level project directory is just for `README` files, `license` information, `configuration` files, and anything else not related to your code. Using Cargo helps you organize your projects. There’s a place for everything, and everything is in its place.

## Common Programming Concepts

### Variable & Mutability

* Variables

> let <VARIABLE_NAME>[: DatType]

```rs
fn main() {
    let variable = <VALUE>;
}
```

By default Rust Variables are immutable. This way Rust protect variable or code against uncontrolled change in concurrent environment (safe & easy concurrency).

* Mutable variable (`mut` keyword)

In order to make a variable mutable:

```rs
fn main() {
    let mut x = 5;
    println!("Value of x: {}", x);
    // Here we can change x
    x = 10;
    println!("Value of x: {} after update", x);
}
```

* Constants
Like immutable variables, constants are values that are bound to a name and are not allowed to change, but there are a few differences between constants and variables.

-- Constants does not allow `mut` keyword, they are always immutable.
-- Constants must only be set in constant expression
-- By convention name constant in uppercase

* Shadowing

```rs
fn main() {
    let x = 5;
    //This program first binds x to a value of 5. Then it shadows x by repeating let x =, taking the original value and adding 1 so the value of x is then 6
    let x = x + 1;

    {
        // Then, within an inner scope, the third let statement also shadows x, multiplying the previous value by 2 to give x a value of 12
        let x = x * 2;
        println!("The value of x in the inner scope is: {}", x);
    }
    // When that scope is over, the inner shadowing ends and x returns to being 6
    println!("The value of x is: {}", x);
}
```

### Data Types

Every value in Rust is of a certain data type, which tells Rust what kind of data is being specified so it knows how to work with that data.

**Note**
    Keep in mind that Rust is a statically typed language, which means that it must know the types of all variables at compile time.

* Scalar Types

A scalar type represents a single value. Rust has four primary scalar types: integers, floating-point numbers, Booleans, and characters.

-- Integers ()

An integer is a number without a fractional component. Rust use `i` for signed integers and `u` for unsigned integers.

> i8 | i16| i32(default) | i64 | i128 - Respectively signed integer 8-bit, 16-bit 32-bit, 64-bit, 128-bit

> u8 | u16| u32 | u64 | u128 - Respectively unsigned integer 8-bit, 16-bit 32-bit, 64-bit, 128-bit

**Note**
    - Each signed variant can store numbers from -(2n - 1) to 2n - 1 - 1 inclusive
    - Unsigned variants can store numbers from 0 to 2n - 1

Example: Number litteral

Decimal -> 98_222
Hex -> 0xff
Octal -> 0o77
Binary -> 0b1111_0000
Byte (u8 only) -> b'A'

-- Floating points

Rust also has two primitive types for floating-point numbers, which are numbers with decimal points. Rust’s floating-point types are `f32` and `f64`, which are 32 bits and 64 bits in size, respectively. The default type is `f64` because on modern CPUs it’s roughly the same speed as `f32` but is capable of more precision.

Example of arithmetic operations:

```rs
fn main() {
    // addition
    let sum = 5 + 10;

    // subtraction
    let difference = 95.5 - 4.3;

    // multiplication
    let product = 4 * 30;

    // division
    let quotient = 56.7 / 32.2;
    let floored = 2 / 3; // Results in 0

    // remainder
    let remainder = 43 % 5;
}
```

-- Boolean

As in most other programming languages, a Boolean type in Rust has two possible values: `true` and `false`.

Example:

```rs
fn main() {
    let t = true;
    let f: bool = false; // with explicit type annotation
}
```

-- Character Type

Rust’s char type is the language’s most primitive alphabetic type. Here’s some examples of declaring `char` values:

Example:

```rs
fn main() {
    let c = 'z';
    let z: char = 'ℤ';
    let heart_eyed_cat = '😻';
}
```

Rust’s char type is four bytes in size and represents a Unicode Scalar Value, which means it can represent a lot more than just `ASCII`. Accented letters; Chinese, Japanese, and Korean characters; emoji; and zero-width spaces are all valid char values in Rust. Unicode Scalar Values range from U+0000 to `U+D7FF` and `U+E000` to `U+10FFFF` inclusive

* Compound types

Compound types can group multiple values into one type. Rust has two primitive compound types: tuples and arrays.

-- Tuples
A tuple is a general way of grouping together a number of values with a variety of types into one compound type. Tuples have a fixed length: once declared, they cannot grow or shrink in size.

Example:

```rs
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);

    // Reading or decomposing a tuple
    let (x, y, z) = tup;

    println!("Y: {}", y);

    // Tuple are zero based indexed
    println("First: {}", tup.0);
}
```

**Note**
The tuple without any values, (), is a special type that has only one value, also written (). The type is called the unit type and the value is called the unit value. Expressions implicitly return the unit value if they don’t return any other value.

-- Arrays

> let array: [Type; SIZE] = [];
> let array = [FILL; SIZE] # Creates array of size <SIZE> filled with <FILL>. It's similar to array_fill() in PHP.

Unlike a tuple, every element of an array must have the same type. Unlike arrays in some other languages, arrays in Rust have a fixed length.

```rs
fn main() {
    let a = [1, 2, 3, 4, 5];

    let a = [0; 32]; // [0,0,0,0....0]

    let a: [u8; 3] = [128, 170, 1];

    // Accessing index of arrays
    println!("Value at index {}, is {}", 3, a[2]);
}
```

**Note**
    Array in Rust has a fixed length. To work with dynamic length collection, Rust provide in standard library a `vector` type just like C++.
    Just like in other programming languages, arrays are `0-based` indexed.

### Functions

Rust code uses snake case as the conventional style for function and variable names, in which all letters are lowercase and underscores separate words. Here’s a program that contains an example function definition:

```syntax
fn func_name() {
    // bloc defintion
}
```

-- Parameterized functions
We can define functions to have parameters, which are special variables that are part of a function’s signature.

```syntax
fn func_name(param: Type [, param2: Type ...]) {
    // bloc defintion
}
```

Example:

```rs
fn print(x: i32) {
    println!("The value of x is: {}", x);
}
```

Unlike C/C++ Rust doesn’t care where you define your functions, only that they’re defined somewhere.

```rs
// Program entry point
fn main() {
    sum(4, 5);
}

// Sum function defintion
fn sum(a: i32, b:i32) -> i32 {
    a + b
}
```

-- Statement & Expressions

**Note**
Statements are instructions that perform some action and do not return a value. Expressions evaluate to a resulting value.
`Calling a macro is an expression. A new scope block created with curly brackets is an expression`

```rs
fn main() {

    let y = 8; // Statements because it does not return value(s)

    let y = {
        let x = 3
        x + 1 //  Because this line does not ends with a semi colon, it is threated as return value of the {} expression
    }; // This is an expression
}
```

**Note**
    Lines not ending with `;` are expression as the return value.

-- Function return value

Functions can return values to the code that calls them. We don’t name return values, but we must declare their type after an arrow (->). In Rust, the return value of the function is synonymous with the value of the final expression in the block of the body of a function

**Note**
You can return early from a function by using the return keyword and specifying a value, but most functions return the last expression implicitly.

```syntax
fn func_name([...]) -> RType {
    // bloc defintion
}
```

```rs
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {}", x);
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```

### Comments in Rust

All programmers strive to make their code easy to understand, but sometimes extra explanation is warranted.

`//` is used to write simple comments. For doc commenting, it will be look into later.

### Control flows

The ability to run some code depending on if a condition is true, or run some code repeatedly while a condition is true, are basic building blocks in most programming languages.

-- `if` Expression

An if expression allows you to branch your code depending on conditions.

```syntax
fn main() {
    if <BOOL_CONDITION> {
        // Execute code
    }
    // Optional part of the if expression 
    [else if <OTHER_BOOL_CONDITION> {

    }]
    else {
        // Default case
    }
}
```

Example:

```rs
fn main() {
    let number: u8 = 3;

    if number < 5 {
        // Run code
    } else {
        // Default
    }
}
```

**note**
It’s also worth noting that the `condition` in this code must be a `bool`. If the `condition` isn’t a `bool`, we’ll get an error.

-- Using if in a let Statement (Ternary operation)

Because if is an expression, we can use it on the right side of a let statement to assign:

```syntax
// Works because line not ending with `;` in a block returns a value
let a = if <BOOL_CONDITION> { <VALUE> } else { <DEFAULT> };
```

**Note**
When using ternary statement, return types must be the same in both case.

-- Loops

For this task, Rust provides several loops, which will run through the code inside the loop body to the end and then start immediately back at the beginning.

```syntax
fn main() {
    loop {
        // Run task infinitely
    }
}
```

Beaking out of loop:

```syntax
fn main() {
    loop {
        // Run task infinitely
        if <BOOL_CONDITION> {
            break;
        }
    }
}
```

Continuing to the next iteration:

```syntax
fn main() {
    loop {
        // Run task infinitely
        if <BOOL_CONDITION> {
            continue;
        }
    }
}
```

Returning value from a loop

```syntax
fn main() {
    let result = loop {
        // Run task infinitely
        if <BOOL_CONDITION> {
            break <VALUE>;
        }
    }
}
```

Example:

```rs
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {}", result);
}
```

-- Conditional Loops with while

A program will often need to evaluate a condition within a loop. While the condition is true, the loop runs. When the condition ceases to be true, the program calls break, stopping the loop.

```syntax
while <BOOL_CONDITION> {
    // Run loop
}
```

-- Smart list iterator

```syntax
for element in list {
    // Do something with the element
}
```

```rs
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {}", element);
    }
}
```

-- Sequences in rust

```syntax
let seq = (1..4); // [1,2,3,4]

// Reverse sequence
let rev_seq = (1..4).rev(); // [4,3,2,1]
```

```rs
fn main() {
    for number in (1..4).rev() {
        println!("{}!", number);
    }
    println!("LIFTOFF!!!");
}
```
