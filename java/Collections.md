# Java collections

The Java collections framework provides a set of interfaces and classes to implement various data structures and algorithms.

Note:
`java. Collections. Collection` is the root interface of the collections framework hierarchy.

Java does not provide direct implementations of the Collection interface but provides implementations of its subinterfaces like List, Set, and Queue.

## Collection interface

```java
public interface Collection<T> {
  public Collection add(int index, T value) // - inserts the specified element to the collection
  public int size(); //  - returns the size of the collection
  public void remove(int index); // - removes the specified element from the collection
  public Iterator<T> iterator()  // - returns an iterator to access elements of the collection
  public Collection|void addAll(); // - adds all the elements of a specified collection to the collection
  public void removeAll(); //- removes all the elements of the specified collection from the collection
  public void clear(); // - removes all the elements of the collection
}
```

### Lists

In Java, the List interface is an ordered collection that allows us to store and access elements sequentially.

```java
public interface List<T> extends Collection<T> {
  public T get(int index); // - helps to randomly access elements from lists

  public List|void set(int index, T value); // - changes elements of lists

  public Array<T> toArray(); // - converts a list into an array

  public boolean contains(); // - returns true if a list contains specified element

  public int indexOf(int index); // Returns index of an element in the list
}
```

```java
// ArrayList implementation of List
List<String> list1 = new ArrayList<>();

// LinkedList implementation of List
List<String> list2 = new LinkedList<>();
```

Examples:

```java
import java.util.List;
import java.util.ArrayList;

class Main {

  public static void main(String[] args) {
      // Creating list using the ArrayList class
      List<Integer> numbers = new ArrayList<>();

      // Add elements to the list
      numbers.add(1);
      numbers.add(2);
      numbers.add(3);
      System.out.println("List: " + numbers);

      // Access element from the list
      int number = numbers.get(2);
      System.out.println("Accessed Element: " + number);

      // Remove element from the list
      int removedNumber = numbers.remove(1);
      System.out.println("Removed Element: " + removedNumber);
}
```

Note:
Both the List interface and the Set interface inherits the Collection interface. However, there exists some difference between them:

* Lists can include duplicate elements. However, sets cannot have duplicate elements.
* Elements in lists are stored in some order. However, elements in sets are stored in groups like sets in mathematics.

#### Array List (Dynamic Arrays)

The ArrayList class of the Java collections framework provides the functionality of resizable-arrays.

* ArrayList vs Array
In Java, we need to declare the size of an array before we can use it. Once the size of an array is declared, it's hard to change it.

#### Vectors

The Vector class is an implementation of the List interface that allows us to create resizable-arrays similar to the ArrayList class.

* Java Vector vs. ArrayList
  + The Vector class synchronizes each individual operation. This means whenever we want to perform some operation on vectors, the Vector class automatically applies a lock to that operation making them less efficient.
  + However, in array lists, methods are not synchronized. Instead, it uses the Collections.synchronizedList() method that synchronizes the list as a whole.

```java
Vector<Type> vector = new Vector<>();
```

#### Stacks (LIFO)

The Java collections framework has a class named Stack that provides the functionality of the stack data structure.

```java
public class Stack<T> extends Vector<T> {

  public void push(T value); // Push an element on the stack

  public T pop(); // Pop and returns the element at the top of the stack and remove element from stack

  public T peek(); // Returns the element at the top of the stack

  public int search(T element); // Locate a position of an element in the stack

  public boolean empty(); // Check if the stack is empty
}
```

```java
Stack<Type> stacks = new Stack<>();
```

Note: Use `ArrayDeque` class which (implements the Deque interface) to implement the stack data structure in Java.

### Java Queue Interface `java.util. Queue`

The Queue interface of the Java collections framework provides the functionality of the queue data structure. It extends Collection interface.

In queues, elements are stored and accessed in First In, First Out manner. That is, elements are added from the behind and removed from the front.

```java

// LinkedList implementation of Queue
Queue<String> animal1 = new LinkedList<>();

// Array implementation of Queue
Queue<String> animal2 = new ArrayDeque<>();

// Priority Queue implementation of Queue
Queue<String> animal 3 = new PriorityQueue<>();
```

