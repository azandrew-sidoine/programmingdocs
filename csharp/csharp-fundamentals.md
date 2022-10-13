# CSharp Fundamentals

-- Importing package or namespaces

```cs
// using <NamespaceName>

using System;

// Declaring the a namespace
namespace Basics
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello {0}!", "Azandrew Sidoine");
        }
    }
}
```

-- Array Indexing

```cs
class Collection {
    private int[] _array = new[] { 1, 2, 3 };

    public int Length {
        get {
            Console.Write("Length ");
            return _array.Length;
        }
    }

    public int this[int index] => _array[index];
}
```

## Data types

> <DataType> variableName;

- Automatic typing

> var variableName = <Value>;

- Array types

> <DataType>[] variableName;

```cs
// Integer number
int i = 10;

// Floating point number
float f = 2.0f;

// Decimal number
decimal d = 10.0m;

// Boolean 
bool b = true;

// Character 
char c = 'c';

// String type
string str = "String";

// Long int
long variableName = <BigNumber>;

// 
int[] vals = new int[5];

// Array or List of values
string[] strVar = {"One", "Two", "Three"};

// Array variable definition
var people = new string[] { "Jane", "Jean", "Grey", "Marcus", "Theophilus", "Keje" };
```

- Null type

> <DataType> variableName = null;

- Type conversion

> var variableName = (<DataType>)rhs;

## Operators

- Arithmetic operators

/, +, -, ++, --, +=, -=, /=

- Logical operators

&&, ||

- Null-Coalescing operators

```cs

string strVar = null;

// Null coealescing assignment
var saferStr = str ?? "Unknown String!";

// Or
var saferStr ??= "Unknown String";
```

## Comments

```cs

/// Provides documentation comments
/// <summary>
/// This is the main sample application
/// <param name="paramName">Parameter description </param>
/// <returns></returns>
/// </summary>

/**
* Multiple lines comments
*/

// Single line comments
```

- Generating documentaion file

```xml
<Project Sdk="...">
    <PropertyGroup>
    ...
        <GenerateDocumentationFile>true</GenerateDocumentationFile>
        <DocumentationFile>Filename.xml</DocumentationFile>
    ...
    </PropertyGroup>
</Project>
```

## Conditionals

```cs
// If ... else statement
if (<Condition>) {

} else {

}

// If ... else if ... statement
if (<Condition>) {

} else if (<Condition2>) {

} else {

}

// Ternary operator

var rValue  = <Condition> ? "<True Condition>" : "<False Condition>";


// Switch statement
switch(<StatementVariable>) {
    case <FirstValue>:
        // Code execution for the FirstValue
        break;
    case <GroupValueFirst>:
    case <GroupValueTwo>:
        // Code Execution
        break;
    default:
        // Default code execution
}

// For Loops
// Traditional for loop
for (int i=0; i< <MaxValue>; i++) {
    // Code execution
}

var list  = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
// Smart for loop
foreach(var i in list) {
    // Code execution on the list items
}


// While loop
while(<Condition>) {
    // Code execution
}

// Do while loop (Loops that runs at least once)
do {
    // Code execution
} while(<Condition>)

// Breaking out a loop
// While loop
while(<Condition>) {
    // Code execution
    if (<condition>) {
        break;
    }

    // Or using continue to jump to the next iteration
    if (<condition2>) {
        continue;
    }
}


// Execption handling
try {
    // Code that throws an exception
} catch (DivideByZeroException e) {
    // Catch DivideByZeroException exception
} catch {
    // Catch any exception
} finally {
    // Runs always
}

// Throwing exceptio
throw new ExceptionClass("<Exception message>")
```

## String Operations

- String length

> str.Length

- Accessing characters by index

> str[index]

- Looping through string

```cs
foreach (var in str) {
    // Code exectution
}
```

- String concatenation

> $"String {strVariable}! ... {someStringVariable}"

- Joining Strings

> String.Join(<Seperator>, strArray)

- String Comparison

> String.Compare(<Lhs>, <Rhs>) -> int - {<0, 0, >0}

- Checking if strings are equals

> str.Equals(str2)

- IndexOf

> str.IndexOf(<Character>) -> int

- Last Index Of

> str.LastIndexOf(<Character>) -> int

- Replacing in string

> str.Replace(<Search>, <Replacement>) -> string

Note : Take a look at the CSharp doc for advance string function


- String formatting

> "{index[,alignment|space]:[format]}" - format=N(Number)|G(General)|F(Fixed-Point)|E(Exponential)|D(Decimal)|P(Percentage)|X(Hexadecimal)|C(Currency)

