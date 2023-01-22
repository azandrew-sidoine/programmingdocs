#include <cstdio>

/**
 * This program try to use pointer iterator to loop through all
 * values of a given array/integer container
 */
int main() {
  int list[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

  printf("value at index 0 = %d\n", *list);

  // Loop though c-style array using pointer incrementation syntax
  // Because arrays are accessed by reference, no need for & to create a pointer
  // to the element
  int *iterator = list;
  // Creates a reference to the last element to compare it against
  // the iterator pointer
  int *last = list + 10;

  // Index is just for debuging pupose when printing value at a given index
  int index = 0;
  while (iterator != last) {
    // We use pointer value at/dereferencing operator to acess the value
    // that th pointer hold
    printf("Value at index: %d, = %d\n", index, *iterator);
    index = index + 1;
    // We increments the pointer to point to the next element
    ++iterator;
  }

  size_t i = 0;
  // Looping using for loop
  printf("\nUsing for... loop \n");
  for (int *int_ptr = list; int_ptr != last; ++int_ptr) {
    printf("Value at index: %lu, = %d\n", i, *int_ptr);
    i = i + 1;
  }

  i = 0;
  // Looping using for c++ range loop
  printf("\nUsing range or smart iterator loop \n");
  for (int current : list) {
    printf("Value at index: %lu, = %d\n", i, current);
    i = i + 1;
  }

  return 0;
}