# C++ : Utilities

## Useful functions

The function in this group requires the `<algorithm>` header. These function must be applied on values or initializer lists.

### std::min, std::max and std::minmax

They return the request value back as result. The can takes a `lambda` as parameter which return a `boolean` result to indicates if first parameter is return or second parameter is returned.

```c++
int main() {
	std::cout << std::min(2011, 2014) << std::endl; // 2011
	std::cout << std::min({3, 1, 2011, 2014, -5}) << std::endl; // -5

	// Using lambda predicate
	std::cout << std::min(-10, -5, [](int a, int b) {
		// the min between a and b
		return std::abs(a) < std::abs(b);
	}) << std::endl;

	// minmax returns the a min and max pair from initializer list oa values
	auto [min, max] = std::min(2011, 2020, 2019); // (2011, 2020)
}
```


### std::midpoint, std::lerp

These function require `<numeric>` header. `std::midpoint(a, b)` calculate the midpoint between a and b.

`std::lerp(a, b, t)` calculate the linear interpolation of two number. It requires `<cmath>` header imports. The return value is `a + t(b - a)`.


### std::cmp_equal, std::cmp_not_equal, std::cmp_less, std::cmp_greater, std::cmp_less_equal, and std::cmp_greater_equal

These functions from the `<utility>` header provides safe comparison of integer values.

### std::move

`std::move` defines in `<utility>` header, implements `move semantics` that allow compiler to move resources (`objects`).

By using `std::move`, the compiler converts the source `arg` to an rvalue reference, `static_cast<std::remove_reference<decltype(arg)>>::type&&>(arg)`.  If the compiler cannot apply move semantic, it fallback to copy semantic.

### std::forward

`std::forward` defined in `<utility>` header, empowers developpers to write function template which can identically foward their arguments. 

*Use cases of `std::forward()` is for factory function (as they must pass argument to internal object unmodified) or constructors*

```c++
tempate<typename T, typename... Args>
T createT(Args&&... args) {
	// Using C++ uniform initialization syntax
	return T(std::forward<Args>(Args)...);
}

struct MyStruct {
	MyStruct(int, double, char) {};
};

int main() {
	int a = createT();
	int b = createT(3);

	auto s = createT("Hello World!");
	auto _struct = createT(1, 3.9, 'a');

	std::vector<int> vect = createT(std::initializer_list({1, 2, 3}));
}
```

**Note** `Args&&...` is an universal reference, or forwarding reference, which is an `rvalue` reference in type deduction context.

### std::to_underlying C++23

`std::to_underlying` convert and enumeration `enum` to it underlying type `Enum`. It requires `type_traits` header.

It is a convenience function for expression `static_cast<std::underlying_type<Enum>::type>(enum)`

### std::swap

`std::swap` function from `<utility>` header allow to easily swap two object. The implementation uses `std::move` utility function.

```c++
template<typename T>
inline swap(T& a, T& b) {
	T tmp(std::move(b))
	b = std::move(a);
	a = std::move(tmp);
}
```

### std::bind, std::bind_front, std::bind_back & std::functions

`std::bind`, `std::bind_front`, and `std::bind_back` enables developper to create new function on the fly, while `std::function` takes temporary function objects and bind them to a variable. Using these function requires `<functional>` header import.

**Note** Most of these functions ends up to be not necessary as `lamda expressions` and `type deduction using auto` can replace them all.

```c++
double division(double a, double b) {
	return a/b;
}

int main() {
	std::function<double(double, double)> func = std::bind(division, 4, 2);
	// Creates a callable wrapper from a callable
	// Bind all arguments from the front of argument list
	std::function<double(double)> func = std::bind_front(division, 2000); // C++23
	// Creates a callable wrapper from a callable
	// Bind all arguments from the back of arguments list
	std::function<double(double)> func = std::bind_back(division, 10);
}
```

**Note** `std::function` is a polymorphic function wrapper. A callable might be a lambda function, function object or a function. `std::function` is always necessary and can't be replaced with `auto`.

### std::pair

`std::pair` requires `<utility>` header import. And the creates a pair of arbitrary pair.

**Note** `std::map` and it conterparts are implemented using the pair implementation.

**Note** Pairs support the comparison operators like `==`, `!=`, `<` , `>`, `<=` and `=>`.

- `std::make_pair`
  It's use to create a pair of arbitrary pair
  ```c++
  #include <utility>

  int main() {
  	auto [s, num] = std::make_pair("str", 3.14);
  }
  ```

### std::tuple

It allows to create tuple of arbitrary length and types. It requires `<tuple>` header imports.

```c++
#include <tuple>

int main() {
	auto [s, intval, num] = std::make_tuple("Second", 4, 1.1);

	// Get value from tuple using indexes
	int value = std::get<2>(std::make_tuple("second", 3, 8));
}
```