```cs
int num = 1235;

Console.WriteLine("{0:D}, {0:N}, {0:G}, {0:E}, {0:F}", num);

// Alignment
Console.WriteLine("{0:D6}, {0:N2}, {0:G}, {0:E2}, {0:F2}", num);

// Spacing
Console.WriteLine("{0,12:D6}, {0,12:N2}, {0,12:G}, {0:E2}, {0:F2}", num);
```

Note: Refer to CSharp string formatting documentation

- String interpolation

```cs
string substr = "Interpolated";
int num = 1235;
string text = $"This is an {substr} string! Formated number: {num:C2}. With Expression {num*2}";
```

- String builder

String builder is a mutable string class that create a ref to a memory address for C# string to be modify.

```cs

using System.Text;

...
c = 200; // String builder capacity
var builder = new StringBuilder("<Initial string>", c);

Console.WriteLine($"{builder.Capacity}, Length: {builder.Length}");

// Appending a new String
builder.Append("<Added string>")

// Appending line
builder.AppendLine();

// Appending formated string
builder.AppendFormat("String with {}", str);

// Appending list of string
builder.AppendJoin("<Separator>", {"Dummy", "String"});

// Inserting at index of string
builder.Insert(0, "Start string");

// Replacing item
builder.Replace("<Source>", "<NewValue>");

// Converting back to immutable string
finalString  = builder.ToString();
...

```

- String parsing

```cs

// Using system.Globalization to specify number styles
using System.Globalization;


...
try {

    // Parsing string to an integer
    int value  = int.Parse("1");

    // Parsing floating number
    float f = int.Parse("1.000", NumberStyles.Float);

    // Potential thousand numbers and decimal point values
    var val = int.Parse("3,000", NumberStyles.Float | NumberStyles.AllowThousand);

    // Parsing boolean
    var b = bool.Parse("True");

    // Parsing floating point values
    var f = float.Parse("1.2345");

} catch {
    // Exception throws while parsing values
}

// Without try catch block

result  = Int32.TryParse("1.0", out val); // Using C++ output syntax
...
```

- Checking if a character is a punctuation or a whitespace

> char.IsPunctuation(c) -> bool

> char.IsWhiteSpace(c) -> bool - Check if character is 

-- Random Generator

```cs

using System;

...
// Generate a number between 0 - MaxValue
randNum = new Random().Next(<MaxValue>);
...

```

## CSharp Function


```cs
/// <DataType> func([<DataType> param]) 
/// {
///     Code execution...
/// }
///

float MilesToKm(float p)
{
    return p * 1.6f;
}

// Void returned function
void func()
{
    // Code execution block
}


/// Named & Default parameters functions
/// Default function parameters must be last parameters
/// <DataType> func(<DataType> param1, <DataType> defaultparam1 =<DefaultValue>) 
/// {
///     Code execution...
/// }
// Calling function with Named params
// func(p, defaultparam1: <Value>)

void func(string str, string prefix = "%", string postfix = "%")
{
    // Function definition...
}

func("Intial string", prefix: "#", postfix: "#")
```

--- Reference out parameters

Note by default, C# parameters ares passed by value, unless they are objects.

In order to modify the value of the parameter, use the [ref] keyword. Note, `ref` is like `&` keyword in other languages.

```cs

/// <DataType> func([ref] [<DataType> param]) 
/// {
///     Code execution...
/// }

/// <DataType> func([out] [<DataType> param]) 
/// {
///     Code execution...
/// }

mutableFunc(ref string value)
{
    value = "<New String Value>";
}

sum(int a, int b out int r)
{
    r = a + b;
}

// Calling reference params functions
str = "<Initial string>";
mutableFunc(ref str);


/// Function with output parameters
int result;

sum(a, b, out result);
```

-- Returning a tuple from a C# function

C# are lightweight immutable datatype for grouping values together.

```cs

/// (<DataType> a, <DataType> b) tuple = (<Val1>, <Val2>)

(int a, int b) numTuple = (5, 10);

/// Returning multiple values using tuples
/// (<DataType>, <DataType>, ...) funcName([<DataType> params])
/// {
///        return (<Expresion1>, <Expression2>, ...)
/// }

(int, int) PlusTimes(int a, int b)
{
    return (a+b, a*b);
}

(bool, int) IsPalinDrome(string str)
{
    str = str.ToLower();
    // Cleanup string
    int = 0; j = str.Length;

    // While both start and end indexes does not cross
    while(i <= j) {
        if (str[i] != str[j]) {
            return (false, 0);
        }
        i++;
        j--;
    }
    return (true, str.Length);
}
```

