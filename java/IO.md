# Java I/O Streams

In Java, streams are the sequence of data that are read from the source and written to the destination.

-- Types of Streams

Depending upon the data a stream holds, it can be classified into:

* Byte Stream
    Byte stream is used to read and write a single byte (8 bits) of data.
    All byte stream classes are derived from base abstract classes called `InputStream` and `OutputStream` .

* Character Stream
    Character stream is used to read and write a single character of data.
    All the character stream classes are derived from base abstract classes `Reader` and `Writer` .

## Java InputStream ( `java.io. InputStream` )

It's a Java abstract class that represent an input stream stream of bytes.

```java
// Creates an InputStream
InputStream object1 = new FileInputStream();
```

-- Definition

```java
public interface InputStream {
    // Returns -1 if end of file is reach
    public byte read() // - reads one byte of data from the input stream
    public ? read(byte[] array) // - reads bytes from the stream and stores in the specified array
    public int available() // - returns the number of bytes available in the input stream
    public ? mark(int offset) // - marks the position in the input stream up to which data has been read
    public ? reset() // - returns the control to the point in the stream where the mark was set
    public boolean markSupported() // - checks if the mark() and reset() method is supported in the stream
    public ? skip() //- skips and discards the specified number of bytes from the input stream
    public void close() // - closes the input stream
}
```

Note: `String` class constructor has an overload which helps in creating string from byte array.

Note: Implementations are:

### FileInputStream

The FileInputStream class of the java.io package can be used to read data (in bytes) from files.

```java
// Using the path to file
FileInputStream input = new FileInputStream(stringPath);

// Using an object of the file
FileInputStream input = new FileInputStream(File fileObject);
```

```java
class FileInputStream implements InputStream {
    public void read(byte[] array, int start, int length) // Overloaded provider of the inout stream
}
```

### ByteArrayInputStream ( `java.io. ByteArrayInputStream` )

The ByteArrayInputStream class of the java.io package can be used to read an array of input data (in bytes).

Note: In ByteArrayInputStream, the input stream is created using the array of bytes. It includes an internal array to store data of that particular byte array. It's an in-memory stream.

```java
// Creates a ByteArrayInputStream that reads entire array
ByteArrayInputStream input = new ByteArrayInputStream(byte[] arr);

// Creates a ByteArrayInputStream that reads a portion of array
ByteArrayInputStream input = new ByteArrayInputStream(byte[] arr, int start, int length);
```

Note: Has same methods as FileInputStream

### ObjectInputStream ( `java.io. ObjectInputStream` )

The ObjectInputStream class of the java.io package can be used to read objects that were previously written by ObjectOutputStream.

-- Working of ObjectInputStream

The ObjectInputStream is mainly used to read data written by the ObjectOutputStream.
Basically, the ObjectOutputStream converts Java objects into corresponding streams. This is known as serialization. Those converted streams can be stored in files or transferred through networks.

```java
// Creates a file input stream linked with the specified file
FileInputStream fileStream = new FileInputStream(String file);

// Creates an object input stream using the file input stream
ObjectInputStream objStream = new ObjectInputStream(fileStream);
```

```java
public class implements InputStream {
    public byte read() // - reads a byte of data from the input stream
    public boolean readBoolean() // - reads data in boolean form
    public char readChar() // - reads data in character form
    public int readInt() // - reads data in integer form
    public Object readObject() // - reads the object from the input stream
}
```

## Java OutputStream Class ( `java.io. OutputStream` )

The `OutputStream` class of the java.io package is an abstract superclass that represents an output stream of bytes.

```java
// Creates an OutputStream
OutputStream object = new FileOutputStream();
```

```java
public interface OutputStream {
    public ? write() // - writes the specified byte to the output stream
    public ?void write(byte[] array) // - writes the bytes from the specified array to the output stream
    public void flush() // - forces to write all data present in output stream to the destination
    public void close() // - closes the output stream
}
```

-- Examples:

```java
import java.io.FileOutputStream;
import java.io.OutputStream;

public class Main {

    public static void main(String args[]) {
        String data = "This is a line of text inside the file.";

        try {
            OutputStream out = new FileOutputStream("output.txt");

            // Converts the string into bytes
            byte[] dataBytes = data.getBytes();

            // Writes data to the output stream
            out.write(dataBytes);
            System.out.println("Data is written to the file.");

            // Closes the output stream
            out.close();
        }

        catch (Exception e) {
            e.getStackTrace();
        }
    }
}
```

Note: Implementations are:

### FileOutputStream ( `java.io. FileOutputStream` )

```java
// Including the boolean parameter
FileOutputStream output = new FileOutputStream(String path, [boolean value]);
// boolean value -> If true, open file in (append) a+, else open in w+ mode

// Not including the boolean parameter
FileOutputStream output = new FileOutputStream(String path);
```

```java
public interface FileOutputStream implements OutputStream {
    public ? write(byte[] array, int start, int length) //- writes the number of bytes equal to length to the output stream from an array starting from the position start
}
```

### ByteArrayOutputStream ( `java.io. ByteArrayOutputStream` )

The ByteArrayOutputStream class of the java.io package can be used to write an array of output data (in bytes).