```java
public interface Queue<T> extends Collection<T> {

  public boolean add(int index, T value); // - Inserts the specified element into the queue. If the task is successful, add() returns true, if not it throws an exception.
  public boolean offer(); // - Inserts the specified element into the queue. If the task is successful, offer() returns true, if not it returns false.
  public T element() // - Returns the head of the queue. Throws an exception if the queue is empty.
  public T peek(); // - Returns the head of the queue. Returns null if the queue is empty.
  public void remove(); // - Returns and removes the head of the queue. Throws an exception if the queue is empty.
  public ?T poll(); // - Returns and removes the head of the queue. Returns null if the queue is empty.
}
```

* Example

```java
class Main {

    public static void main(String[] args) {
        // Creating Queue using the PriorityQueue class
        Queue<Integer> numbers = new PriorityQueue<>();

        // offer elements to the Queue
        numbers.offer(5);
        numbers.offer(1);
        numbers.offer(2);
        System.out.println("Queue: " + numbers);

        // Access elements of the Queue
        int accessedNumber = numbers.peek();
        System.out.println("Accessed Element: " + accessedNumber);

        // Remove elements from the Queue
        int removedNumber = numbers.poll();
        System.out.println("Removed Element: " + removedNumber);

        System.out.println("Updated Queue: " + numbers);
    }
}
```

#### Java PriorityQueue

The PriorityQueue class provides the functionality of the heap data structure.

Note:
  Unlike normal queues, priority queue elements are retrieved in sorted order.

```java
// Handle PriorityQueue in reverse order
// using a comparator class

import java.util.PriorityQueue;
import java.util.Comparator;
class Main {
    public static void main(String[] args) {

        // Creating a priority queue
        PriorityQueue<Integer> numbers = new PriorityQueue<>(new CustomComparator());
        numbers.add(4);
        numbers.add(2);
        numbers.add(1);
        numbers.add(3);
        System.out.print("PriorityQueue: " + numbers);
    }
}

class CustomComparator implements Comparator<Integer> {

    @Override
    public int compare(Integer number1, Integer number2) {
        int value =  number1.compareTo(number2);
        // elements are sorted in reverse order
        if (value > 0) {
            return -1;
        }
        else if (value < 0) {
            return 1;
        }
        else {
            return 0;
        }
    }
}
```

#### Java Deque Interface

The Deque interface of the Java collections framework provides the functionality of a double-ended queue.

```java

class Deque<T> extends Queue<T> {
  public void addFirst(T value) // - Adds the specified element at the beginning of the deque. Throws an exception if the deque is full.
  public void addLast(T value) // - Adds the specified element at the end of the deque. Throws an exception if the deque is full.
  public void offerFirst(T value) // - Adds the specified element at the beginning of the deque. Returns false if the deque is full.
  public void  offerLast(T value) // - Adds the specified element at the end of the deque. Returns false if the deque is full.
  public T getFirst() // - Returns the first element of the deque. Throws an exception if the deque is empty.
  public T getLast() // - Returns the last element of the deque. Throws an exception if the deque is empty.
  public T peekFirst() // - Returns the first element of the deque. Returns null if the deque is empty.
  public T peekLast() // - Returns the last element of the deque. Returns null if the deque is empty.
  public void removeFirst() //- Returns and removes the first element of the deque. Throws an exception if the deque is empty.
  public void removeLast() // - Returns and removes the last element of the deque. Throws an exception if the deque is empty.
  public T pollFirst() // - Returns and removes the first element of the deque. Returns null if the deque is empty.
  public T pollLast() // - Returns and removes the last element of the deque. Returns null if the deque is empty.
}
```

```java
// Array implementation of Deque
Deque<String> animal1 = new ArrayDeque<>();

// LinkedList implementation of Deque
Deque<String> animal2 = new LinkedList<>();
```

#### Java LinkedList

The LinkedList class of the Java collections framework provides the functionality of the linked list data structure (doubly linkedlist).

```java
LinkedList<Type> linkedList = new LinkedList<>();
```

Note:
  LinkedList as Deque and Queue:

Since the LinkedList class also implements the Queue and the Deque interface, it can implement methods of these interfaces as well.

--- LinkedList Vs. ArrayList

Both the Java ArrayList and LinkedList implements the List interface of the Collections framework. However, there exists some difference between them.

  To iterate over a LinkedList, we can use the for each loop

#### Java ArrayDeque

In Java, we can use the ArrayDeque class to implement queue and deque data structures using arrays.

