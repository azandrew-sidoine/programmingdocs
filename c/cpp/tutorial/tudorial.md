# C++ Tutorial

## Structures

They allow to define composite type that are build of variables of different data types called members.

```c++
// Here is an example of C++ structure
// This is just a blueprint and no memory is allocated
struct Person {
    char name[50];
    int age;
    float salary;
};
```

**Note** *Always remember ; at the end of structures and class definitions in C++ as it may lead to compilation errors*

- Structures variable definition
  Struct instances or variables are created just like any C++ type:
  ```c++
  Person p;
  // Or with initialization
  Person p{name: "Azandrew", age: 31, salary: 500000};
  ```

    **Note** Struct memory alignment

*
    Struct members must be defines in the order of small sized member to large sized member.*

- Accessing structure members
  Struct members are access using the `.` member access operator.

  ```c++
  // Assignment
  p.age = 32;

  // Getter
  printf("Person age: %d\n", p.age);
  ```
- Accessing structure members by reference

  C++ structures passed by reference elements can also be accessed through the `->` instead of `.` operator.

## Classes & Objects

C++ classes are implementation of Object-Oriented concept which try to defines protocols for solving real world problems by modeling them as object with properties and behaviour, relations between these object and all abstraction applied to them.

```C++
// Just like C++ structs, the ; should not be omitted else it will result in compilation error
class Point {
	// public members declarations
	double getX();
	double getY();

	void move(float dx);
	void move(float dx, float dy);
	// private fields / members
	private:
		float x;
		float y;
};

// Here we provide class methods definition
Point::getX()
{
	return x;
}

Point::getY()
{
	return y;
}

Point::move(float dx)
{
	x += dx;
}

Point::move(float dx, float dy)
{
	x += dx;
	y += dy;
}
```

- Class instances definition
  Class instance are create as any built-in type or struct type instances.

  ```c+=
  Point p;
  ```
- Class data members accessor

  Class data members are access using `.` operator like the way struct members are accessed.

## C++ Class Inheritance

Class inheritance is an OOP concept that allow developper to create new type from existing types. We cannot inherit built-in C++ types, by any user defined type can be ihnerited using `:` operator.

```c++

class Shape {
private:
	char name[100];
public:
	*char getName();
};

class Rectangle : public Shape {
private:
	double width;
	double height;

public:
	double getWidth();
	double getHeight();
};
```

**Note Like** **`private` members,** **`protected` members are inaccessible outside of the class. However, they can be accessed by** ****derived classes** and** ***friend classes/functions*.**

### Access Mode in C++ inheritance

We have used the `public` keyword in order to inherit a class from a previously-existing base class. However, we can also use the **`private` and** `protected `keywords to inherit classes.
Note:

- If `public`, then base class members are inherited as they are.
- Else if `private` all base class members become `private` in derive class.
- If `protected` all base class member becomes protected in derived class definition.

### Accessing base class members

C++ provides developpers with `Base` keyword to access base class member from derived classes or source code outside derive class:

```c++
class Base {
public:
	void print();
};

class Derived ; public Base {
public:
	void print() {
		Base::print();
		std::cout << "Derived: " << std::endl;
	}
};

int main() {
	// From main program we can access base class print
	Derived o;
	o.Base.print();

	// Calling derived class print
	o.print();
}

```

## Operator Overloading

Operator overloading changes the way some operators behave on our user defined type `classes & structs`. Below is the defintion of operator overloading syntax:

```c++
class Point {
public:
	DType operator symbol (arguments) {
		// Provide overload implementation
	}
}
```

- Unary operator overloading *(++, --)*

  ```c++
  ;class Counter {
  private:
  	int value;
  public:
  	// Default constructor
  	Counter() = default;

  	// Prefix ++ operator overloading
  	Counter operator ++ () {
  		Counter c;
  		c.value = ++value;
  		c;
  	}

  	// Postfix operator overloading
  	Counter operator ++(int) {
  		Counter c;
  		c.value = value++;
  		c;
  	}
  };
  ```
- Bynary operator overloading

  Bynary operators oberloading implementation takes an argument.

  ```c++
  class Complex {
  private:
  	double real;
  	double img;
  public:
  	// Compiler default constructor
  	Complex() = default;

  	// + Operatator overloading
  	Complex operator + (const Complex& c) {
  		Complex _c;
  		_c.real = real + c.real;
  		_c.img = img + c.img;
  		return _c;
  	}
  };
  ```

