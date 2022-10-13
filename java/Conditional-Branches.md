# Java Conditional & Branches

## Conditionals

### If...[else if ]... else

```java
if (condition) {
  // codes in if block
}
else {
  // codes in else block
}
// Code after else
```

### Switch

```java
switch (expression) {

  case value1:
    // code
    break;
  
  case value2:
    // code
    break;

    // Case statements ...
  
  default:
    // default statements
  }
```

Note: The Java switch statement only works with:
    - Primitive data types: byte, short, char, and int
    - Enumerated types
    - String Class
    - Wrapper Classes: Character, Byte, Short, and Integer.

## Loops

* For Loop

```java
for (initialExpression; testExpression; updateExpression) {
    // body of the loop
}

class Main {
  public static void main(String[] args) {

    int n = 5;
    // for loop  
    for (int i = 1; i <= n; ++i) {
      System.out.println("Java is fun");
    }
  }
}
```

* For each
The Java for loop has an alternative syntax that makes it easy to iterate through arrays and collections:

```java

// Syntax:
for(dataType item : array) {
    // ...
}

// create an array
int[] numbers = {3, 7, 5, -5};

// iterating through the array 
for (int number: numbers) {
    System.out.println(number);
}
```

* While
Java while loop is used to run a specific code until a certain condition is met.

```java
while (condition) {
    // body of loop

    // Break statement
    // Used to break out of the loop
    if (someCondition) {
        break;
    }

    // Continue statement
    // Used return to the next iteration dropping expression after it
    if (someCondition) {
        continue;
    }
}
```

* do...while

The do...while loop is similar to while loop. However, the body of do...while loop is executed once before the test expression is checked.

```java
do {
    // body of loop
} while(condition)
```