```java
import java.util.ArrayDeque;

ArrayDeque<Type> animal = new ArrayDeque<>();
```

Note:
  To iterate over elemts we must use the iterator pattern:

```java
ArrayDeque<String> animals= new ArrayDeque<>();
animals.add("Dog");
animals.add("Cat");
animals.add("Horse");

System.out.print("ArrayDeque: ");

// Using iterator()
Iterator<String> iterate = animals.iterator();
while(iterate.hasNext()) {
    System.out.print(iterate.next());
    System.out.print(", ");
}
```

Note:
  To implement a LIFO (Last-In-First-Out) stacks in Java, it is recommended to use a deque over the Stack class.

  LinkedList supports null elements, whereas ArrayDeque doesn't.

  ArrayDeque is likely to faster than a LinkedList.

#### Java BlockingQueue

The BlockingQueue interface of the Java Collections framework extends the Queue interface. It allows any operation to wait until it can be successfully performed.

For example, if we want to delete an element from an empty queue, then the blocking queue allows the delete operation to wait until the queue contains some elements to be deleted.

```java
// Array implementation of BlockingQueue
BlockingQueue<String> animal1 = new ArraryBlockingQueue<>();
```

* Methods that blocks the operation

```java
public interface BloquingQueue<T> extends Queue<T> {

  public void put(T value) // - Inserts an element to the blocking queue. If the queue is full, it will wait until the queue has space to insert an element.

  public T take() //- Removes and returns an element from the blocking queue. If the queue is empty, it will wait until the queue has elements to be deleted.
}
```

* Why BlockingQueues ?
In Java, BlockingQueue is considered as the thread-safe collection. It is because it can be helpful in multi-threading operations.

Now, if the first thread runs slower, then the blocking queue can make the second thread wait until the first thread completes its operation.

#### Java ArrayBlockingQueue `java.util.concurrent. ArrayBlockingQueue`

The ArrayBlockingQueue uses arrays as its internal storage.

It is considered as a thread-safe collection. Hence, it is generally used in multi-threading applications.

```java
ArrayBlockingQueue<Type> animal = new ArrayBlockingQueue<>(int capacity);
```

#### Java LinkedBlockingQueue

The LinkedBlockingQueue class of the Java Collections framework provides the blocking queue implementation using a linked list.

```java
// Here the default initial capacity will be 231-1.
LinkedBlockingQueue<Type> animal = new LinkedBlockingQueue<>();
```

### Maps

In Java, elements of Map are stored in key/value pairs. Keys are unique values associated with individual Values.

Note: Map cannot contains duplicate keys.

-- How to use ?

```java
import java.util.Map;

// Map implementation using HashMap
Map<KeyType, ValueType> numbers = new HashMap<>();
```

-- Interface

```java
public interface Map<K,V> extends Collection<V> {
  public void put(K, V) //- Inserts the association of a key K and a value V into the map. If the key is already present, the new value replaces the old value.
  public void  putAll() // - Inserts all the entries from the specified map to this map.
  public void  putIfAbsent(K, V) // - Inserts the association if the key K is not already associated with the value V.
  public V get(K) //- Returns the value associated with the specified key K. If the key is not found, it returns null.
  public V getOrDefault(K, defaultValue) // - Returns the value associated with the specified key K. If the key is not found, it returns the defaultValue.
  public boolean containsKey(K) // - Checks if the specified key K is present in the map or not.
  public boolean containsValue(V) // - Checks if the specified value V is present in the map or not.
  public void replace(K, V) //- Replace the value of the key K with the new specified value V.
  public void replace(K, oldValue, newValue) //- Replaces the value of the key K with the new value newValue only if the key K is associated with the value oldValue.
  public V remove(K) //- Removes the entry from the map represented by the key K.
  public V  remove(K, V) //- Removes the entry from the map that has key K associated with value V.
  public Set<K> keySet() //- Returns a set of all the keys present in a map.
  public Set<V> values() //- Returns a set of all the values present in a map.
  public Set<K,V> entrySet() // - Returns a set of all the key/value mapping present in a map.
  public void compute() // computes a new value for the specified key
  public void computeIfAbsent(K) // computes value if a mapping for the key is not present
  public void computeIfPresent(K) // computes a value for mapping if the key is present
  public Map<K, V> merge(Map<K,V>) //merges the specified mapping to the HashMap
  public Map<K,V> clone() // makes the copy of the HashMap
  public boolean containsKey() // checks if the specified key is present in Hashmap
  public boolean containsValue() //	checks if Hashmap contains the specified value
  public boolean isEmpty() // checks if the Hashmap is empty
}
```

