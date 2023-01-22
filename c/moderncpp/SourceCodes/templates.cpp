#include <iostream>

template <typename... T> void my_func(T... args) {
  std::cout << "Total number of arguments: " << sizeof...(args) << std::endl;
}

template <typename... T> auto sum(T... t) { return (t + ...); }

// Returns the expression passed in the tempate as runtime value
template <auto value> auto template_val() { return value; }

int main() {

  my_func(2, 4, "Hello World!");
  std::cout << template_val<20>() << std::endl;
  std::cout << sum(1, 2, 3, 4, 5, 6, 7, 8, 9) << std::endl;
}