# JAVA LANGUAGE NOTES

```java
class App {
    // All java application starts from the :
    // public static void main(String[] args) { // Statements ... }
    // Declaration

    // Note: All java applications must have only on main() function
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
}
```

## Class definition

```java
class CLASS_NAME {

    //# Properties definitions
    // <TYPE> name [= <VALUE>];

    // #method Definition
    // <ReturnTYpe> METHO_NAME(<PARMS>) {}

}

class Point {
    private double x;
    private double y;

}
```

## Tools

### What is JVM?

JVM (Java Virtual Machine) is an abstract machine that enables your computer to run a Java program.

When you run the Java program, Java compiler first compiles your Java code to bytecode. Then, the JVM translates bytecode into native machine code (set of instructions that a computer's CPU executes directly).

### What is JRE?

JRE (Java Runtime Environment) is a software package that provides Java class libraries, Java Virtual Machine (JVM), and other components that are required to run Java applications.

## Console I/O

* Writing to the console:

```java
// Print line
System.out.println();
// Print value
System.out.print();
// Print with formatting
System.out.printf();
```

* Reading user input using Scanner class

```java
import java.util.Scanner;

// ... other defintions

// Create Scanner
Scanner input = new Scanner(System.in); // or java.util.Scanner input = new java.util.Scanner(System.in);

// Read input
int number = input.nextInt(); // nextLong(), nextFloat(), nextDouble(), next()

// Closing the scanner
scanner.close();
```

## Comments

```java
// Single line comment

/**
 * Multi lines comments
 * /
```
