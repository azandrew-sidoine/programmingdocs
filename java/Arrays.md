# Java Arrays

## Arrays

An array is a collection of similar types of data, that have a fixed length.
Java array are zero based indexed.

```java
Type[] array = new Type[size]; // -> Declaration and definition
// or
Type[] array; //  Declaration

// Example
double values = new double[10]; // Memory allocation that hold ten double elements

// Uniform initialization
int[] integers = {12, 4, 5, 2, 5};

// Accessing or modifying item using indexes
// array[index]
integers[0] = 10; // Modify element at first position
System.out.println(integers[4]); // Access element at 5th position

// Length of an array
// It's a property of the array object
// array.length
```

### Multi dimensional

```java
double[][] matrix = new double[10][4]; // Create a 10x4 matrix

//
String[][][] data = new String[4][4][2]; // Creates a 4x4x2 array
// 3D arrays are basically array of 2D arrays.

// Uniform initialization
int[][] a = {
      {1, 2, 3}, 
      {4, 5, 6, 9}, 
      {7}, 
};

// Looping through 2 dimensional array
for (int i = 0; i < a.length; ++i) {
    for(int j = 0; j < a[i].length; ++j) {
        System.out.println(a[i][j]);
    }
}
// or
for (int[] innerArray: a) {
    // second for...each loop access each element inside the row
    for(int data: innerArray) {
        System.out.println(data);
    }
}

```

### Copying arrays

* Using Asssignment (Shallow copy)

It creates a reference copy of the array. If the source is modify, the destination is modify as well.

```java
int [] numbers = {1, 2, 3, 4, 5, 6};
int [] positiveNumbers = numbers;
```

* Using copy method from system class (System.utils. Arrays.arraycopy())

Java provides an Arrays class from the `System.utils.Arrays` package

```java
// System.utils.Arrays.arraycopy(Object src, int srcPos,Object dest, int destPos, int length)
// copying elements from index 2 on n1 array
// copying element to index 1 of n3 array
// 2 elements will be copied
System.arraycopy(n1, 2, n3, 1, 2);
```

* Using copy method from system class (System.utils. Arrays.copyOfRange())

Java provides an Arrays class from the `System.utils.Arrays` package

```java
// Copy 2 elements starting from index 0
System.arraycopy(n1, 0, 2);
```