#### HashMap

The HashMap class of the Java collections framework provides the functionality of the hash table data structure.

```java
// hashMap creation with 8 capacity and 0.6 load factor
HashMap<K, V> numbers = new HashMap<>();
```

-- How to iterate ?

```java
for (Integer key : languages.keySet()) {
  System.out.print(key);
  System.out.print(", ");
}

// iterate through values only
System.out.print("\nValues: ");
for (String value : languages.values()) {
  System.out.print(value);
  System.out.print(", ");
}

// iterate through key/value entries
System.out.print("\nEntries: ");
for (Entry<Integer, String> entry : languages.entrySet()) {
  System.out.print(entry);
  System.out.print(", ");
}
```

Notes:
Note: While creating a hashmap, we can include optional parameters: capacity and load factor. For example, 

```java
HashMap<K, V> numbers = new HashMap<>(8, 0.6f);
```

* 8 (capacity is 8) - This means it can store 8 entries.
* `0.6f (load factor is 0.6) - This means whenever our hash table is filled by 60%, the entries are moved to a new hash table double the size of the original hash table.`
If the optional parameters not used, then the default capacity will be `16` and the default load factor will be `0.75` .

#### Java LinkedHashMap

The LinkedHashMap class of the Java collections framework provides the hash table and linked list implementation of the Map interface.

The LinkedHashMap interface extends the HashMap class to store its entries in a hash table. It internally maintains a doubly-linked list among all of its entries to order its entries.

```java
LinkedHashMap<Key, Value> numbers = new LinkedHashMap<>([capacity, loadFactor, accessOrder]);

// Here, accessOrder is a boolean value. Its default value is false. In this case entries in the linked hashmap are ordered on the basis of their insertion order
```

--- LinkedHashMap Vs. HashMap

* The LinkedHashMap class requires more storage than HashMap. This is because LinkedHashMap maintains linked lists internally
* The performance of LinkedHashMap is slower than HashMap.

#### Java WeakHashMap (implements Map)

The WeakHashMap class of the Java collections framework provides the feature of the hash table data structure.

Note:

Keys of the weak hashmap are of the WeakReference type.

The object of a weak reference type can be garbage collected in Java if the reference is no longer used in the program.

```java
import java.util.WeakHashMap;

//WeakHashMap creation with capacity 8 and load factor 0.6
WeakHashMap<Key, Value> numbers = new WeakHashMap<>(8, 0.6);

```

--- Differences Between HashMap and WeakHashMap

Note: All functionalities of hashmaps and weak hashmaps are similar except keys of a weak hashmap are of weak reference, whereas keys of a hashmap are of strong reference.

#### Java EnumMap (implements Map, Clonable, Serializable)

The EnumMap class of the Java collections framework provides a map implementation for elements of an enum.

In EnumMap, enum elements are used as keys. It implements the Map interface.

```java
import java.util.EnumMap;

enum Size {
    SMALL, MEDIUM, LARGE, EXTRALARGE
}

EnumMap<Size, Integer> sizes = new EnumMap<>(Size.class);
```

-- EnumSet Vs. EnumMap

* Enum set is represented internally as a sequence of bits, whereas the enum map is represented internally as arrays.
* Enum set is created using its predefined methods like allOf(), noneOf(), of(), etc. However, an enum map is created using its constructor.

#### Java SortedMap Interface (implements Map)

The SortedMap interface of the Java collections framework provides sorting of keys stored in a map.

Note : In order to use the functionalities of the SortedMap interface, we need to use the class TreeMap that implements it.

```java
// SortedMap implementation by TreeMap class
SortedMap<Key, Value> numbers = new TreeMap<>();
```

```java
public interface SortedMap<K,V> extends Map<K,V> {
  public Comparator comparator() // - returns a comparator that can be used to order keys in a map
  public K firstKey() // - returns the first key of the sorted map
  public K lastKey() // - returns the last key of the sorted map
  public Map<K,V> headMap(key) // - returns all the entries of a map whose keys are less than the specified key
  public Map<K,V> tailMap(key) //- returns all the entries of a map whose keys are greater than or equal to the specified key
  public Map<K,V> subMap(key1, key2) // - returns all the entries of a map whose keys lies in between key1 and key2 including key1
}
```