-- Deconstructing tuples

```cs

public class Example
{
    public static void Main()
    {
        var result = QueryCityData("New York City");

        var city = result.Item1;
        var pop = result.Item2;
        var size = result.Item3;

         // Do something with the data.
    }

    private static (string, int, double) QueryCityData(string name)
    {
        if (name == "New York City")
            return (name, 8175133, 468.48);

        return ("", 0, 0);
    }

    var (city, population, area) = QueryCityData("New York City");

    // Deconstructing with discard of some values
    (string city, _, double area) = QueryCityData("New York City");
}
```

## Object oriented in C#

```cs
// Class definition in C#
namespace Geometry
{
    /// <AccessModifier> class <Classname>
    /// {
    ///     <AccessModifier> <Classname>()
    ///     {
    ///         // Initialize class members in the constructor
    ///     }
    ///     // Class members definitions
    /// }

    public class Coord
    {

        // Csharp properties definition
        private double _x;
        public double X
        {
            get { return _x; }
            set { _x = value; }
        }
        
        private double _y;
        public double Y
        {
            get { return _y; }
            set { _y = value; }
        }

        public Coord()
        {
        }

        string public ToString()
        {
            return $"{{x : {_x}, y: {_y} }}";
        }
    }

    /// C# Inheritance
    /// <AccessModifier> class <BaseClassName>
    /// {
    ///     <AccessModifier> <Classname>([<params>])
    ///     {
    ///         // Initialize class members in the constructor
    ///     }
    ///     // Class members definitions

    ///     // Method is declare virtual in order to allow 
    ///     // overriding
    ///     <AccessModifier> virtual <DataType> function()
    ///     {
    ///         // Provide base class code
    ///     }
    /// }
    /// <AccessModifier> class <SubClassname> : <BaseClassName>
    /// {
    ///     <AccessModifier> <Classname>([<params>]): base([<baseclassCtorParams>])
    ///     {
    ///         // Initialize class members in the constructor
    ///     }
    ///     // Class members definitions
    ///     <AccessModifier> override <DataType> function()
    ///     {
    ///         // Provide override code
    ///         // Calling base class method
    ///         var result = base.function();
    ///         // Do something else
    ///     }
    /// }
}
```

-- Abstract class

```cs
namespace ClassNamespace
{
    public abstract class AbstractClass
    {
        // Provide properties definitions
        public double num {get; set; };

        // Provide abstract method defintions
        /// <public> abstract <DataType> Func();
        public abstract void AbstractMethod();
    }
}
```

-- C# Interfaces

Note: C# Interface can have properties defines in them. But is that a good design idea? You should decide.

```cs
namespace InterfaceNamespace
{
    public interface ClassInterface
    {
        // Provide method declarations
        /// <public> abstract <DataType> Func();
        void method1();
    }

    // Implementing an interface
    /// <AccessModifier> class <ClassName> : <InterfaceName> 
    /// {
    ///     // Provide class definitions
    /// }
    public class ClassName :  ClassInterface, ClassInterface2
    {
        public void method1()
        {
            // Provides interface implementation
        }
    }
}
```

-- Extension Methods

Extension methods provides a way for adding functionnality to a class externally.

Note: Extension class must be public and static.

```cs

using System.Text;
///
/// public static class ExtensionClasname
/// {
///     public static <DataType> <FuncName>(this <DataTypeToExtends> param)
///      {
            // Extension code
///       }
/// }
public static class ExtensionMethodClass
{
    public static int WordCount(this string str)
    {
        var wCount = str.Split(new char[] {' ', '.', '?'}, StringSplitOptions.RemoveEmptyEntries).Length;

        return wCount;
    }
}
```

## C# Collections

Note: Generic collection classes offer better performance over the non-generic collection types.

List - Good for random access to data, Fast for retrieval, Item intended to be kepts in memory, Need contiguous memory to store data.

Linked-List - Good for sequential accessed data, Fast adding and removing data, Item intended to be kepts in memory

Stack & Queue - Good for sequential accessed data, Fast adding and removing data, Items intended to be discard after processing, Need contiguous memory to store data, FIFO, LIFO order

Dictionnary - Good for random access to data, Fast for retrieval, Item intended to be kepts in memory,Need contiguous memory to store data.


--- List

Unlike arrays, list can be resized.