Note: In ByteArrayOutputStream maintains an internal array of bytes to store the data.

```java
// Creates a ByteArrayOutputStream with default size = 32
ByteArrayOutputStream out = new ByteArrayOutputStream();

// Creating a ByteArrayOutputStream with specified size
ByteArrayOutputStream out = new ByteArrayOutputStream(int size);
```

```java
class ByteArrayOutputStream implements OutputStream {
    public ? writeTo(ByteArrayOutputStream out1) // - writes the entire data of the current output stream to the specified output stream

    public byte[] toByteArray() // - returns the array present inside the output stream

    public String toString() // - returns the entire data of the output stream in string form

    public int size() // - returns the size of the array in the output stream
}
```

### ObjectOutputStream ( `java.io. ObjectOutputStream` )

Basically, the ObjectOutputStream encodes Java objects using the class name and object values. And, hence generates corresponding streams. This process is known as serialization.

Note: The ObjectOutputStream class only writes those objects that implement the Serializable interface. This is because objects need to be serialized while writing to the stream.

```java
// Creates a FileOutputStream where objects from ObjectOutputStream are written
FileOutputStream fileStream = new FileOutputStream(String file);

// Creates the ObjectOutputStream
ObjectOutputStream objStream = new ObjectOutputStream(fileStream);
```

```java
public class implements OutputStream {
    public ? write() // - writes a byte of data to the output stream
    public ? writeBoolean() // - writes data in boolean form
    public ? writeChar() // - writes data in character form
    public ? writeInt() // - writes data in integer form
    public ? writeObject() // - writes object to the output stream
}
```

-- Example:

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

class Dog implements Serializable {

    String name;
    String breed;

    public Dog(String name, String breed) {
        this.name = name;
        this.breed = breed;
    }
}

class Main {
    public static void main(String[] args) {

        // Creates an object of Dog class
        Dog dog1 = new Dog("Tyson", "Labrador");

        try {
            FileOutputStream fileOut = new FileOutputStream("file.txt");

            // Creates an ObjectOutputStream
            ObjectOutputStream objOut = new ObjectOutputStream(fileOut);

            // Writes objects to the output stream
            objOut.writeObject(dog1);

            // Reads the object
            FileInputStream fileIn = new FileInputStream("file.txt");
            ObjectInputStream objIn = new ObjectInputStream(fileIn);

            // Reads the objects
            Dog newDog = (Dog) objIn.readObject();

            System.out.println("Dog Name: " + newDog.name);
            System.out.println("Dog Breed: " + newDog.breed);

            objOut.close();
            objIn.close();
        }

        catch (Exception e) {
            e.getStackTrace();
        }
    }
}
```

Note: We can also create the output stream from other subclasses of the OutputStream class.

### Java BufferedInputStream Class (implements InputStream) (`java.io.BufferedInputStream`)

The BufferedInputStream class of the `java.io` package is used with other input streams to read the data (in bytes) more efficiently.

-- Working of BufferedInputStream

The BufferedInputStream maintains an internal buffer of 8192 bytes.

During the read operation in BufferedInputStream, a chunk of bytes is read from the disk and stored in the internal buffer. And from the internal buffer bytes are read individually.

Hence, the number of communication to the disk is reduced. This is why reading bytes is faster using the BufferedInputStream.

```java
// Creates a FileInputStream
FileInputStream file = new FileInputStream(String path);

// Creates a BufferedInputStream
BufferedInputStream buffer = new BufferInputStream(file);
```

### Java BufferedOutputStream Class (implements OutputStream) (`java.io.BufferedOutputStream`)

-- Working of BufferedOutputStream
The BufferedOutputStream maintains an internal buffer of `8192` bytes.

During the write operation, the bytes are written to the internal buffer instead of the disk. Once the buffer is filled or the stream is closed, the whole buffer is written to the disk.

Hence, `the number of communication to the disk is reduced`. This is why writing bytes is faster using BufferedOutputStream.

```java
// Creates a FileOutputStream
FileOutputStream file = new FileOutputStream(String path);

// Creates a BufferedOutputStream
BufferedOutputStream buffer = new BufferOutputStream(file);
```

### Print Stream (extends OutputStream)

The PrintStream class of the java.io package can be used to write output data in commonly readable form (text) instead of bytes.

-- Working of PrintStream
Unlike other output streams, the PrintStream converts the primitive data (integer, character) into the text format instead of bytes. It then writes that formatted data to the output stream.

And also, the PrintStream class does not throw any input/output exception. Instead, we need to use the checkError() method to find any error in it.

Note: The PrintStream class also has a feature of auto flushing. This means it forces the output stream to write all the data to the destination under one of the following conditions:

* if newline character \n is written in the print stream
* if the println() method is invoked
* if an array of bytes is written in the print stream

```java
// Creates a FileOutputStream
FileOutputStream file = new FileOutputStream(String file);

// Creates a PrintStream
PrintStream output = new PrintStream(file, autoFlush);
```

```java
public class PrintStream extends OutputStream {
    public String print() // - prints the specified data to the output stream
    public String println() // - prints the data to the output stream along with a new line character at the end
    public String printf() // - method can be used to print the formatted string.
}
```
