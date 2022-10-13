# Lambda & Streams

## Side notes : Thread

Thread helps in running task in parallel.

```java
public static void main(String[] args) {
    // Anonymous inner classes
    Thread thread = new Thread(new Runnable() {
        public function void run() {
            // Task to be perform in the other thread
        }
    });

    // Starting the thread
    thread.start();

    // Java 8
    Thread thread1 = new Thread(() -> {
        // Task to be perform in the other thread
    });

    // Starting the thread
    thread1.start();
}
```

## Method reference

Method references are method prefix with `::` when the method is used

```java
numbers.forEach(System.out::println);
```

## Streams

## Streams to List

Coverting abstract stream to concrete types is done using collectors.

```java

import java.util.Stream.Collector.*;

public static void main(String[] args) {

    List<int> numbers = Array.asList(1,2,4, /*... */);

    // Converting stream to list using a list collector
    List<int> evens = numbers.stream()
                            .filter(e -> e % 2 == 0)
                            .collect(toList());

    // Collecting to sets
    Set<int> evens = numbers.stream()
                            .filter(e -> e % 2 == 0)
                            .collect(toSet());

    // Using Map transformation
    Set<int> evens = numbers.stream()
                            .filter(e -> e % 2 == 0)
                            .collect(toMap(
                                e -> {}, // Key generator function,
                                e -> e // Value Generator
                            ));

    // Using groupingBy to group elements
    // And mapping to map the grouped values
    List<Person> result = people.stream()
        .collect(groupingBy(Person::getName, mapping(Person::getAge), toList()));
}
```