#### Java NavigableMap Interface (extends SortedMap)

The NavigableMap interface of the Java collections framework provides the features to navigate among the map entries.

It is considered as a type of SortedMap

Note: In order to use the functionalities of the NavigableMap interface, we need to use the TreeMap class that implements NavigableMap.

```java
// NavigableMap implementation by TreeMap class
NavigableMap<Key, Value> numbers = new TreeMap<>();
```

```java
interface NavigatableMap<K,V> extends SortedMap<K,V> {
  public Map<K,V> headMap(K key, [booleanValue=false]) // method returns all the entries of a navigable map associated with all those keys before the specified key (which is passed as an argument)
  public Map<K,V> tailMap(key, booleanValue) // The tailMap() method returns all the entries of a navigable map associated with all those keys after the specified key (which is passed as an argument) including the entry associated with the specified key

  public Map<K,V> subMap(k1, bv1, k2, bv2) // method returns all the entries associated with keys between k1 and k2 including the entry associated with k1. The bv1 and bv2 are optional parameters. The default value of bv1 is true and the default value of bv2 is false.

  public Map<K,V> descendingMap() // - reverse the order of entries in a map
  public Map<K,V> descendingKeyMap() // - reverses the order of keys in a map
  public V ceilingEntry() // - returns an entry with the lowest key among all those entries whose keys are greater than or equal to the specified key
  public K ceilingKey() // - returns the lowest key among those keys that are greater than or equal to the specified key
  public V floorEntry() // - returns an entry with the highest key among all those entries whose keys are less than or equal to the specified key
  public K floorKey() // - returns the highest key among those keys that are less than or equal to the specified key
  public V higherEntry() //- returns an entry with the lowest key among all those entries whose keys are greater than the specified key
  public K higherKey() // - returns the lowest key among those keys that are greater than the specified key
  public V lowerEntry() // - returns an entry with the highest key among all those entries whose keys are less than the specified key
  public K lowerKey() // - returns the highest key among those keys that are less than the specified key
  public V firstEntry() // - returns the first entry (the entry with the lowest key) of the map
  public V lastEntry() //- returns the last entry (the entry with the highest key) of the map
  public V pollFirstEntry() // - returns and removes the first entry of the map
  public V pollLastEntry() // - returns and removes the last entry of the map
}
```

#### Java TreeMap

The TreeMap class of the Java collections framework provides the tree data structure implementation.

--- TreeMap Comparator

```java
public static class TreeComparator implements Comparator<String> {

    @Override
    public int compare(String o1, String o2) {
        int result = o1.compareTo(o2);
        return (int)(result > 0 ? -1 : (result < 0 ? 1 : 0));
    }
}
```

#### Java ConcurrentMap Interface

The ConcurrentMap interface of the Java collections framework provides a thread-safe map. That is, multiple threads can access the map at once without affecting the consistency of entries in a map.

In order to use the functionalities of the ConcurrentMap interface, we need to use the class ConcurrentHashMap that implements it.

```java
import java.util.concurrent.ConcurrentMap;

// ConcurrentMap implementation by ConcurrentHashMap
CocurrentMap<Key, Value> numbers = new ConcurrentHashMap<>();
```

```java
public interface ConcurentMap extends Map {
  public void forEach(parallelismThreshold, transformer) // Access all entries of a map and perform the specified actions.
  // parallelismThreshold: after how many elements operations in a map are executed in parallel.

  search([parallelThreshold], lambda) // method searches the map based on the specified function and returns the matched entry.
  
  reduce([parallelThreshold], mapFunc, lambda) // The reduce() method accumulates (gather together) each entry in a map. This can be used when we need all the entries to perform a common task, like adding all the values of a map.
  // mapFunc -> is a transformer function. It transfers the key/value mappings into values only.
```

#### Java ConcurrentHashMap

* Bulk ConcurrentHashMap Operations

The ConcurrentHashMap class provides different bulk operations that can be applied safely to concurrent maps.

```java
// forEach
new ConcurrentHashMap<String, Integer>().forEach(4, (k, v) -> System.out.println("key: " + k + " value: " + v));

// reduce
int sum = numbers.reduce(4, (k, v) -> v, (v1, v2) -> v1 + v2);
```

