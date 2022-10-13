//
//  main.cpp
//  Cppworkspace
//
//  Created by LIKSOFT on 24/02/2021.
//

#include <cstdio>
#include "points.hpp"
#include "rational.hpp"
#include <cstdint>
#include <new>

constexpr size_t count = 1024;

void run_new_and_delete()
{
    // Note: Every object initialized with new must be delete with
    // delete otherwise program must leak memory
    printf("Allocate space for %lu int a *ip with new \n", count);

    long int* i_ptr;

    try {
        i_ptr = new long int [count];
    } catch (std::bad_alloc& ex) {
        std::fprintf(stderr, "Cannot allocate memory (%s)\n", ex.what());
        return;
    }
    // initialize array
    for (long int i = 0; i < count; ++i) {
        i_ptr[i] = i;
    }

    for (long int i = 0; i < count; ++i) {
        printf("Value of index %ld\n", i_ptr[i]);
    }

    // Deallocate the memory space
    // [] delete for than one item
    delete [] i_ptr;
    puts("Space at *i_ptr deleted");
}
int sum_down(int n)
{
    int r = 0;
    while (n > 0) {
        r += n;
        --n;
    }
    return r;
}

uint64_t fact(uint64_t n)
{
    uint64_t r  = 1;
    while (n > 1) {
        r = r * n;
        --n;
    }
    return r;
}


uint64_t recursive_fact(uint64_t n)
{
    if (n <= 1) return 1;
    else return n * recursive_fact(n-1);
}

int recursive_sum_down(int n)
{
    if (n <= 0)
    {
        return 0;
    }
    return n + recursive_sum_down(n - 1);
}

// Fibonacci
template<int n>
struct Fibonacci {
    enum {
        value = Fibonacci<n - 1>::value + Fibonacci<n - 2>::value
    };
};

template<>
struct Fibonacci<0> {
    enum {
        value = 0
    };
};

template<>
struct Fibonacci<1> {
    enum {
        value = 1
    };
};

int main()
{
//    Point p;
//    const Point p2 = Point{.5, -3.5}; // Point(.5, -3.5)
//
//    p = p2;
//    printf("Point coordinates: {x: %lf, y: %lf} \n", p.getX(), p.getY());
//    p.move(2, 3.5);
//    printf("Point coordinates after moving: {x: %lf0, y: %lf0} \n", p.getX(), p.getY());
//
//    // Working with Rational class
//    Rational a = 7;
//    Rational b(5, 3);
//    Rational c = b; // Called copy constructor
//    Rational d = std::move(c);
//
//    printf("Value of a is, %s\n", a.c_str());
//    printf("Value of b is, %s\n", b.c_str());
//    printf("Value of c is, %s\n", c.c_str());
//    printf("Value of d is, %s\n", d.c_str());
    
    
//    printf("Iterative sum_down is equal = %d\n", sum_down(10));
//    printf("Recursive sum_down is equal = %d\n", recursive_sum_down(10));
    printf("fib(0) = %d\n", Fibonacci<0>::value);
    printf("fib(4) = %d\n", Fibonacci<4>::value);
    printf("fib(8) = %d\n", Fibonacci<8>::value);
    printf("fib(10) = %d\n", Fibonacci<10>::value);
    return 0;
}
