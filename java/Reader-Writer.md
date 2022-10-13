# Java Reader & Writer

## Java Reader Class

The Reader class of the java.io package is an abstract superclass that represents a stream of characters.

```java
import java.io.Reader;

// Creates a Reader
Reader input = new FileReader();
```

```java
public abstract class Reader {
    public boolean ready() // - checks if the reader is ready to be read
    public ? read(char[] array) // - reads the characters from the stream and stores in the specified array
    public ? read(char[] array, int start, int length) // - reads the number of characters equal to length from the stream and stores in the specified array starting from the start
    public ? mark() // - marks the position in the stream up to which data has been read
    public ? reset() // - returns the control to the point in the stream where the mark is set
    public ? skip() // - discards the specified number of characters from the stream
}
```

-- Example:

```java
import java.io.Reader;
import java.io.FileReader;

class Main {
    public static void main(String[] args) {

        // Creates an array of character
        char[] array = new char[100];

        try {
            // Creates a reader using the FileReader
            Reader input = new FileReader("input.txt");

            // Checks if reader is ready 
            System.out.println("Is there data in the stream?  " + input.ready());

            // Reads characters
            input.read(array);
            System.out.println("Data in the stream:");
            System.out.println(array);

            // Closes the reader
            input.close();
        }

        catch(Exception e) {
            e.getStackTrace();
        }
    }
}
```

### BufferedReader

### InputStreamReader

The InputStreamReader class of the java.io package can be used to convert data in bytes into data in characters.

Note: It is also known as a bridge between byte streams and character streams.

```java
// Creates an InputStream
FileInputStream file = new FileInputStream(String path);

// Creates an InputStreamReader
InputStreamReader input = new InputStreamReader(file, [Charset cs]);
```

```java
class extends InputStreamReader extends Reader {
    public String|Charset getEncoding() // Get et the type of encoding that is used to store data in the input stream
}
```

### FileReader

The FileReader class of the java.io package can be used to read data (in characters) from files.

```java
FileReader input = new FileReader(String name);

// File reader that will be linked to the file specified by the object of the file
FileReader input = new FileReader(File fileObj);
```

-- Example

```java
import java.io.FileReader;

class Main {
  public static void main(String[] args) {

    // Creates an array of character
    char[] array = new char[100];

    try {
      // Creates a reader using the FileReader
      FileReader input = new FileReader("input.txt");

      // Reads characters
      input.read(array);
      System.out.println("Data in the file: ");
      System.out.println(array);

      // Closes the reader
      input.close();
    }

    catch(Exception e) {
      e.getStackTrace();
    }
  }
}
```

### Java BufferedReader Class

The BufferedReader class of the java.io package can be used with other readers to read data (in characters) more efficiently.

-- Working of BufferedReader
The BufferedReader maintains an internal buffer of 8192 characters.

During the read operation in BufferedReader, a chunk of characters is read from the disk and stored in the internal buffer. And from the internal buffer characters are read individually.

```java
// Creates a FileReader
FileReader file = new FileReader(String file);

// Creates a BufferedReader
BufferedReader buffer = new BufferedReader(file);
```

-- Example:

```java
import java.io.FileReader;
import java.io.BufferedReader;

public class Main {

  public static void main(String args[]) {

    // Creates an array of characters
    char[] array = new char[100];

    try {
      // Suppose, the input.txt file contains the following text
      // This is a line of text inside the file.
      FileReader file = new FileReader("input.txt");

      // Creates a BufferedReader
      BufferedReader input = new BufferedReader(file);

      // Skips the 5 characters
      input.skip(5);

      // Reads the characters
      input.read(array);

      System.out.println("Data after skipping 5 characters:");
      System.out.println(array);

      // closes the reader
      input.close();
    }

    catch (Exception e) {
      e.getStackTrace();
    }
  }
}
```

### StringReader

The StringReader class of the java.io package can be used to read data (in characters) from strings.

Note: In StringReader, the specified string acts as a source from where characters are read individually.

```java
// Creates a StringReader
StringReader input = new StringReader(String data);
```

--- Example

```java
import java.io.StringReader;

public class Main {
  public static void main(String[] args) {

    String data = "This is the text read from StringReader";
    System.out.println("Original data: " + data);

    // Create a character array
    char[] array = new char[100];

    try {
      // Create a StringReader
      StringReader input = new StringReader(data);

      // Use the skip() method
      input.skip(5);

      //Use the read method
      input.read(array);
      System.out.println("Data after skipping 5 characters:");
      System.out.println(array);

      input.close();
    }

    catch(Exception e) {
      e.getStackTrace();
    }
  }
}
```

## Java Writer Class

The Writer class of the java.io package is an abstract superclass that represents a stream of characters.

```java
// Creates a Writer
Writer output = new FileWriter();
```

```java
public abstract class Writer {
    write(char[] array) // - writes the characters from the specified array to the output stream
    write(String data) // - writes the specified string to the writer
    append(char c) // - inserts the specified character to the current writer
    flush() // - forces to write all the data present in the writer to the corresponding destination
    close() // - closes the writer
}
```

