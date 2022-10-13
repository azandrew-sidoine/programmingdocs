# Java OOP

## OOP

A class is a blueprint for the object. Before we create an object, we first need to define the class.

Note: By default Java classes properties are public.

```java
class CLASS_NAME {

  // # Class constructor
  // CLASS_NAME() {
  //  
  // }

  //# Properties definitions
  // <TYPE> name [= <VALUE>];

  // #method definitions
  // [MODIFIER] <RETURNTYPE> METHO_NAME(<PARMS>) {
  // Method body
  //}

  // #Static Method 
  // [<MODIFIER>] static <RETURNTYPE> STATIC_METHOD_NAME([<...params>]) {
  // Method body
  // }

}

// Creating an object of the class
CLASS_NAME object = new CLASS_NAME();

// Calling method
object.METHO_NAME();

// Calling static method
CLASS_NAME.STATIC_METHOD_NAME();
```

### Method overloading

In Java, two or more methods may have the same name if they differ in parameters (different number of parameters, different types of parameters, or both). These methods are called overloaded methods.

```php
void func() { ... }
void func(int a) { ... }
float func(double a) { ... }
float func(int a, float b) { ... }
```

### Java constructors

In Java, constructors can be divided into 3 types:

* No-Arg Constructor

```java
class CLASS_NAME {

  // # Class constructor
  // [<ACESS_MODIFIER>] CLASS_NAME() {
  //  
  // }
  
  // ...

}
```

* Parameterized Constructor

```java
class CLASS_NAME {

  // # Class constructor
  // [<ACESS_MODIFIER>] CLASS_NAME(...<PARAMS>) {
  //  
  // }
  
  // ...

}
```

* Default Constructor

Note: A constructor cannot be `abstract` or `static` or `final` .

--- Constructors Overloading

```java
class CLASS_NAME {

  // # Class constructor
  // [<ACESS_MODIFIER>] CLASS_NAME(...<PARAMS>) {
  //  
  // }

  // # Class constructor
  // [<ACESS_MODIFIER>] CLASS_NAME() {
  //  
  // }
  
  // ...

}

class Complex {

    private int a, b;
    // constructor with 2 parameters
    private Complex( int i, int j ){
        this.a = i;
        this.b = j;
    }
    // constructor with single parameter
    private Complex(int i){
        // invokes the constructor with 2 parameters
        this(i, i); 
    }

    // constructor with no parameter
    private Complex(){
        // invokes the constructor with single parameter
        this(0);
    }

    @Override
    public String toString(){
        return this.a + " + " + this.b + "i";
    }
}
```

### Java string

In Java, a string is a sequence of characters represented using `double quotes` .

Note: Java string is not a primitive type, it's an object.

--- Operations

```java
//... 
String greet = "Hello! World";

// or 
String greet = new String("Hello! World");

// Length
greet.length(); // return the total number of character in the string

// Concatenation
String result = greet.concat("Welcome To the App");

// Comparison
boolean equals = greet.equals(otherString);

// Escape character [\]
String string = "Hello! You are All \" Suckers"
```

Note: Java string are immutable, Methods calls on the them creates a copy of the content before performing the operation.

String literal vs new:

When directly providing the value of the string (Java). Hence, the compiler first checks the string pool to see if the string already exists:

  + If the string already exists, the new string is not created. Instead, the new reference, example points to the already existed string (Java).

  + If the string doesn't exist, the new string (Java is created.

--- Methods

* contains() =========> checks whether the string contains a substring
* substring() =========> returns the substring of the string
* join() =========> join the given strings using the delimiter
* replace() =========> replaces the specified old character with the specified new character
* replaceAll() =========> replaces all substrings matching the regex pattern
* replaceFirst() =========> replace the first matching substring
* charAt() =========> returns the character present in the specified location
* getBytes() =========> converts the string to an array of bytes
* indexOf() =========> returns the position of the specified character in the string
* compareTo() =========> compares two strings in the dictionary order
* compareToIgnoreCase() =========> compares two strings ignoring case differences
* trim() =========> removes any leading and trailing whitespaces
* format() =========> returns a formatted string
* split() =========> breaks the string into an array of strings
* toLowerCase() =========> converts the string to lowercase
* toUpperCase() =========> converts the string to uppercase
* valueOf() =========> returns the string representation of the specified argument
* toCharArray() =========> converts the string to a char array
* matches() =========> checks whether the string matches the given regex
* startsWith() =========> checks if the string begins with the given string
* endsWith() =========> checks if the string ends with the given string
* isEmpty() =========> checks whether a string is empty of not
* intern() =========> returns the canonical representation of the string
* contentEquals() =========> checks whether the string is equal to charSequence
* hashCode() =========> returns a hash code for the string
* subSequence() =========> returns a subsequence from the string

### Final keyword

In Java, the `final` keyword is used to denote constants. It can be used with variables, methods, and classes.

