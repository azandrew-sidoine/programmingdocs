# Java Advance Topics

## Scanner class

The Scanner class of the java.util package is used to read input data from different sources like input streams, users, files, etc. Let's take an example.

```java
import java.util.Scanner;

// creates an object of Scanner
Scanner input = new Scanner(System.in);

// takes input from the keyboard
String name = input.nextLine();

// We can use nextInt(), nextFloat(), nextBoolean(), next(), nextByte(), nextDouble(), nextShort(), nextLong()

// read input from the input stream
Scanner sc1 = new Scanner(InputStream input);

// read input from files
Scanner sc2 = new Scanner(File file);

// read input from a string
Scanner sc3 = new Scanner(String str);

// import java.math.BigDecimal;
// import java.math.BigInteger;
// nextBigInteger() - reads the big integer value from the
// nextBigDecimal() - reads the big decimal value from the user
```

## Type casting

-- Definition

The process of converting the value of one data type (int, float, double, etc.) to another data type is known as typecasting.

-- Widening Type Casting (Implicit Type Casting)

In Widening Type Casting, Java automatically converts one data type to another data type.

In the case of Widening Type Casting, the lower data type (having smaller size) is converted into the higher data type (having larger size). Hence there is no loss in data. This is why this type of conversion happens automatically.

```java
// create int type variable
int num = 10;

// convert into double type
double data = num;
```

-- Narrowing Type Casting

In Narrowing Type Casting, we manually convert one data type into another using the parenthesis.

In the case of Narrowing Type Casting, the higher data types (having larger size) are converted into lower data types (having smaller size). Hence there is the loss of data. This is why this type of conversion does not happen automatically.

```java
// Syntax Type value = (Type) expression
double num = 10.99;

// convert into int type
int data = (int)num;

// converts int to string type
String data = String.valueOf(data);

// convert string variable to int
int num = Integer.parseInt(data);
```

### Java autoboxing and unboxing

In autoboxing, the Java compiler automatically converts primitive types into their corresponding wrapper class objects.

```java
int a = 56;

// autoboxing
Integer aObj = a;
```

In unboxing, the Java compiler automatically converts wrapper class objects into their corresponding primitive types. For example:

```java
// autoboxing
Integer aObj = 56;

// unboxing
int a = aObj;
```

## Lambda expressions

The lambda expression was introduced first time in Java 8. Its main objective to increase the expressive power of the language.

-- What is Functional Interface?

If a Java interface contains one and only one abstract method then it is termed as functional interface. This only one method specifies the intended purpose of the interface.

```java
import java.lang.FunctionalInterface;

@FunctionalInterface
public interface ValueInterface{
    // the single abstract method
    double getValue();
}
```

-- Introduction to lambda expressions (-> operator)

Lambda expression is, essentially, an anonymous or unnamed method. The lambda expression does not execute on its own. Instead, it is used to implement a method defined by a functional interface.

--- Definition

> ([parameters]) -> lambda body; 
> ([parameters]) -> { Lambda body }; 

Note: For the block body, you can have a return statement if the body returns a value. However, the expression body does not require a return statement.

```java
import java.lang.FunctionalInterface;

// this is functional interface
@FunctionalInterface
interface MyInterface{

    // abstract method
    double getPiValue();
}

public class Main {

    public static void main( String[] args ) {

    // declare a reference to MyInterface
    MyInterface ref;
    
    // lambda expression
    ref = () -> 3.1415;
    
    System.out.println("Value of Pi = " + ref.getPiValue());
    } 
}
```

-- Generic Lambda

```java
// GenericInterface.java
@FunctionalInterface
interface GenericInterface<T> {

    // generic method
    T call(T t);
}
```

-- Lambda Expression and Stream API

The new `java.util.stream` package has been added to JDK8 which allows java developers to perform operations like search, filter, map, reduce, or manipulate collections like Lists.

```java
import java.util.ArrayList;
import java.util.List;

public class StreamMain {

    // create an object of list using ArrayList
    static List<String> places = new ArrayList<>();

    // preparing our data
    public static List getPlaces(){

        // add places and country to the list
        places.add("Nepal, Kathmandu");
        places.add("Nepal, Pokhara");
        places.add("India, Delhi");
        places.add("USA, New York");
        places.add("Africa, Nigeria");

        return places;
    }

    public static void main( String[] args ) {

        List<String> myPlaces = getPlaces();
        System.out.println("Places from Nepal:");
        
        // Filter places from Nepal
        myPlaces.stream()
                .filter((p) -> p.startsWith("Nepal"))
                .map((p) -> p.toUpperCase())
                .sorted()
                .forEach((p) -> System.out.println(p));
    }

}
```

## Java Generics

The Java Generics allows us to create a single class, interface, and method that can be used with different types of data (objects).

Like Generics in Typescript.

--- Generic methods

```java
class DemoClass {

  // creae a generics method
  public <T> void genericsMethod(T data) {
    System.out.println("Generics Method:");
    System.out.println("Data Passed: " + data);
  }
}
// Calling generic method
demo.<String>genericMethod("Java Programming");
```

--- Bounded types

> <T extends A>

## Java File class

The File class of the `java.io` package is used to perform various operations on files and directories.

There is another package named `java.nio` that can be used to work with files. However, in this tutorial, we will focus on the `java.io` package.

-- File and Directory

```java
import java.io.File;

// Creating a file pointer/reference
// creates an object of File using the path 
// or an abstract representation of a file
File file = new File(String pathName);
```

-- Java File Operation Methods

```java
import java.io.File;

File file = new File(String pathName);

// Create a new file
// returns true if created, or false if file already exists
// trying to create a file based on the object
boolean value = file.createNewFile();
```

--- Reading files

```java
// importing the FileReader class
import java.io.FileReader;

// Creates a reader using the FileReader
FileReader input = new FileReader("input.txt");

byte[] array =  new byte[100]
// Reads characters
input.read(array);

// Close the input
// Closes the reader
input.close();
```

--- Writing to files

```java
// importing the FileWriter class
import java.io.FileWriter;

 class Main {
   public static void main(String args[]) {

     String data = "This is the data in the output file";
     try {
       // Creates a Writer using FileWriter
       FileWriter output = new FileWriter("output.txt");

       // Writes string to the file
       output.write(data);
       System.out.println("Data is written to the file.");

       // Closes the writer
       output.close();
     }
     catch (Exception e) {
       e.getStackTrace();
     }
  }
}
```

--- Deleting files

```java
import java.io.File;

class Main {
  public static void main(String[] args) {

    // creates a file object
    File file = new File("file.txt");

    // deletes the file
    boolean value = file.delete();
    if(value) {
      System.out.println("The File is deleted.");
    }
    else {
      System.out.println("The File is not deleted.");
    }
  }
}
```

## Java Wrapper class

byte =====      Byte
boolean =====   Boolean
char =====      Character
double =====    Double
float =====     Float
int ======      Integer
long =====      Long
short =====     Short

- valueOf()

Wrap a primitive value in a wrapper.

> Integer.valueOf()

- From Wrapper to Primity

> Wrapper.<byte|int|float|double|long|short>Value()