### Reference wrapper

Reference wrappers are copy-constructible and `copy-assignable` wrapper object of ` type&` which is defined in  ``<functional>`` header. They create object that behaves like reference to other object but can be `copied`.

It provides `.get()` method to access the referenced object.

- `strd:ref` & `std::cref`
  They allow developpers to easily create reference wrappers for variables.
  ```c++
  #include <functional>

  void print(const std::string& s) {
  	// Code
  }

  int main() {
  	std::string s{"Color"};

  	// Calling print
  	print(std::cref(s));
  }
  ```

### Smart pointers

Smart pointers are essential to ` C++` because they empower you to implement explicit memory management in  `C++`. Utilities are defines in `<memory>` header file.

Smart pointers manage their resource according to the `RAII` (Resource Acquisition is Initialization), therefore resource is automatically free if the smart pointer goes out of scope.

- `std::unique_ptr`
  It models the concept of exclusif ownership. It cannot be be copied, instead it must be moved.
  ```c++
  #include <memory>

  int main() {
  	std::unique_ptr<int> num(new int(2011));

  	// Creates a unique pointer using make unique
  	std::unique_ptr<int> num = std::make_unique(2014);

  	// Copy semantic
  	std::unique_ptr<int> num2 = num; // Compile Error
  	// Move semantic
  	std::unique_ptr<int> num3 = std::move(num); // OK

  	// Get the pointer to the resource
  	int* int_ptr = num.get(); // 0x249783

  	// Get and Release the pointer to the resource
  	int* int_ptr_2 = num.release();

  	// Reset the resource
  	num.reset();
  }
  ```
- `std::shared_ptr`
  In contrast to `std::unique_ptr`, `std::shared_ptr` models the concepts of shared ownership. It has a reference count for the shared variable, and delete the object if the reference count is 0.
  Shared pointer support copy semantic an any copy of the resource increases the reference counter.
  ```c++
  #include <memory>

  class MyInt {
  private:
  	int value;
  public:
  	MyInt(int v): value(v) {}
  };

  class SharedClass : public std::enable_shared_from_this<SharedClas>{
  	// Creates a shared pointer of the current object
  	std::shared_ptr<SharedClas> getShared(){ 
  		return shared_from_this();
  	} 
  };


  int main() {
  	auto shr_int = std::make_shared(1998);

  	// Get the reference count
  	std::cout << shr_int.use_count() << std::endl;

  	// Local
  	{
  		std::shared_ptr local_shr(shr_int); // Copy semantic
  	}
  }
  ```
- `std:weak_ptr`
  it models the concept of temporary ownership. It does not modify the reference counter. `std::weak_ptr` is not a smart pointer. `std::weak_ptr` supports no transparent access to the resource because it only borrows the ressource from a `std::shared_ptr`.
  ```c++
  #include <memory>

  int main() {
  	auto shared_ptr = std::make_shared(2021);

  	// Creates a weak pointer
  	std::weak_ptr<int> weak_ptr(shared_ptr); // Does not increment the shared pointer reference counter

  	// .lock() : creates a shared pointer from a weak pointer
  	if (std::shared_ptr<int> shared_ptr_1 = weak_ptr.lock()) {
  	}

  	// Check if resource is deleted
  	weak_ptr.expired(); // False
  }
  ```

## Type Traits

Type traits utility library enables you to check, compare, and modify types at compile time.

**Note** There are 2 main reason for using `<type_traits>` library in source code: `Correctness` (requirements for code to run are checked at compile time) and `Optimization`.

```c++
template<typename T>
T fact(T a) {
	static_assert(std::is_integral<T>::value, "T must be an integral");
	// Code
}

int main() {
	fact(10); // OK
	fact(10.3); // Compile Error
}
```


### Check type information

All function below has a `::value` attribute which the result of the evaluation.

```c++
template <class T> struct is_void;
template <class T> struct is_integral;
template <class T> struct is_floating_point; 
template <class T> struct is_array;
template <class T> struct is_pointer;
template <class T> struct is_null_pointer;
template <class T> struct is_member_object_pointer;
template <class T> struct is_member_function_pointer; template <class T> struct is_enum;
template <class T> struct is_union;
template <class T> struct is_class;
template <class T> struct is_function;
template <class T> struct is_lvalue_reference;
template <class T> struct is_rvalue_reference;
template <class T> struct is_object; // is_arithmetic, is_enum, is_pointer, is_member_pointer
template <class T> struct is_arithmetic; // is_floating_point or is_integral
template <class T> struct is_arithmetic; // is_lvalue_reference or is_rvalue_reference
template <class T> struct is_scalar; // is_arithmetic or is_pointer, or is_null_pointer
```

