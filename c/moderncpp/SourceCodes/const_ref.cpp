#include <cstdio>

// Passing const reference to a function prevent the function
// to modify the value of the variable passed as parameter
// and allow program to gain in efficiency as no copy of the variable is make
// when passing variable
const int& immutable_update(const int&);

// The program test c++ const reference of functions
int main() {
    short int myval = 10;
    int result = immutable_update(myval);
    const int& (*func_ptr)(const int&) = &immutable_update;

    printf("Value of myval: %d\n", myval);
    printf("Result value: %d\n", result);

    // Invoke function pointer
    printf("Function pointer return: %d\n", func_ptr(30));
    return 0;
}

const int& immutable_update(const int& input) {
    int _input =  input;
    return ++_input;
}