```cs

/// var listVar = List<DataType>(<Capacity>)
var list = new List<string>(10);

/// list.AddRange(<DataType>[] arr) - Adding a range of values
list.addRange({"Hello", "World", "!"});

/// list.Add(<DataType> p) - Adding a single value
list.Add("Suckers");

/// list[index] - Get item at index
var value = list[2];

/// list.RemoveAt(int index) - Removing at index
list.RemoveAt(3);
/// list.Remove(<DataType> p) - Removing list element
list.Remove("Suckers");

/// list.Sort() - Sorting list items
list.Sort();

/// list.Contains(<DataType> p) -> bool - Returns true or false if the list contains the param
list.Contains("Suckers");

/// list.Exists(Lambda) -> bool - Returns true for the return value of the lamda
list.Exists(x => x.Length > 15);


/// list.Find(Lambda) -> <DataType> - Return the first item matching a given criteria
list.Find(x => x.StartWith("L"));

/// list.FindAll(Lambda) -> <DataType> - Return all matches for a given lambda
List<string> result = list.FindAll(x => x.StartWith("L"));

/// list.TrueForAll(Lambda) -> <DataType> - Return true if all element in the list match the predicated
List<string> result = list.TrueForAll(x => x.StartWith("L"));
```

--- LinkedList

Csharp linkedlist are Doubly linked list, that hold a ref to the next and previous. Items can't be easily access randomly. Great for sequential data.

The linkedlist support `Find` and `FindAll` methods as well but return a ref to LinkedListNode class instance.

```cs
...
using System.Collections.Generic;
...

LinkedList<string> list = new LinkedList<string>({
    "Shout", "Satisfaction", "Help!"
});

/// list.AddFirst(<DataType> p) - Adding to the top of the list
list.AddFirst("Africa");

/// list.AddLast(<DataType> p) - Adding to the tail of the list
list.AddLast("Europa");

/// list.First - Getting linked list first node
LinkedListNode<string> first = list.First;
LinkedListNode<string> last = list.Last;

/// listNode.Value - Accessing node value
Console.WriteLine(first.Value);

/// list.AddAfter(LinkedListNode<DataType> p, <DataType> value) Adding after a node
list.AddAfter(first, "Hello");
```

--- Stacks

```cs
...
using System.Collections.Generic;
...

/// Creating a stack
var stack = new Stack<string>();

/// stack.Push(<DataType> p) - Push item to the stack
stack.Push("New Value");

/// stack.Count - Number of item in the stack
total = stack.Count;

/// stack.Peek(); Get the top element without removing it
var item = stack.Peek()

/// stack.Pop() -> <DataType> - Get top element and remove it
var item = stack.Pop();

/// stack.Contains(<DataType> p) -> bool - Check if stack contains a given element
```


--- Queues

They are FIFO data structures.

```cs
...
using System.Collections.Generic;
...

/// Creating a stack
var q = new Queue<string>();

/// q.Enqueue(<DataType> p) - Push item to the queue
stack.Enqueue("New Value");

/// q.Count - Number of item in the stack
total = q.Count;

/// q.Peek(); Get the fromt element without removing it
var item = q.Peek()

/// q.Dequeue() -> <DataType> - Get front element and remove it
var item = q.Dequeue();

/// q.Contains(<DataType> p) -> bool - Check if stack contains a given element

/// q.Clear() - Flush the queue
q.Clear();
```

--- Dictionnary Collection types

```cs
var dict = new Dictionary<string, string>();

/// dict.Add(<KType> k, <VType> v) Adding item to the dictionnary
dict.Add(".bmp", "Bitmap");

/// dict.Count - Number of item in the dictionnary
total = dict.Count;

/// dict.TryAdd(<KType> k, <VType> v) -> bool - Safely add a key, If already exist, the key is not added and False is returned
result = dict.TryAdd(".bmp", "Bitmap")

/// Accessing based on keys
result = dict[".bmp"];

/// Modifying dictionnary key
dict[".bmp"] = "Bitmap Image";

/// dict.Contains(<KType> k) -> bool - Check if dictionnary contains a given key
dict.Contains(".bmp");

/// Remove value assoc to key
dict.Remove(".bmp");
```

--- ListDictionary and HybridDictionary (non-generic dictionary)

For items less (<10) List Dictionary is faster than Dictionary as it's implemented as LinkedList. But it's old implementation.

HybridDictionary act like a ListDictionary when item <= 10, and converge to Dictionary when size grows

> var list = new HybridDictionary(<Capacity>, false)

--- OrderedDictionary

Dictionary element are ordered as they are added to the collection.

> var list = new OrderedDictionary();


