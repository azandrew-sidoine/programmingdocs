# .NET Functionnal programming

-- Pure function
    Mathematic concept of a function that take an input and return the same output if the same input is provided

-- High order function
    Function that take function as parameter and/or return function as return values.

-- Function composition
    Composed function is a paradigm of output of a function being input of another function.


## Higher order function

> Func<T> - Takes a parameter and return a new parameters. They are the return type of lambda expression

> Action<T> - Function that do not return

```cs

private void Lambda()
{
    // Lambda expression
    Func<int, int> func = x => x * 10;
}

// Higher order function implementation
public static K  HigherOrderFunc<T, K>(Func<(T, T), K> func, T num1, T num2)
{
    return func((num1, num2));
}

Console.WriteLine("Multiplication Result: {0}", HigherOrderFunc(Func, 10, 20));

Console.WriteLine("Addition  Result: {0}", HigherOrderFunc(Func2, 10, 20));

// Usage
Func<(double, double), double> Func = ((double x, double y) p) => p.x * p.y;

Func<(double, double), double> Func2 = ((double x, double y) p) => p.x + p.y;
```

## Function Composition with extension method

```cs
public static class Extensions
{
    public static Func<T, TReturn2> Compose<T, TReturn1, TReturn2>(this Func<TReturn1, TReturn2> func1, Func<T, TReturn1> func2)
    {
        return x => func1(func2(x));
    }
}
```