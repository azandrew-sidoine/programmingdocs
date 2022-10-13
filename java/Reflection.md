# Java Reflection

Require to import:

> java.lang. Class; 
> java.lang.reflect.*; 

In Java, reflection allows us to inspect and manipulate classes, interfaces, constructors, methods, and fields at run time.

There is a class in Java named Class that keeps all the information about objects and classes at runtime. The object of Class can be used to perform reflection.

* Reflection of Java Classes

In order to reflect a Java class, we first need to create an object of `Class` .

There exists three ways to create objects of `Class` :

```java
class Dog {
  // ...
}

// 1) Using forName() method
// create object of Class
// to reflect the Dog class
Class a = Class.forName("Dog");

// 2) Using getClass() method
Dog d1 = new Dog();
// create an object of Class
// to reflect Dog
Class b = d1.getClass();

// 3) Using .class extension
// create an object of Class
// to reflect the Dog class
Class c = Dog.class;
```

* Reflection API

```java
import java.lang.Class;
import java.lang.reflect.*;

// imports ...

// ...

Class reflectedClass = Class.forName('ClassName');

// Get the name of the clss
reflectedClass.getName();

// Get access modifiers of the class
int modifier_ = reflectedClass.getModifiers();

// Modifiers to string
string modifier = Modifier.toString(modifier_);

// Get super class
reflectedClass.getSuperClass();

//

// - Reflecting Fields, Methods, and Constructors
// The package java.lang.reflect provides classes that can be used for manipulating class members.

// Get class declared methods
Method[] methods = reflectedClass.getDeclaredMethods();
for (Method m : methods) {

  // Get method name
  System.out.println("Method Name: " + m.getName());

  // Get method modifiers
  int modifier = m.getModifiers();
  System.out.println("Modifier: " + Modifier.toString(modifier));

  // Get method return type
  System.out.println("Return Types: " + m.getReturnType());
  System.out.println(" ");
}

// Reflecting fields
// Get the field by it name
Field fieldname = reflectedClass.getField("fieldname");
// Set the value of the field
fieldname.set(object, "labrador");

// Get value of the field
String typeValue = (String) fieldname.get(object);
System.out.println("Value: " + typeValue);

// Get field modifiers
int mod = field1.getModifiers();

// convert the modifier to String form
String modifier1 = Modifier.toString(mod);

// Modifiying private field accessibility
// Access the private field color
Field field = obj.getDeclaredField("color");

// Make the field public
field.setAccessible(true);
// Set the value of color
field1.set(object, "brown");

// 3. Reflection of Java Constructor
// Get all constructors of Dog
Constructor[] constructors = obj.getDeclaredConstructors();

for (Constructor c : constructors) {
  // Get the name of constructors
  System.out.println("Constructor Name: " + c.getName());

  // get the access modifier of constructors
  // convert it into string form
  int modifier = c.getModifiers();
  String mod = Modifier.toString(modifier);
  System.out.println("Modifier: " + mod);

  // Get the number of parameters in constructors
  System.out.println("Parameters: " + c.getParameterCount());
  System.out.println("");
}
```
