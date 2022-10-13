# .NET Essentials - Working With LINQ (Links to Object)

## LINQ Query providers

- It's responsible for turning query intent into domain specific commands.

- When query is compiled, query is turned into an expession trees

- The query expression tree is then executed as a deffered manner

LINQ QUERY -> EXPRESSION -> EXECUTION OF THE EXPRESSION TREE

## Keypaet of .NET

--- Anonymous types

```cs

// Use new operator, but don't specify a typename
// use {} to initialize read-only properties
// Use the name-value pair within the initializer to declare property names
// Type properties are inferred by the compiler
var x = new {Color = "Red", Price = 40M };
```

--- Object initializers

```cs

public class House
{
    public int Floor;
    public int Bathrooms;
}

// Using the object initializer syntax to initialize house object
var h = new House {Bathrooms = 2};

var h2 = new House {};

var h3 = new House {Bathrooms = 4, Floor = 3};
```

--- Collection initializers

```cs

var l = new List<Int32> {1, 3, 56, 9};

var arr = new double[] {1.2, 2.3, 3.5};

var dict = new Dictionnary<string, int> {
    {"yellow", 23},
    {"blue": 12}
};
```

--- Lambda expression

> Func<InType, OutType> variableName;

```cs
Func<Int32, Int32> adder = (Int32 n) => {n += 2 ; return n + 1; };
Console.WriteLine(adder(5));
```

--- Extension methods


```cs

public static class TypeNameExtensions
{
    public static void ShowAll<T>(this  IEnumerable<T> c)
    {
        // Loop through the collection items and write all element to the console
    }
}
```

--- Generic Types

Library writers creates generic classes, method, interfaces, delegates... and the library users provide specific type that can replace the generic type at runtime.

## The parts of a Query

--- Dump method

> Dump() -> return the data in a queryable or Enumerable data.

```cs
// Loading A library at runtime
var asm = Assembly.Load("System.Data.Entities");

// Filter by generic types
// With LINQ, FROM <Alias> in <Collection> comes first and SELECT comes last in contrast to SQL
var q = from type in asm.GetExportedTypes()
        from i in type.GetInterfaces()
        where i.IsGenericType && type.IsClass && i.GetGenericTypeDefinition() == typeof(IEnumerable<>)
        orderby type.Name
        // select type.Name;
        select { Name = type.Name };
```

--- What are queryable data ?

They are sort of pool, sequence or collection ot items.


--- Deffered execution of LINQ Queries

For IEnumerable<T> or IQueryable<T>, toArray() triggers the query execution.

```cs
var nums = new List<int>{3, 4.5, 2.5. 10};

q = from n in nums
    where n > 7
    select num;

q.ToArray();

// or

q = nums.Where(n => n > 7).Distinct();
q.ToArray();
```

--- Pipelining function calls with

Based on extension methods, Link queries cn be chained.

--- Combining Expression method & Query method

```cs

var q1 = from c in colors
    where c.StartWith("G")
    select c;

// Calling lambda
total_count = q1.Count();

// Or
var result = (from c in colors
    where c.StartWith("G")
    select c).Count();
```

## Generates

> var list = Enumerable.Empty<DataType>() -> DataType - Returns an empty list

> Enumerable.Empty()

> Enumerable.DefaultIfEmpty<DataType>(<DataType> default_param) -> IEnumerable - Return default datatype value if default_param is empty


--- Repeat

> Enumerable.Repeat<DataType>(int <NumToFillCellsWith>, int <NumberOfIteration>)

--- Range

Generate sequence of integral number within a specified range

> Enumerable.Range(start: 1000, count: 30);

## The basics