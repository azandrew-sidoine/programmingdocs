#include <utility>
#include <iostream>

template<typename T>
inline void swap(T& a, T& b) {
    T tmp(std::move(b));
    b = std::move(a);
    a = std::move(tmp);
}

int main() {
    int a = 10;
    int b = 20;

    std::cout << "A: " << a << std::endl;
    std::cout << "B: " << b << std::endl;

    swap(a, b);

    std::cout << "A: " << a << std::endl;
    std::cout << "B: " << b << std::endl;

    return 0;
}