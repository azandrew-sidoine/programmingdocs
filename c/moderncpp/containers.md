# Modern C++ (Containers)

## Linear containers

- std::array

It's a fixed templated array alterative to `std::vector` type. It provides an object oriented way to work with `C` arrays using property and method instead of functions to interact with array (`array.size(), array.empty(), etc...`).
Unlike C arrays, it supports smart iterators (`for auto&& i : array`), and eligible for lambda sort function `std::sort(array.begin(), arrray.end(), [](int a, int b) { /* ... */ } )`

**Note**
`std::array` size must be a `constexpr`:

```cpp
int main()
{
    constexpr int len = 4;
    std::array<int, len> arr{1,2,3,4};
}
```

- Functions

> std::array::data() -> returns the internal C-style arrays
> std::array::size() -> Size of the array
> std::array::empty() -> True if array is empty
> std::array::begin(): std::iterator<T> -> Pointer to the first element of the array
> std::array::end(): std::iterator<T> -> Pointer to the last element of the array
> etc...

- std::forward_list
  std::forward_list is a list container, and the usage is similar to std::list

**Note**
Need to know is that, unlike the implementation of the doubly linked list of std::list, std::forward_list is implemented using a singly linked list. Provides element insertion of O(1) complexity, does not support fast random access (this is also a feature of linked lists), It is also the only container in the standard library container that does not provide the size() method. Has a higher space utilization than std::list when bidirectional iteration is not required.

## Unordered Container

- std::map<T>/std::set<T>
  These elements are internally implemented by red-black trees. The average complexity of inserts and searches is O(log(size)).

**Note**
The elements in the unordered container are not sorted, and the internals is implemented by the Hash table. The average complexity of inserting and searching for elements is O(constant), Significant performance gains can be achieved without concern for the order of the elements inside the container.

- std::unordered_map<T>/std::unordered_multimap<T> & std::unordered_set<T>/std::unordered_multiset<T>

```c++
#include <unordered_map>
#include <map>

int main()
{
    std::unordered_map<int, std:string> u{
        1, "1",
        2, "2",
        3, "3"
    }

    std::map<int, std:string> u{
        1, "1",
        2, "2",
        3, "3"
    }

    // Iterated the same way
    for (const auto& element : u) {
        std::<< "Key: " << element.first() << "Value: " << element.second() << std::endl;
    }
}
```

## Tuples `std::make_tuple<...>()` `<tuple>`

`std::make_tuple<typename ...T>()` allows C++ developpers to create a tuple of values.

**Note**`std::get<n>()`
To query for a value at a given position, we make use of `std::get<n>(tuple)`.

**Note**`std::tie<typename ...T>()`
`std::tie<T>(n)` helps C++ developpers to unpack tuples values.

```c++
#include <tuple>

auto get_student(int id)
{
    if (id == 0)
        return std::make_tuple(3.8, 'A', 'John');
    if (id == 1)
        return std::make_tuple(2.9, 'C', 'Jack');
    if (id == 0)
        return std::make_tuple(1.7, 'D', 'Ive');

    return std::make_tuple(0.0, 'D', "null");
}

int main()
{
    auto student = get_student(0);

    // Query for the first element of the student tuple
    std::cout << std::get<0>(student) << std::endl;

    // Unpacking the students
    double gpa = 0;
    char grade = '';
    std::string name = "";
    std::tie(gpa, grade, name) = get_student(1);
}
```

## Runtime indexing C++17

std::get<> depends on a compile-time constant. To overcome this, C++17 introduced an invariant type to provide type template parameters for variant<>

- std::variant<>
  It's similar to variable types in programing language like Python, Javascript, etc...

```cpp
#include <variant>

template <size_t n, typename... T>
constexpr std::variant<T...> _tuple_index(const std::tuple<T...>& tpl, size_t i) 
{
    if constexpr (n >= sizeof...(T)) 
        throw std::out_of_range(" .");
    if (i == n)
        return std::variant<T...>{ std::in_place_index<n>, std::get<n>(tpl) };

    return _tuple_index<(n < sizeof...(T)-1 ? n+1 : 0)>(tpl, i); 
}
template <typename... T>
constexpr std::variant<T...> tuple_index(const std::tuple<T...>& tpl, size_t i)
{
    return _tuple_index<0>(tpl, i);
}
```

## Merge & Iteration

Another common requirement is to merge two tuples, which can be done with `std::tuple_cat`

```cpp
// Query for the size of a tupe instance
template <typename T>
auto tuple_len(T &tpl) 
{
    return std::tuple_size<T>::value; 
}

int main()
{
    auto new_tuple = std::make_tuple(/*...*/); //
    for(int i = 0; i != tuple_len(new_tuple); ++i)
        // runtime indexing
        // Using a runtime index to access each index of the tuple
        std::cout << tuple_index(new_tuple, i) << std::endl;
}
```