**Note** By default `=` copy assignment operator and `&` operators are overloaded in C++.

There are some operators that can't be overloaded: `::` (scope resolution), `.` (member accessor), `.*` (member selection through pointer), `?:` (trenary operator).


## C++ Abstract class, Virtual Function and Interfaces

**Note** In contrast to other programming language, C++ does not provide interfaces definition, but provides `multiple` inheritance to create `interface` like implementation through absract classes.

- Virtual functions **virtual**
  A `virtual function` is a member function in the base class that we expect to redefine in derived classes. Basically, a `virtual function` is used in the base class in order to ensure that the function is `overridden`.**

```c++
class Base {
public:
	// Should be overridden
	virtual void print();
};

class Derived : public Base {
public:
	void print() {
		// Provide overriden implementation
	}
	// From C++11 we must use override keyword for explicit override
	void print() override {
		// Code...
	}

};
```

## C++ Memory management

*C++ allows us to allocate the memory of a variable or an array in run time. This is known as dynamic memory allocation.*

**Note** *In other programming languages such as Java and Python, the compiler automatically manages the memories allocated to variables. But this is not the case in C++.*

**Warning** *In C++, we need to deallocate the dynamically allocated memory manually after we have no use for the variable.*

- Allocating & Deallocating memory

  ```c++
  int main() {
  	const SIZE = 10;
  	int* memory = new int;

  	// Array memory allocation
  	float* memset = new float[SIZE];

  	// Prevent memory leak
  	delete memory;
  	// Deleting array allocated memory. We use the square brackets [] in order to denote that the memory deallocation is that of an array.
  	delete[] memset;
  }
  ```



## C++ Template

C++ templates are powerful feature to implements generic programming. There a 2 template types:

- Class Templates

  Similar to function templates, we can use class templates to create a single class to work with different data types.

  ```c++
  template <class T>
  class Optional {
  private:
  	T value;

  public:
  	Optional() = default;
  	Optional(T _value): value(_value) {}
  	T getValue();
  	// Boolean flag check if optional instance has a given value
  	bool hasValue();
  };

  template <class T>
  T Optional<T>::getValue() {
  	return value;
  }
  ```

  **Note** In the above declaration, T `is the template argument which is a placeholder for the data type used, and class` is a keyword.

  Usage:

  ```c++
  int main() {
  	Optional<int> intval;
  	return 0;
  }
  ```

  **Note** C++ template support multiple parameters and default type for least template keywords:

  ```c++
  template <class T, class U, class V=int>
  class MyClass {
  	// Provide class definition
  };
  ```
- Function Templates

  A function template starts with the keyword `template` followed by parameters inside `<>`:

  ```c++
  template <typename T>
  T func(T p, T p2, ...) {
  }

  int main() {
  	// Using function template
  	func<int>(1, 3, 5);
  }
  ```

### Template specialization

Templates Specialization is defined as a mechanism that allows any programmer to use types as parameters for a class or a function:

```c++
// In the code below sort is specialized for character data type
template<>
void sort<char>(char arr[], int size) {
	// Provide implementation
}
```

**Note** Example:

```c++
// Template function that return the maximum of 2 values
template<typename T>
T max(T a, T b) {
	return a > b ? a : b;
}
```

- Class template specialization
  ```c++
  template <typename T>
  class MyClass {
  	// Provide template class definition
  };

  // Creating specialized class definition
  template <>
  class MyClass<int> {
  	// Provide specialization for integer type
  }
  ```

**Note** *When we write any template-based function or class, the compiler creates a copy of that function/class whenever the compiler sees that being used for a new data type or a new set of data types(in case of multiple template arguments).
If a specialised version is present, the compiler first checks with the specialised version and then the main template. The compiler first checks with the most specialised version by matching the passed parameter with the data type(s) specified in a specialised version.*


### Template parameters

- Non-Type template parameters
  A part for `type` template parameter, C++ support non type parameters. Supported values are `lvalue reference`, `nullptr`, `pointer`, `enumeration`, and `integral`. Most use non-type parameter to template is integral.
  An example of non-type template implementation is `std::array<T, TSize>. `
  Non-types can be passed to template. They are ways of passing hey mainly focus on passing the constant expression i.e address of a function, object or static class member at compile time.
  **Note** Instead of `typename` or `class` keyword, non-type template accept type name as `keyword`.
- ```c++
  template <std::string *temp>
  void func() {
  	// Code
  }

  template <std::string& value>
  void func () {
  	// Template for reference value
  }

  ```