Once any entity (variable, method or class) is declared `final` , it can be assigned only once.

-- Methods

In Java, the final method cannot be overridden by the child class. For example.

-- Classes

Final classes cannot be inherited.

### Recursion

In Java, a method that calls itself is known as a recursive method. And, this process is known as recursion.

A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.

```java
static int factorial( int n ) {
    if (n != 0)  // termination condition
        return n * factorial(n-1); // recursive call
    else
        return 1;
}
```

Note:
When a recursive call is made, new storage locations for variables are allocated on the stack. As, each recursive call returns, the old variables and parameters are removed from the stack. Hence, recursion generally uses more memory and is generally slow.

### Instanceof operator

The instanceof operator in Java is used to check whether an object is an instance of a particular class or not.

```java
// Checks if object is instance ClassName
objectName instanceOf className;
```

Note:

The instanceof operator is also used to check whether an object of a class is also an instance of the interface implemented by the class.

## OOP II

### Inheritance

It's a technique that allow developpers to create a new class from an existing one.
It helps creating an `is-a` relashionship.

* Method overriding

Method overriding is a concept that allow or provides the subclass with the ability to redefine methods previously define in the base class.
By convention, we use `@Override` annotation to tell the compiler that it's an override, even though it's not composery.

Note: Java only support single inheritance, as Java does not support multiple inheritance.

Note: To prevent method overriding in Java, use the `final` keyword.

Note: static methods can not be override

* `Super` keyword

`super` is a keyword in java provides a way to access superclass members(attributes, contructor and method).

* Usage of the super keyword:

  + To call methods of the superclass that is overridden in the subclass.
  + To access attributes (fields) of the superclass if both superclass and subclass have attributes with the same name.
  + To explicitly call superclass no-arg (default) or parameterized constructor from the subclass constructor.

```java
class BaseClass {

  BaseClass(int value) {
    // Initializations
  }

  public void performAction() {
    // Code for performing action
  }
}

class SubClass extends BaseClass {

  SubClass() {
    // Calling super class parameterized constructor
    super(0);
    // Class initialization code
  }

  @Override
  public void performAction() {
    // Override the parent class
    // Call to the parent method
    super.performAction();
  }

}
```

### Abstract class and Methods `abstract`

* Classes

The abstract class in Java cannot be instantiated (we cannot create objects of abstract classes).

* Methods

A method that doesn't have its body is known as an abstract method. We use the same `abstract` keyword to create abstract methods.

```java
abstract class AbstractClass {

  // [ Constructor defintion ]

  // Provide members declarations...
  abstract void abstractMethod();

  // Provide member definitions
  void concreteClass() {
    // Method body
  }
}

```

Note: The major use of abstract classes and methods is to achieve abstraction in Java.

Abstraction is an important concept of object-oriented programming that allows us to hide unnecessary details and only show the needed information.

Key points:

* We use the abstract keyword to create abstract classes and methods.
* An abstract method doesn't have any implementation (method body).
* A class containing abstract methods should also be abstract.
* We cannot create objects of an abstract class.
* To implement features of an abstract class, we inherit subclasses from it and create objects of the subclass.
* A subclass must override all abstract methods of an abstract class. However, if the subclass is declared abstract, it's not mandatory to override abstract methods.
* We can access the static attributes and methods of an abstract class using the reference of the abstract class.

### Interfaces

```java
interface Language {
  // Returns the type of the language
  public String type();

  // Returns the version of the laguage
  public String version();
}

// Implementation

class Java implements Language {
  public String type() {
    // Provide implementations for getting type
  }

  public String version() {
    // Implementation for getting version...
  }
}
```

Note:

* Java support multiple implemementation, where the syntax is same as PHP.
* Java interfaces can extends other interfaces just like in PHP.
* All inter

Advantages:

* Similar to abstract classes, interfaces help us to achieve abstraction in Java.

* Interfaces provide specifications that a class (which implements it) must follow.

* Interfaces are also used to achieve multiple inheritance in Java.

* Default methods in interfaces

From Java8, we can now add default method implementation inside an interface.

Also from Java8, Static method where added to interfaces.

```java
interface Language {
  // Returns the type of the language
  public String type();

  // Returns the version of the laguage
  public String version();

  public String author() {
    // Provide definition for the default method
  }

  staticMethod(){
    // ...
  }
}

// Implementation

class Java implements Language {
  public String type() {
    // Provide implementations for getting type
  }

  public String version() {
    // Implementation for getting version...
  }
}

// Calling Static methods on interface
Language.staticMethod();

```

### Polymorphism

It's a concept in OOP that allow an object to take more than one form.
That means, the same entity (method|Operator|Object) can perform #ts operations in #ts scenario.

* Operator overloading

Some operators in Java behave differently with different operands.

Note: Java doesn't support user-defined operator overloading.

* Polymorphic Variables

A variable is called polymorphic if it refers to different values under different conditions.

