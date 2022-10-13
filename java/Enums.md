# Java Enumerartion

## Enumeration

n Java, an enum (short for enumeration) is a type that has a fixed set of constant values. We use the enum keyword to declare enums. For example, 

```java
enum Size { 
   SMALL, MEDIUM, LARGE, EXTRALARGE 
}
```

Note: By convention The enum constants are usually represented in uppercase.

* Enum Class in Java

In Java, enum types are considered to be a special type of class. It was introduced with the release of Java 5.

```java
enum Size {
    constant1, constant2, …, constantN;

    // methods and fields	
}

// Example
enum Size {
  SMALL, MEDIUM, LARGE, EXTRALARGE;

  public String getSize() {
    // this will refer to the object SMALL
    switch(this) {
      case SMALL:
        return "small";

      case MEDIUM:
        return "medium";

      case LARGE:
        return "large";

      case EXTRALARGE:
        return "extra large";

      default:
        return null;
      }
   }
}
```

* Methods of Java Enum Class

1. Java Enum ordinal()
The ordinal() method returns the position of an enum constant.

2. Enum compareTo()
The compareTo() method compares the enum constants based on their ordinal value.

3. Enum toString()
The toString() method returns the string representation of the enum constants.

4. Enum name()
The name() method returns the defined name of an enum constant in string form. The returned value from the name() method is final.

5. Java Enum valueOf()
The valueOf() method takes a string and returns an enum constant having the same string name.

6. Enum values()
The values() method returns an array of enum type containing all the enum constants.

* Java enum Constructor

In Java, an enum class may include a constructor like a regular class. These enum constructors are either

* private - accessible within the class
            or

* package-private - accessible within the package

```java
enum Size {

   // enum constants calling the enum constructors 
   SMALL("The size is small."),
   MEDIUM("The size is medium."),
   LARGE("The size is large."),
   EXTRALARGE("The size is extra large.");

   private final String pizzaSize;

   // private enum constructor
   private Size(String pizzaSize) {
      this.pizzaSize = pizzaSize;
   }

   public String getSize() {
      return pizzaSize;
   }
}

class Main {
   public static void main(String[] args) {
      Size size = Size.SMALL;
      System.out.println(size.getSize());
   }
}
```

* Java enum Strings

In Java, we can get the string representation of enum constants using the toString() method or the name() method.

```java
enum Size {
   SMALL, MEDIUM, LARGE, EXTRALARGE
}

class Main {
   public static void main(String[] args) {

      System.out.println("string value of SMALL is " + Size.SMALL.toString());
      System.out.println("string value of MEDIUM is " + Size.MEDIUM.name());

   }
}
```

* Overriding or providing a default string value

```java
enum Size {
   SMALL {
      // overriding toString() for SMALL
      public String toString() {
        return "The size is small.";
      }
   },

   MEDIUM
}
```
