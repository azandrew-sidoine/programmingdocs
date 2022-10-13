# Parallel and Asynchronous Programming

## Parallel vs Asynchronous

Parallel is a concept of forking multiple tasks to multiple handlers(thread) and join them when the are completed. Here tasks executions are synced.

Note:
    First task to complete is handle first.

Asynchronous : Set task to be executed and do not care about how the start, or complete, but only cares about their end result. Here tasks executions are not synced.

```java

import java.util.*;

class Program {
    public static void Main(String[] args) {

        // Martin Fowler : Stream are collection pipeline

        List<Integer> numbers = Array.asList(1,2,3,4,5,6,7,8,9);

        // #region Imperative ways
        int total = 0;

        for(int e : numbers) {
            if (e % 2 == 0) {
                total += e;
            }
        }
        System.out.println(total);
        // #endregion Imperative ways

        // #region Functional programming using functional composition
        // Create an internal iterator, that we not control using break; or continue;
        System.out.println(
            // Transform list of integer to a Stream of Integers
            numbers.stream()
            .filter(e -> e % 2 == 0) // Retrieve even numbers
            .mapToInt(e -> e * 2)
            .sum()
        );
        // # region Functional programming
    }
}
```

Note:
    Using streams the structure of sequential code looks and feels the same as the structure of concurrent code.

```java
public static use(Stream<Integer> stream) {
    stream
    .parallel() // no op because of sequential below
    .map(Main::transform)
    .sequential() // Sequential execution will take over the parallel
    .forEach(System.out::println);
}
```

Java stream class has methods for working on the stream as well as running the sream in parallel.

```java
interface Stream<T>
{
    // Transformation method on the stream values
    Stream<T> map(MapFunction);

    // Filter out some stream values
    Stream<T> filter(FilterFunction);

    // Execute the callback on each stream item
    void forEach(EachFunction);

    // Impose ordering as wait for previous task result before returning
    // result of the next task
    // Useful when one would like to order the end result of a parallel execution
    // Note: Garanties the imposed order of the source stream
    // Like the toArray() in rxjs
    void forEachOrdered();

    // Runs sequentially as it takes each stream value and reduce it to the
    // Return value from the reducer function
    <RType> reduce<RType>(RType identityValue, (carry, curr) -> ReducerFunction(carry, current));

    // Convert the stream into parallel stream
    ParallelStream<T> parallel();

    // First operator
    ?T findFirst();
}
```

## Streams vs Reactive Stream

> Streams - Sequential vs Parallel
> Reactive Stream - Synchronous vs Asynchronous
    subscribeOn() - Gives no segment
    observeOn() - segments

## Observing Threads

> `Thread.currentThread()` -> Returns the current thread on which the tasks is being performed on.

> Java 5 - ExecutorServices() -> Pool of thread that are internally manage by Java Runtime, using pool service methods.

> Java 7 - Workstealing - fork join pool (FJP)

Note: By default Java 8 uses common forkjoin pool from Java 7,  when calling `parallelStream()` on collection objects.

## How many thread should be create to handle parallel execution ?

* Computation intensive vs I/O Intensive

> Computation intensive - # of Threads <= # of core
> I/O Intensive - May be greater than # of cores ???

Formula:
    #T = (# of cores) / 1 - blocking_factor
    0 <= blocking_factor < 1

* What is the Default Number of thread ?

```java
// Request for available cores on the machine
Sytem.out.println(Runtime.getRuntime().availableProcessors());
System.out.print(ForkJoinPool.commonPool()); // Returns details of the common pool
```

* Configuring number of thread at JVM level

This override the system wide computation parallel pool.

> Djava.util.concurrent.ForkJoinPool.common.parallelism=<VALUE> // Should not be done

* ForkJoinPool

```java
// Running a task in a pool

public static void process(Stream<Integer> stream) throws Execption {
    ForkJoinPool pool = new ForkJoinPool(<POOL_SIZE>);
    pool.submit(() -> stream.forEach(e -> {}));
    // Closing the pool executor service
    pool.shutdown();
    // Wait for tasks to complete
    pool.awaitTermination(10, TimeUnit.SECONDS);
}
```

* How to decide to go parallel

> If running slow tasks
> If has a lot of objects being handled

* When parallel makes no sense

> When dealing with fast running tasks

