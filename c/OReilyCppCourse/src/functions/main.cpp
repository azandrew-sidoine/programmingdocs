#include "functions/math.hpp"
#include "functions/utils.hpp"
#include <cstdio>
#include <string>

void run_tuple_code();

void c_malloc();

void cpp_malloc(); // Function for testing c++ memory allocation

void cpp_malloc_string(); // Dynamic malloc for cpp strings

void cpp_2d_malloc(); // 2D array malloc

int main() {
  int values[6]{1, 2, 3, 4, 5, 6};

  int length = *(&values + 1) - values;

  printf("Performing calculation... \n");

  int result = sum(values, length);

  printf("Result: %d \n", result);

  // Tuple code
  run_tuple_code();
  return 0;
}

void run_tuple_code() {
  int a = 5;
  int b = 8;
  swap(a, b);
  printf("Valueof a: %d - Valueof b: %d \n", a, b);

  std::string i = "Hello";
  std::string j = "World";
  swap(i, j);

  printf("Valueof i: %s - Valueof j: %s \n", i.c_str(), j.c_str());

  // C Memory allocation
  c_malloc();

  // C++ Memory allocation
  cpp_malloc();

  // C++ Arrays memories allocation
}

void c_malloc() {
  // Allocate memory on the heap
  int *p = (int *)malloc(sizeof(int));

  if (p == NULL) {
    printf("Malloc fails to allocate memory!\n");
  }

  // Assign value to the memory
  *p = 5;

  // Print the value of p
  printf("Value: %d\n", *p);

  // Free the allocated memory
  free(p); // Remember to set the p value to null after free to avoid dangling
           // pointers
  p = NULL;
  free(p); // Testing for dangling pointers
}

void cpp_malloc() {
  // Allocate memory for integer on the heap
  int *p = new int;

  // Or dynamic initialization - int *p = new int(10);
  *p = 10;

  // Display value of p
  printf("Value: %d\n", *p);

  delete p;

  // Always set pionter to nullptr
  p = nullptr;

  // Allocating memory for array

  int *array = new int[10]; // Allocate memory for an array of 10 integers

  for (int i = 0; i < 10; i++) {
    array[i] = i;
  }

  // Printing values of the array
  printf("List Values:\n");
  for (int i = 0; i < 10; i++) {
    printf("Index: %d = %d \n", i, array[i]);
  }

  delete[] array;
  array = nullptr;

  cpp_malloc_string();

  cpp_2d_malloc();
}

void cpp_malloc_string()
{
  char* chararray = new char[4]; // 
  std::strcpy(chararray, "C++"); // Allocated 4 char length because of \0 character that must terminate strings
  printf("String value is : %s\n", chararray);
  delete[] chararray;
  chararray = nullptr;
}

void cpp_2d_malloc()
{
  int *r = new int[2];
  int* c = new int[3];

  // Creating 2d array malloc
  int** table = new int*[2];

  table[0] = r;
  table[1] = c;

  // Assigning value to an element of the 2d array
  table[0][1] = 10;

  // Printing value of table[0][1]
  printf("Value at 0:1 = %d\n", table[0][1]);

  delete[] r;
  delete[] c;
  delete[] table;

}