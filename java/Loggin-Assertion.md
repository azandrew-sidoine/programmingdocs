# Java Loggin & Assertion

## Logging

Java allows us to create and capture log messages and files through the process of logging.

In Java, logging requires frameworks and APIs. Java has a built-in logging framework in the `java.util.logging` package.

We can also use third-party frameworks like [Log4j], [Logback], and many more for logging purposes.

```java
Logger logger = Logger.getLogger("newLoggerName");

// or
Logger logger = Logger.getLogger(MyClass.class.getName());

// Setting logger lever
// logger.setLevel(Level.<LogLevel>);
logger.setLevel(Level.FINE);

// Logging with level
// logger.log(Level.LogLevel, "log message");
logger.log(Level.INFO, "This is INFO log level message");

// Short hand
logger.info( "This is INFO log level message");
logger.warning( "This is WARNING log level message");
```

* Log filters

A filter (if it is present) determines whether the LogRecord should be forwarded or not. As the name suggests, it filters the log messages according to specific criteria.

```java
// set a filter
logger.setFilter(filter);

// get a filter
Filter filter = logger.getFilter();
```

* Builting handlers

* StreamHandler: writes to an OutputStream
* ConsoleHandler : writes to console
* FileHandler: writes to file
* SocketHandler: writes to remote TCP ports
* MemoryHandler: writes to memory

A handler can pass the LogRecord to a filter to again determine whether it can be forwarded to external systems or not.

```java
// logger.addHandler(handler);

// example
Handler handler = new ConsoleHandler();
logger.addHandler(handler);

// Removing a handler
// logger.removeHandler(handler);

// example
Handler handler = new ConsoleHandler();
logger.addHandler(handler);
logger.removeHandler(handler);
```

* Formatters

A handler can also use a Formatter to format the LogRecord object into a string before exporting it to external systems.

```java
// Java SE has two built-in Formatters:
// SimpleFormatter: formats LogRecord to string
// XMLFormatter: formats LogRecord to XML form

// formats to string form
handler.setFormatter(new SimpleFormatter());

// formats to XML form
handler.setFormatter(new XMLFormatter());
```

* LogManager

The LogManager object keeps track of the global logging information. It reads and maintains the logging configuration and the logger instances.

The log manager is a singleton, which means that only one instance of it is instantiated.

To obtain the log manager instance, we use the following code:

```java
LogManager manager = new LogManager();

```

## Assertion

Assertions in Java help to detect bugs by testing code we assume to be true.

> Syntax: assert condition;

* Enabling Assertions

> java -ea:arguments

or

> java -enableassertions:arguments

```java
class Main {
  public static void main(String args[]) {
    String[] weekends = {"Friday", "Saturday", "Sunday"};
    assert weekends.length == 2;
    System.out.println("There are " + weekends.length + "  weekends in a week");
  }
}
```

* Another form of assertion statement

> assert condition : expression; -> `In this form of assertion statement, an expression is passed to the constructor of the AssertionError object.`

```java
class Main {
  public static void main(String args[]) {
    String[] weekends = {"Friday", "Saturday", "Sunday"};
    assert weekends.length==2 : "There are only 2 weekends in a week";
    System.out.println("There are " + weekends.length + "  weekends in a week");
  }
}
```

* Enable assertion in class names

> java -ea Main