--- String Collection (Old implementation of List<string>)

```cs

var collection = new StringCollection();

collection.addRange({"Hello", "World"});

collection.Add("Element");

collection.Insert(0, "First Element");

var count  = collection.Count();

/// Array indexing
collection[index];

/// Contains
collection.Contains("Element");

/// Index of
collection.IndexOf("Element");

/// Clearing the collection
collection.Clear();
```

## C# Interfaces and Generics

--- Interfaces

```cs

/// Check if a given object is an instance of class or intreface
if (obj is ClassType) {
    // Object is of a given ClassType
}

/// Casting to a class or interface
(obj as ClassType).interfaceMethod();
```

- Explicit interface implementation

```cs

namespace NamespaceName
{
    interface Foo
    {
        void SomeMethod();
    }

    interface Bar
    {
        void SomeMethod();
    }

    public class FooBar : Foo, Bar
    {
        /// Explicit interface implementation for resolving naming conflicts
        void Foo.SomeMethod()
        {

        }

        void Bar.SomeMethod()
        {

        }
    }
}
```


-- Generic class and Method

> IComparer<T> - C# Comparison interface to implement comparison in list items. It provide only one method:

```cs
interface IComparer<T>
{
    int Compare(T lhs, T rhs);
}

class ValueComparer<VType> : IComparer<VType>
{
    int Compare(T lhs, T rhs)
    {
        // 0 - object are equals
        // > 0 - First object is greater than the second
        // < 0 - First object is less than the second
    }
}


list.Sort(new ValueComparer());
```

```cs
/// Creating generic classes
class GenericClass<T,U,...>
{

}

/// Generic type inheriting from base type
class GenericClass<T>: BaseClass
{

}

/// Generic type constraints
class GenericClass<T> where T : System.IComparable<T>
{
    // It works like <T extends AnotherType>
}

/// Generic classes with Generic method
class SampleClass<T>
{
    void Swap(ref T lhs, ref T rhs) { }
}


/// Generic interfaces
interface IDictionary<K, V>
{
}

interface IBaseInterface<T> { }

/// Generic method
static void Swap<T>(ref T lhs, ref T rhs)
{
    T temp;
    temp = lhs;
    lhs = rhs;
    rhs = temp;
}
```

### Delegates

```cs

/// Like type Function = (message: string) => void implementation in Typescript
public delegate void DelagateType(string message);

/// Function that can be use in place of the delegate
// Create a method for a delegate.
public static void DelegateMethod(string message)
{
    Console.WriteLine(message);
}

// Instantiate the delegate.
DelagateType handler = DelegateMethod;

// Call the delegate.
handler("Hello World");
```

-- Multi cast delegate

It works like function composition, but a little bit wierd.

```cs
using System;

// Define a custom delegate that has a string parameter and returns void.
delegate void CustomDel(string s);

class TestClass
{
    // Define two methods that have the same signature as CustomDel.
    static void Hello(string s)
    {
        Console.WriteLine($"  Hello, {s}!");
    }

    static void Goodbye(string s)
    {
        Console.WriteLine($"  Goodbye, {s}!");
    }

    static void Main()
    {
        // Declare instances of the custom delegate.
        CustomDel hiDel, byeDel, multiDel, multiMinusHiDel;

        // In this example, you can omit the custom delegate if you
        // want to and use Action<string> instead.
        //Action<string> hiDel, byeDel, multiDel, multiMinusHiDel;

        // Create the delegate object hiDel that references the
        // method Hello.
        hiDel = Hello;

        // Create the delegate object byeDel that references the
        // method Goodbye.
        byeDel = Goodbye;

        // The two delegates, hiDel and byeDel, are combined to
        // form multiDel.
        multiDel = hiDel + byeDel;

        // Remove hiDel from the multicast delegate, leaving byeDel,
        // which calls only the method Goodbye.
        multiMinusHiDel = multiDel - hiDel;

        Console.WriteLine("Invoking delegate hiDel:");
        hiDel("A");
        Console.WriteLine("Invoking delegate byeDel:");
        byeDel("B");
        Console.WriteLine("Invoking delegate multiDel:");
        multiDel("C");
        Console.WriteLine("Invoking delegate multiMinusHiDel:");
        multiMinusHiDel("D");
    }
}
/* Output:
Invoking delegate hiDel:
  Hello, A!
Invoking delegate byeDel:
  Goodbye, B!
Invoking delegate multiDel:
  Hello, C!
  Goodbye, C!
Invoking delegate multiMinusHiDel:
  Goodbye, D!
*/
```