Object variables (instance variables) represent the behavior of polymorphic variables in Java. It is because object variables of a class can refer to objects of its class as well as objects of its subclasses.

### Java Encapsulation

Encapsulation is one of the key features of object-oriented programming. Encapsulation refers to the bundling of fields and methods inside a single class.

It prevents outer classes from accessing and changing fields and methods of a class. This also helps to achieve data hiding.

## OOP III

### Java Nested and Inner Class

In Java, you can define a class within another class. Such class is known as nested class. For example:

```java
class OuterClass {
    // ...
    class NestedClass {
        // ...
    }
}
```

* Non-Static Nested Class (Inner Class)

A non-static nested class is a class within another class. It has access to members of the enclosing class (outer class).

```java
class CPU {
    double price;
    // nested class
    class Processor{

        // members of nested class
        double cores;
        String manufacturer;

        double getCache(){
            return 4.3;
        }
    }

    // nested protected class
    protected class RAM{

        // members of protected nested class
        double memory;
        String manufacturer;

        double getClockSpeed(){
            return 5.5;
        }
    }
}

public class Main {
    public static void main(String[] args) {

        // create object of Outer class CPU
        CPU cpu = new CPU();

       // create an object of inner class Processor using outer class
        CPU.Processor processor = cpu.new Processor();

        // create an object of inner class RAM using outer class CPU
        CPU.RAM ram = new cpu.RAM();
        System.out.println("Processor Cache = " + processor.getCache());
        System.out.println("Ram Clock speed = " + ram.getClockSpeed());
    }
}
```

Note:

* We can access the members of the outer class by using this keyword.

```java
class Car {
    String carName;
    String carType;

    // assign values using constructor
    public Car(String name, String type) {
        this.carName = name;
        this.carType = type;
    }

    // private method
    private String getCarName() {
        return this.carName;
    }

// inner class
    class Engine {
        String engineType;
        void setEngine() {

           // Accessing the carType property of Car
            if(Car.this.carType.equals("4WD")){

                // Invoking method getCarName() of Car
                if(Car.this.getCarName().equals("Crysler")) {
                    this.engineType = "Smaller";
                } else {
                    this.engineType = "Bigger";
                }

            }else{
                this.engineType = "Bigger";
            }
        }
        String getEngineType(){
            return this.engineType;
        }
    }
}
```

* Static Nested Class

In Java, we can also define a static class inside another class. Such class is known as static nested class. Static nested classes are not called static inner classes.

Note:
Unlike inner class, a static nested class cannot access the member variables of the outer class. It is because the static nested class doesn't require you to create an instance of the outer class.

```java
class MotherBoard {

   // static nested class
   static class USB{
       int usb2 = 2;
       int usb3 = 1;
       int getTotalPorts(){
           return usb2 + usb3;
       }
   }

}
public class Main {
   public static void main(String[] args) {

       // create an object of the static nested class
       // using the name of the outer class
       MotherBoard.USB usb = new MotherBoard.USB();
       System.out.println("Total Ports = " + usb.getTotalPorts());
   }
}
```

Note:

* In Java, only nested classes are allowed to be static.
* In Java, static nested classes are associated with the outer class. This is why static nested classes can only access the class members (static fields and methods) of the outer class.

### Java anonymous classes

In Java, a class can contain another class known as nested class. It's possible to create a nested class without giving any name.

A nested class that doesn't have any name is known as an anonymous class.

An anonymous class must be defined inside another class. Hence, it is also known as an anonymous inner class. Its syntax is:

```java
class OuterClass {

    // defining anonymous class
    object1 = new Type(parameterList) {
         // body of the anonymous class
    };
}
```

```java
class Polygon {
   public void display() {
      System.out.println("Inside the Polygon class");
   }
}

class AnonymousDemo {
   public void createClass() {
      // creation of anonymous class extending class Polygon
      Polygon p1 = new Polygon() {
         public void display() {
            System.out.println("Inside an anonymous class.");
         }
      };
      p1.display();
   }
}

class Main {
   public static void main(String[] args) {
       AnonymousDemo an = new AnonymousDemo();
       an.createClass();
   }
}
```

### Java Singleton Class

In Java, Singleton is a design pattern that ensures that a class can only have one object.

Note:
To create a singleton class, a class must implement the following properties:

* Create a private constructor of the class to restrict object creation outside of the class.
* Create a private attribute of the class type that refers to the single object.
* Create a public static method that allows us to create and access the object we created. Inside the method, we will create a condition that restricts us from creating more than one object.

```java
class Database {

   private static Database db;

   private Database() { 
     // Initialization code ...     
   }

   public static Database getInstance() {

      // create object if it's not already created
      if(db == null) {
         db = new Database();
      }

       // returns the singleton object
       return db;
   }

   public void getConnection() {
       System.out.println("You are now connected to the database.");
   }
}
```