- Type Properties

  In addition to the primary and composite type categories, there are many type properties.

  ```c++
  template <class T> struct is_const;
  template <class T> struct is_volatile;
  template <class T> struct is_trivial;
  template <class T> struct is_trivially_copyable;
  template <class T> struct is_standard_layout;
  template <class T> struct has_unique_object_represenation;
  template <class T> struct is_empty;
  template <class T> struct is_polymorphic;
  template <class T> struct is_abstract;
  template <class T> struct is_final;
  template <class T> struct is_aggregate;
  template <class T> struct is_implicit_lifetime;
  template <class T> struct is_signed;
  template <class T> struct is_unsigned;
  template <class T> struct is_bounded_array;
  template <class T> struct is_unbounded_array;
  template <class T> struct is_scoped_enum;
  template <class T, class... Args> struct is_constructible;
  template <class T> struct is_default_constructible; 
  template <class T> struct is_copy_constructible;
  template <class T> struct is_move_constructible;
  template <class T, class U> struct is_assignable;
  template <class T> struct is_copy_assignable;
  template <class T> struct is_move_assignable;
  template <class T> struct is_destructible;
  template <class T, class... Args> struct is_trivially_constructible; template <class T> struct is_trivially_default_constructible;
  template <class T> struct is_trivially_copy_constructible;
  template <class T> struct is_trivially_move_constructible;
  template <class T, class U> struct is_trivially_assignable;
  template <class T> struct is_trivially_copy_assignable;
  template <class T> struct is_trivially_move_assignable;
  template <class T> struct is_trivially_destructible;
  template <class T, class... Args> struct is_nothrow_constructible; template <class T> struct is_nothrow_default_constructible; template <class T> struct is_nothrow_copy_constructible;
  template <class T> struct is_nothrow_move_constructible;
  template <class T, class U> struct is_nothrow_assignable;
  template <class T> struct is_nothrow_copy_assignable; 
  template <class T> struct is_nothrow_move_assignable;
  template <class T> struct is_nothrow_destructible; 
  template <class T> struct has_virtual_destructor;
  template <class T> struct is_swappable_with; 
  template <class T> struct is_swappable;
  template <class T> struct is_nothrow_swappable_with;
  template <class T> struct is_nothrow_swappable;
  ```
- Type Relationships

  ```c++
  template <class Base, class Derived> struct is_base_of; // Checks if Derived is derived from base class
  template <class From, class To> struct is_convertible; // If type is convertible to `To`
  template <class From, class To> struct is_nothrow_convertible;  // If type is convertible to `To` without exception
  template <class T, class U> struct is_same; // If U and T are same
  template <class T, class U> struct is_layout_compatible; // T and U are layout compatible
  template <class Base, class Derived> struct is_pointer_interconvertible_base_of; // Check if a type is a pointer-inconvertible
  template <class Fn, class ... ArgTypes> struct is_invocable; // Check if Function os invokable with arguments
  template <class Fn, class ... ArgTypes> struct is_invocable_r; // Check if Function os invokable with arguments
  template <class Fn, class ... ArgTypes> struct is_nothrow_invocable;  // Check if Function os invokable with arguments
  template <class Fn, class ... ArgTypes> struct is_nothrow_invocable_r;  // Check if Function os invokable with arguments
  ```
- Type Modifications

  Type library enables to change types during compile time.

  ```c++
  template <class T> struct remove_const; // Removes constness of on the type
  template <class T> struct remove_volatile; // Removes volatile flag on the type
  template <class T> struct add_const; // Add constness of on the type
  template <class T> struct add_volatile; // Add volatile flag on the type
  template <class T> struct make_signed; // Creates signed type at compile time
  template <class T> struct make_unsigned; // Creates unsigned type at compile time
  template <class T> struct remove_reference; // Remove reference from the type
  template <class T> struct add_lvalue_reference; // Add L value reference to the type
  template <class T> struct add_rvalue_reference; // Add R-value reference to the type
  template <class T> struct remove_pointer; // Remove pointer from the type
  template <class T> struct add_pointer; // Add pointer to the type


  // Useful type for generic programming
  template <class B> struct enable_if; // Conditional function overload or template specialization from overload resolution like `extends` in typescript or java
  template <class B, class T, class F> struct conditional; // Provides you with ternary operator at compile time.
  template <class... T> common_type; // Common of all types
  template <class... T> common_reference;
  template <class... T> basic_common_reference;
  template <class... T> void_t;
  template <class... T> type_identity;
  ```

**Note** The functions `std::conjunction`, `std::disjunction`, and `std::negation` enable the logical combina-tions of the type traits functions. They are variadic templates.

## Time Library
