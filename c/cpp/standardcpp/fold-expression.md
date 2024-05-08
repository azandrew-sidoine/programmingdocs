# C++17 Fold Expressions

It's an instruction for the compiler to repeat the `application of an operator over a variadic template pack`. Below is an example that sum a list of parameters passed to a function:

```c++
template<typename... T>
auto sum(T const&... args) {
	// Code
	return (args + ...); // Fold expression that compute the sum of all elements passed to the function
}
```

**Note** `()` is needed for the fold expression to works. `+ ...` creates the repetition of the operation + on all elements passed to the function.

## Fold expression associativity

`(operator ...)` denote a right associativity of the fold expression while `(... operator)` denote a left associative operation.

`(value + ...)` computes `value + sum(...)` while `(... + value)` computes `sum(...) + value`. Sometimes/in some operation associativity matter, therefore fold expression should be implemented carefully.

**Note** By default, C++ compilers does not handle empty parameters case of fold expression, therefore developper should take care of handling empty parameter case when writing fold expression. For example, for a `sum` function to return 0 if empty parameter is passed in:

```
template<typename... T>
auto sum(T const&... values) {
	return (0 + ... + values);
}
```
