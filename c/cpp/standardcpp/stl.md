# C++ The Standard Library (Introduction)

The standard Template Library is the part of C++ standard that deals with *Containers* , *Algorithms on Containers* and *Iterators. Various components of the STL are:*

## Non Associative container

- std::vector
  Dynamic resizeable list of items. Used in *95%* of times as default container
- std::array
  Fixed sized container alternative to C-arrays.

Here is a list of most non-associative containers:

*std::list* (for double linked list), *std::forward_list* (for single linked list), *std::deque, std::stack*, *std::queue* (an std::deque adapter), etc...

**Note** There are more non-associative container dedicated to specific cases in STL

## Associative containers

C++ STL provides various associative container that store values using key value pairs. The C++ STL have 8 associatives containers classed in *ordered* (in which keys are ordered [*std::set, std::map, std::multiset and std::multimap*]) and *unordered* (in which keys are not ordered [*std::unordered_set, std::unordered_map, std::unordered_multiset, and std::unordered_multimap*].

**Note** In *95%* of time you will use *std::unordered_map* unless specific cases.


## Iterators

C++ STL *Iterators* glue together Containers and Algorithms. They are created by containers. As generalized pointers, you can use them to iterate forward and backward or jump to an arbitrary position in the container.


## Algorithms

C++ STL provides *100 algorithms* for working with C++ containers. Most container algorithms can be run *sequentially, in parallel, or parallel and vectorized.*

**Note** *Many algorithms can be further customized by callables like functions, function objects, or lambda-functions. The callables provide special criteria for the search or the transformation of elements. They highly increase the power of the algorithm.*

**Note** *The algorithms of the ranges library are lazy, can work directly on the container, and can easily be composed. They extend C++ with functional ideas. Furthermore, most of the classical STL algorithms have ranges pendants, which support projections and provide additional safety guarantees.*

## Text Processing

With strings and regular expressions, C++ has two powerful libraries to process text.

- std::string
  C++ STL type for manipulating strings. C++ strings manage their memory. They are kind of C++ *std::vector `<char>`.*
- std::string_view
  C++ STL type that creates a a non-owning reference to a *std::string.* They are cheap to copy.

## Input and Output

*I/O streams library* is a library, present from the start of C++, that allows communication with the outside world.

*In contrast to the I/O streams library, the filesystem library was added to the C++-Standard with C++17. The library is based on three concepts file, file name, and path. Files can be directories, hard links, symbolic links, or regular files. Paths can be absolute or relative.*

## Multithreading

*C++ gets with the 2011 published C++ standard a multithreading library*. This library has basic building blocks like atomic variables, *threads*, *locks*, and *condition variables.*

**Note** *A new thread in C++ will immediately start its work. It can run in the foreground or background and gets its data by copy or reference. Thanks to the stop token, you can interrupt the improved thread std::jthread.*

- C++ Promises or Futures

  Tasks have much in common with threads. But while a programmer explicitly creates a thread, a task will be implicitly created by the C++ runtime. Tasks are like data channels. The data can be a *value*, an *exception*, or *simply a notification*. The promise puts data into the data channel; the future picks the value up
- C++ & Co-routines

  Coroutines are functions that can suspend and resume their execution while keeping their state. Coroutines are the usual way to write *event-driven applications1*.
