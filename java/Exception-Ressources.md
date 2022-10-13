# Java Exception & Resources Management

## Java Exceptions

* Java Exception Types

The exception hierarchy also has two branches: RuntimeException and IOException

1. RuntimeException

A runtime exception happens due to a programming error. They are also known as unchecked exceptions.

* Improper use of an API - `IllegalArgumentException`
* Null pointer access (missing the initialization of a variable) - `NullPointerException`
* Out-of-bounds array access - `ArrayIndexOutOfBoundsException`
* Dividing a number by 0 - `ArithmeticException`

2. IOException

An IOException is also known as a checked exception. They are checked by the compiler at the compile-time and the programmer is prompted to handle these exceptions.

Trying to open a file that doesn’t exist results in `FileNotFoundException`

* Java try...catch block

```java
try {
  // code
}
catch(Exception e) {
  // code
}
```

* Java finally block

In Java, the finally block is always executed no matter whether there is an exception or not.

```java
try {
  //code
}
catch (ExceptionType1 e1) { 
  // catch block
}
finally {
  // finally block always executes
}
```

* Java throw and throws keyword

The Java throw keyword is used to explicitly throw a single exception.

```java
class Main {
  public static void divideByZero() {

    // throw an exception
    throw new ArithmeticException("Trying to divide by 0");
  }

  public static void main(String[] args) {
    divideByZero();
  }
}
```

Similarly, the throws keyword is used to declare the type of exceptions that might occur within the method. It is used in the method declaration.

Note: We use the throws keyword in the method declaration to declare the type of exceptions that might occur within it.

```java
accessModifier returnType methodName() throws ExceptionType1, ExceptionType2 … {
  // code
}
```

```java
import java.io.*;

class Main {
  // declareing the type of exception
  public static void findFile() throws IOException {

    // code that may generate IOException
    File newFile = new File("test.txt");
    FileInputStream stream = new FileInputStream(newFile);
  }

  public static void main(String[] args) {
    try {
      findFile();
    }
    catch (IOException e) {
      System.out.println(e);
    }
  }
}
```

* Catching Multiple Exceptions

From Java SE 7 and later, we can now catch more than one type of exception with one catch block using Type Union implementation.

```java
try {
  // code
} catch (ExceptionType1 | Exceptiontype2 ex) { 
  // catch block
}
```

### Java try-with-resources statement

Any object that implements java.lang.AutoCloseable, which includes all objects which implement java.io.Closeable, can be used as a resource.

The try-with-resources statement is a try statement that has one or more resource declarations.

It's like the `with` syntax in C#.

Note:
The try-with-resources statement is also referred to as automatic resource management. This statement automatically closes all the resources at the end of the statement.

```java
try (PrintWriter out = new PrintWriter(new FileWriter("OutputFile.txt")) {
  // use of the resource
}
```

Note: The try-with-resources statement closes all the resources that implement the AutoCloseable interface.

* Retrieving Suppressed Exceptions

In Java 7 and later, the suppressed exceptions can be retrieved by calling the `Throwable.getSuppressed()` method from the exception thrown by the try block.

This method returns an array of all suppressed exceptions. We get the suppressed exceptions in the catch block.

```java
import java.io.*;
import java.util.*;

try (PrintWriter out = new PrintWriter(new FileWriter("OutputFile.txt")) {
  // use of the resource
} catch(IOException e) {
  System.out.println("Thrown exception=>" + e.getMessage());
  Throwable[] suppressedExceptions = e.getSuppressed();
  for (int i=0; i<suppressedExceptions.length; i++) {
    System.out.println("Suppressed exception=>" + suppressedExceptions[i]);
  }
}

// With multiple resources
class Main {
  public static void main(String[] args) throws IOException{
    try (Scanner scanner = new Scanner(new File("testRead.txt")); 
      PrintWriter writer = new PrintWriter(new File("testWrite.txt"))) {
      while (scanner.hasNext()) {
        writer.print(scanner.nextLine());
      }
    }
  }
}
```