--- ConcurrentHashMap vs HashMap

* ConcurrentHashMap is a thread-safe collection. That is, multiple threads can access and modify it at the same time.
* ConcurrentHashMap provides methods for bulk operations like forEach(), search() and reduce().

--- WHy Concurent Map

* It provides its own synchronization.
* By default, the concurrent hashmap is divided into 16 segments. This is the reason why 16 threads are allowed to concurrently modify the map at the same time. However, any number of threads can access the map at a time.

### Java Sets interfaces (extends Collection)

The Set interface of the Java Collections framework provides the features of the mathematical set in Java. It extends the Collection interface.

```java
import java.util.Set;

// Set implementation using HashSet
Set<String> animals = new HashSet<>();

```

```java
public interface Set<T> extends Collection<T> {
  public void|Set<T> add() // - adds the specified element to the set
  public void|Set<T>  addAll(Set<T>) //- adds all the elements of the specified collection to the set
  public Iterator<T> iterator() // - returns an iterator that can be used to access elements of the set sequentially
  public void remove(index) // - removes the specified element from the set
  public void removeAll() // - removes all the elements from the set that is present in another specified set
  public ? retainAll() // - retains all the elements in the set that are also present in another specified set (For intersection )
  public void clear() // - removes all the elements from the set
  public int size() // - returns the length (number of elements) of the set
  public T[] toArray() // - returns an array containing all the elements of the set
  public boolean contains() // - returns true if the set contains the specified element
  public boolean containsAll() // - returns true if the set contains all the elements of the specified collection
  public ? hashCode() // - returns a hash code value (address of the element in the set)
}
```

#### HashSet

The HashSet class of the Java Collections framework provides the functionalities of the hash table data structure.

```java
import java.util.HashSet;
import java.util.Set;

// HashSet with 8 capacity and 0.75 load factor
Set<Integer> numbers = new HashSet<>(8, 0.75);
```

Note: HashSet is not synchronized. That is if multiple threads access the hash set at the same time and one of the threads modifies the hash set. Then it must be externally synchronized

#### Java EnumSet (implements Set<T>, Clonable, Serializable)

The EnumSet class of the Java collections framework provides a set implementation of elements of a single enum.

* allOf(enum)

```java
import java.util.EnumSet;

class Main {
    // an enum named Size
    enum Size {
        SMALL, MEDIUM, LARGE, EXTRALARGE
    }
    
    public static void main(String[] args) {
        // Creating an EnumSet using allOf()
        EnumSet<Size> sizes = EnumSet.allOf(Size.class);

        System.out.println("EnumSet: " + sizes);
    }

}
```

* range(enum, enum)
The range() method creates an enum set containing all the values of an enum between e1 and e2 including both values.

```java
import java.util.EnumSet;

class Main {

    enum Size {
        SMALL, MEDIUM, LARGE, EXTRALARGE
    }

    public static void main(String[] args) {
        // Creating an EnumSet using range()
        EnumSet<Size> sizes = EnumSet.range(Size.MEDIUM, Size.EXTRALARGE);
        System.out.println("EnumSet: " + sizes);
    }
}
```

* of(enum)
The of() method creates an enum set containing the specified elements.

```java
import java.util.EnumSet;

class Main {

    enum Size {
        SMALL, MEDIUM, LARGE, EXTRALARGE
    }

    public static void main(String[] args) {
        // Using of() with a single parameter
        EnumSet<Size> sizes1 = EnumSet.of(Size.MEDIUM);
        System.out.println("EnumSet1: " + sizes1);
        EnumSet<Size> sizes2 = EnumSet.of(Size.SMALL, Size.LARGE);
        System.out.println("EnumSet2: " + sizes2);
    }
}
```

--- Why EnumSet?
The EnumSet provides an efficient way to store enum values than other set implementations (like HashSet, TreeSet).

This is the reason why enum sets are internally implemented as a sequence of bits. Bits specifies whether elements are present in the enum set or not.

#### Java SortedSet Interface (extends Set<T>)

The SortedSet interface of the Java Collections framework is used to store elements with some order in a set.

```java
import java.util.SortedSet;
import java.util.TreeSet;

// SortedSet implementation by TreeSet class
SortedSet<String> animals = new TreeSet<>();

```