-- Example:

```java
import java.io.FileWriter;
import java.io.Writer;

public class Main {

    public static void main(String args[]) {

        String data = "This is the data in the output file";

        try {
            // Creates a Writer using FileWriter
            Writer output = new FileWriter("output.txt");


            // Writes string to the file
            output.write(data);

            // Closes the writer
            output.close();
        }

        catch (Exception e) {
            e.getStackTrace();
        }
    }
}
```

### BufferedWriter

### OutputStreamWriter

The OutputStreamWriter class of the java.io package can be used to convert data in character form into data in bytes form.

Note: It is also known as a bridge between byte streams and character streams.

```java
// Creates an OutputStream
FileOutputStream file = new FileOutputStream(String path);

// Creates an OutputStreamWriter
OutputStreamWriter output = new OutputStreamWriter(file, [Charset cs]);
```

-- Example:

```java
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;

public class Main {

  public static void main(String args[]) {

    String data = "This is a line of text inside the file.";

    try {
      // Creates a FileOutputStream
      FileOutputStream file = new FileOutputStream("output.txt");

      // Creates an OutputStreamWriter
      OutputStreamWriter output = new OutputStreamWriter(file);

      // Writes string to the file
      output.write(data);

      // Closes the writer
      output.close();
    }

    catch (Exception e) {
      e.getStackTrace();
    }
  }
}

```

* `getEncoding()` Method
The getEncoding() method can be used to get the type of encoding that is used to write data to the output stream. For example,

### FileWriter

The FileWriter class of the java.io package can be used to write data (in characters) to files.

```java
FileWriter output = new FileWriter(String name);

// From File object
FileWriter  input = new FileWriter(File fileObj);
```

--- Example

```java
import java.io.FileWriter;

public class Main {

  public static void main(String args[]) {

    String data = "This is the data in the output file";

    try {
      // Creates a FileWriter
      FileWriter output = new FileWriter("output.txt");

      // Writes the string to the file
      output.write(data);
    
      System.out.println("Character encoding of output1: " + output.getEncoding());

      // Closes the writer
      output.close();
    }

    catch (Exception e) {
      e.getStackTrace();
    }
  }
}
```

### Java BufferedWriter Class

The BufferedWriter class of the java.io package can be used with other writers to write data (in characters) more efficiently.

-- Working of BufferedWriter
The BufferedWriter maintains an internal buffer of 8192 characters.

During the write operation, the characters are written to the internal buffer instead of the disk. Once the buffer is filled or the writer is closed, the whole characters in the buffer are written to the disk.

```java
// Creates a FileWriter
FileWriter file = new FileWriter(String name);

// Creates a BufferedWriter
BufferedWriter buffer = new BufferedWriter(file, [int size]);
```

-- Example

```java
import java.io.FileWriter;
import java.io.BufferedWriter;

public class Main {
  public static void main(String[] args) {

    String data = "This is a demo of the flush method";

    try {
      // Creates a FileWriter
      FileWriter file = new FileWriter(" flush.txt");

      // Creates a BufferedWriter
      BufferedWriter output = new BufferedWriter(file);

      // Writes data to the file
      output.write(data);

      // Flushes data to the destination
      output.flush();
      System.out.println("Data is flushed to the file.");

      output.close();
    }

    catch(Exception e) {
      e.getStackTrace();
    }
  }
```

### StringWriter

The StringWriter class of the java.io package can be used to write data (in characters) to the string buffer.

```java
// Creates a StringWriter
StringWriter output = new StringWriter();
```

-- Example

```java
import java.io.StringWriter;

public class Main {
  public static void main(String[] args) {

    String data = "This is the original data";

    try {
      // Create a StringWriter with default string buffer capacity
      StringWriter output = new StringWriter();

      // Writes data to the string buffer
      output.write(data);

      // Returns the string buffer
      StringBuffer stringBuffer = output.getBuffer();
      System.out.println("StringBuffer: " + stringBuffer);

      // Returns the string buffer in string form
      String string = output.toString();
      System.out.println("String: " + string);

      output.close();
    }

    catch(Exception e) {
      e.getStackTrace();
    }
  }
}
```

### Java PrintWriter Class

The PrintWriter class of the java.io package can be used to write output data in a commonly readable form (text).

-- Working of PrintWriter

Unlike other writers, PrintWriter converts the primitive data (int, float, char, etc.) into the text format. It then writes that formatted data to the writer.

```java
// Creates a FileWriter
FileWriter file = new FileWriter("output.txt");

// Creates a PrintWriter
PrintWriter output = new PrintWriter(file, [boolean autoFlush] [,Charset cs]);
```

-- Example

```java
import java.io.PrintWriter;

class Main {
  public static void main(String[] args) {

    String data = "This is a text inside the file.";

    try {
      PrintWriter output = new PrintWriter("output.txt");

      output.print(data);

      int age = 25;

      output.printf("I am %d years old.", age);
      
      output.close();
    }
    catch(Exception e) {
      e.getStackTrace();
    }
  }
}

```
