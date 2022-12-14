# Java Annotations

Java annotations are metadata (data about data) for our program source code.

> @AnnotationName([elementName = "elementValue", ...])

1. Type annotations

Before Java 8, annotations could be applied to declarations only. Now, type annotations can be used as well. This means that we can place annotations wherever we use a type.

```java
ArrayList list = new @Readonly ArrayList<>();

// Non-null string
@NonNull String str;

// Non null List of string
List<@NonNull String> newList;

// Type casting
String newStr = (@NonNull String) str;
```

2. Types of Annotations

* Predefined annotations

  @Deprecated : `annotation is a marker annotation that indicates the element (class, method, field, etc) is deprecated and has been replaced by a newer element`

  @Override : `annotation specifies that a method of a subclass overrides the method of the superclass with the same method name, return type, and parameter list.`

  @SuppressWarnings : `As the name suggests, the @SuppressWarnings annotation instructs the compiler to suppress warnings that are generated while the program executes.`

  @SafeVarargs : `annotation asserts that the annotated method or constructor does not perform unsafe operations on its varargs (variable number of arguments).`

  @FunctionalInterface: `Java 8 first introduced this @FunctionalInterface annotation. This annotation indicates that the type declaration on which it is used is a functional interface. A functional interface can have only one abstract method.`

* Meta-annotations
  @Retention: `The @Retention annotation specifies the level up to which the annotation will be available. @Retention(RetentionPolicy. SOURCE|RetentionPolicy. CLASS|RetentionPolicy. RUNTIME)`

  @Documented: `To include our annotation in the Javadoc documentation, we use the @Documented annotation.`

  @Target: `We can restrict an annotation to be applied to specific targets using the @Target annotation. @Target(ElementType. ANNOTATION_TYPE|ElementType. CONSTRUCTOR|ElementType. FIELD||ElementType. LOCAL_VARIABLE||ElementType. METHOD|ElementType. PACKAGE|ElementType. PARAMETER|ElementType. TYPE)`

  @Inherited: `However, if we need to inherit an annotation from a superclass to a subclass, we use the @Inherited annotation.`

  @Repeatable: `An annotation that has been marked by @Repeatable can be applied multiple times to the same declaration.`

* Use of Annotations

* Compiler instructions - Annotations can be used for giving instructions to the compiler, detect errors or suppress warnings. The built-in annotations @Deprecated, @Override, @SuppressWarnings are used for these purposes.

* Compile-time instructions - Compile-time instructions provided by these annotations help the software build tools to generate code, XML files and many more.

* Runtime instructions - Some annotations can be defined to give instructions to the program at runtime. These annotations are accessed using Java Reflection.

* Custom Annotations
It is also possible to create our own custom annotations.

```java
[Access Specifier] @interface<AnnotationName> {         
  DataType <Method Name>() [default value];
}
```

```java
@interface MyCustomAnnotation {
  String value() default "default value";
}

class Main {
  @MyCustomAnnotation(value = "programiz")
  public void method1() {
    System.out.println("Test method 1");
  }

  public static void main(String[] args) throws Exception {
    Main obj = new Main();
    obj.method1();
  }
}

```

## Java advance Custom annotations

### Class Annotations

They are annotations that get apply to classes.

* `@Target(ElementType.TYPE|ElementType.METHOD|ElementType.FIELD)`

```java
import java.lan.annotation.ElementType;

@Target({ElementType.TYPE})
public @interface AnnotationClass {
    // Annotation code
}
```

Which Java Type the class must be applied on. It is used to restrict annotation to a class, method or property.

* `@Retention`

Tell Java a which stage of the application lifetime the annotion should be retain (Whether at build time or at runtime).

```java
import java.lan.annotation.ElementType;
import java.lan.annotation.Retention;
import java.lan.annotation.RetentionPolicy;

@Target({ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
// RetentionPolicy.SOURCE -> annotation is remove before Java compiles codes
// RetensionPolicy.CLASS -> annotation is remove after code compilation. annotation is not available at runtime
public @interface AnnotationClass {
    // Annotation code
}
```

* Parameterized Annotation

Parameters of the annotations are defined using method instead of fields.

```java
public @interface MyAnnotation {
  boolean required();
}

// Using the annotation
@MyAnnotation(required=true)
```

**Warning**
Only primitives, `java.lang.String` and `java.lang.Array` types can be used.

-- default value annotation

```java
public @interface MyAnnotation {
  boolean required() default true;
}

// Using the annotation
@MyAnnotation(required=true)
```

**Note**
To get annotation using on a given class, method or field, we use Java reflection API `getAnnotation()`

```java
for (Method method: Person.class.getDeclaredMethods()) {
  if (method.isAnnotationPresent(MyAnnotation.class)) {
    MyAnnotation annotation = method.getAnnotation(MyAnnotation.class);
    // Getting annotation parameters is now easy as:
    // annotation.required();
  }
}
```

```java
@Target()
public @interface AnnotationClass {

}
```