```java
public static void main(String[] args) {
    Array.asList()
    .stream()
    .filter(person -> person.getAge() > 30)
    .filter(person -> person.getGender() == Gender.FEMALE)
    .map(Person::getName)
    findFirst()
    .orElse("Person not found");
}
```

Note: Parallel may waste a lot of resources therefore, should be use with care.

## Completable Futures (Java Promises)

Completable futures are non-blocking I/O operations execution.

Promises (0 or 1 data):
    thow channels
        data ---->
        error ----> (Treat error as another form of data)
        errors are first class citizens
Reactive Stream (0 or * data)

* Stages
    It's a pipeline of execution. At every stage, we take a previous completable future result and return to the next completable future.

```java
    // ...
    public static int createAsync() {
        SafeThread.Sleep(100);
        System.out.printf("Running createAsync on %s\n", Thread.currentThread());
        return 2;
    }

    // Create a completable future
    public static CompletableFuture<Integer> create() {
        // Force Creating future from another pool
        // return CompletableFuture.supplyAsync(() ->create(), new ForkJoinPool(10);
        return CompletableFuture.supplyAsync(() -> createAsync());
    }

    public static <T> void printAsyncResult(T value) {
        System.out.printf("Running printAsyncResult on %s\n", Thread.currentThread());
        System.out.println(value);
    }

    public static void processCompletableFuture() {
        CompletableFuture<Integer> future = create();
        // Note:
        //
        // Famous or Popular functional interface
        // Supplier<T> -> T get(); // Factories
        // Predicate<T> -> boolean test(T); // filter
        // Function<T, R> R apply(T); // Transformation, Map
        // Consumer<T> void accept(T) - forEach()

        // Note:
        // `get()` -> It's a blocking call that block the main thread
        // Working with completable future
        // consuming value produce by the future
        future.thenAccept(Program::printAsyncResult); // returns CompletableFuture<void>

        // Apply then on a void completable feature
        // Can be used as notification channel for notifying users of
        // successfully completed tasks
        // future.thenRun(() -> System.out.println("Continues to run"));

        // Transform the value of the future
        future.thenApply((state) -> state + 1)
                .thenAccept(Program::printAsyncResult);

        SafeThread.Sleep(3000);
    }
    // ...
```

* Completing a future

> Resolving -> CompletableFuture<T>.complete(T)

* Pipelines

> thenApply(MapFunctionOperator) -> produce a transformed value on each chain.

* Completing the pipeline

> complete(<LASTVALUE>)

* Exception handling

> rejecting - completeExecptionnally(Throwable) // js reject

> handling error - .exceptionally(ErrorHandler)

* Completing on timeout

> Future.complete(<VALUE>, <TIME_VALUE>, TIMEUNIT)

```java
public static CompletableFuture<Integer> createAsync()
{
    var future = CompletableFuture.supplyAsync(() -> 2)
                    .thenApply(state -> state * 2)
                    .exceptionally(error -> handleException(err))
                    .thenRun(state -> {});

    
    // Return 0 when not completed 
    // before the given timeout
    future.completeOnTimeout(0, 2, TimeUnit.SECONDS);

    // or
    // Throws an exception when not completed 
    // before the given timeout
    future.orTimeout(2, TimeUnit.SECONDS);
}
```

### Combine & Compose

> Combine - Take a completable future result and combine it with another completable future.

```java
    public static void CombineAndCompose() {
        // thenCombine(CompletableFuture<T>, CombineFunction) - Combine the result value of multiple future into on output
        create(4).thenCombine(create(5), (value1, value2) -> Arrays.asList(value1, value2))
                .thenAccept(state -> System.out.println(state));

        SafeThread.Sleep(2000);
    }
```

> Composition - thenCompose -> Used when a function returns a CompletableFuture. It's similar to flatMap on streams.

Note: FlatMap in Java is like mergeMap(), switchMap() or flatMap() in RxJs... Where it takes a stream an return a stream (on-to-many).

```java
public static int func2(int number) {
    return number * 2;
}

public static int[] func2(int number) {
    return new int[] {number -1, number + 1};
}

public static void main() {
    // ...

    numbers.stream()
        .map(e -> func1(e))
        .flatMap(e -> Stream.of(func(e)))
        .forEach(e -> {});
}
```