```java
public interface SortedSet<T> extends Set<T> {
  public Comparator comparator() // - returns a comparator that can be used to order elements in the set
  public T first() // - returns the first element of the set
  public T last()  // - returns the last element of the set
  public Set<T> headSet(element) - // returns all the elements of the set before the specified element
  public Set<T> tailSet(element) // - returns all the elements of the set after the specified element including the specified element
  public Set<T> subSet(element1, element2) // - returns all the elements between the element1 and element2 including element1
}
```

#### Java NavigableSet Interface (extends SortedSet<T>)

The NavigableSet interface of the Java Collections framework provides the features to navigate among the set elements.

```java
import java.util.NavigableSet;

// SortedSet implementation by TreeSet class
NavigableSet<String> numbers = new TreeSet<>();
```

```java
interface NavigableSet<T> extends SortedSet<T> {

  public Set<T> headSet(T element, [booleanValue=false]) // method returns all the entries of a navigable Set associated with all those keys before the specified key (which is passed as an argument)
  public Set<T> tailSet(T element, booleanValue) // The tailSet() method returns all the entries of a navigable Set associated with all those keys after the specified key (which is passed as an argument) including the entry associated with the specified key

  public Set<T> subSet(k1, bv1, k2, bv2) // method returns all the entries associated with keys between k1 and k2 including the entry associated with k1. The bv1 and bv2 are optional parameters. The default value of bv1 is true and the default value of bv2 is false.

  public public Set<T> descendingSet() //- reverses the order of elements in a set
  public Iterator<T> descendingIterator() // - returns an iterator that can be used to iterate over a set in reverse order
  public T ceiling() // - returns the lowest element among those elements that are greater than or equal to the specified element
  public T floor() // - returns the greatest element among those elements that are less than or equal to the specified element
  public T higher() // - returns the lowest element among those elements that are greater than the specified element
  public T lower() // - returns the greatest element among those elements that are less than the specified element
  public T pollFirst() // - returns and removes the first element from the set
  public T pollLast() // - returns and removes the last element from the set
}
```

#### Java TreeSet (implements NavigableSet<T>)

```java
TreeSet<Integer> numbers = new TreeSet<>();
```

--- TreeSet Vs. HashSet

* Unlike HashSet, elements in TreeSet are stored in some order. It is because TreeSet implements the SortedSet interface as well.
* TreeSet provides some methods for easy navigation. For example, first(), last(), headSet(), tailSet(), etc. It is because TreeSet also implements the NavigableSet interface.
* HashSet is faster than the TreeSet for basic operations like add, remove, contains and size.

### Java Algorithms ( `java.util. Collections` )

The Java collections framework provides various algorithms that can be used to manipulate elements stored in data structures.

Algorithms in Java are static methods that can be used to perform various operations on collections.

* Sorting

```java

import java.util.ArrayList;
import java.util.Collections;

// Using the sort() method
Collections.sort(new ArrayList<>());
```

* Shuffle

```java
import java.util.ArrayList;
import java.util.Collections;

// Using the shuffle() method
Collections.shuffle(new ArrayList<>());
```

* Collections.reverse(<Collection>) - reverses the order of elements
* Collections.fill(<Collection>, value) - replace every element in a collection with the specified value
* Collections.copy(<destCollection>, <sourceCollection>) - creates a copy of elements from the specified source to destination
* Collections.swap(<Collection>, index, index) - swaps the position of two elements in a collection
* Collections.addAll(<Collection>) - adds all the elements of a collection to other collection
* Collections.binarySearch(<Collection>, value)
* Collections.frequency(<Collection>, value) - returns the count of the number of times an element is present in the collection
* Collections.disjoint(<Collection>, <Collection>) - checks if two collections contain some common element
* Collections.min(<Collection>) - Min value in the collection
* Collections.max(<Collection>) - Compute max value in the collection

### Iterators

The Iterator interface of the Java collections framework allows us to access elements of a collection. It has a subinterface ListIterator.

--- Methods

* hasNext() - returns true if there exists an element in the collection
* next() - returns the next element of the collection
* remove() - removes the last element returned by the next()
* forEachRemaining() - performs the specified action for each remaining element of the collection

#### ListIterator (extends Iterator)

* nextIndex() returns the index of the element that the next() method will return
* previous() - returns the previous element of the list
* previousIndex() - returns the index of the element that the previous() method will return
* set() - replaces the element returned by either next() or previous() with the specified element
