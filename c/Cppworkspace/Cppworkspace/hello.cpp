//
//  hello.cpp
//  Cppworkspace
//
//  Created by LIKSOFT on 19/02/2021.
//

#include "hello.hpp"

//constexpr  size_t  byte = 8;
//
//struct Employee {
//    int id;
//    const char* name;
//    const char* role;
//};
//
//const int& func(const int& i) {
//    int _i = i;
//    return ++_i;
//}
//
//void f(int i) {
//    printf("Value of i is %d\n", i);
//}
//
//void f(const char* s) {
//    printf("the pointer is %p\n", s);
//}
//
//int main()
//{
//    puts("Hello Suckers!"); // write a sinngle line to the standard output
//    
//    // assigning and returning value at the same time
//    int value = 0;
//    printf("The value of x is %u \n", value = 42);
//    
//    // working with pointers
//    int x = 0;
////    int y = 0;
//    
//    int *x_ptr =  &x;
////    int *y_prt  =  &y;
//    
//    *x_ptr = 12;
//    
//    printf("Value  of x is %d \n", x);
//    printf("Value of pointer to x is %d \n", *x_ptr);
//    
//    // working  with integers  size
//    
//    printf("sizeof  char  is  %lu bits\n",  sizeof(int8_t) * byte);
//    printf("sizeof  short  is  %lu bits\n",  sizeof(short int) * byte);
//    printf("sizeof  int  is  %lu bits\n",  sizeof(int) * byte);
//    printf("sizeof  long int  is  %lu bits\n",  sizeof(long int) * byte);
//    printf("sizeof  long long int  is  %lu bits\n",  sizeof(long long int) * byte);
//    
//    printf("Octal based (147) %d\n", x = 0223);
//    
//    printf("Hexadecimal based (147) %d\n", x = 0x0093);
//    
//    // Working with reference
//    int i = 5;
//    // Create a reference variable that point to the same address as i
//    int &i_ref = i;
//    i_ref = 10;
//    
//    printf("Value of i is: %d\n", i);
//    
//    // const reference
//    printf("value of i is %d\n", i);
//    printf("value of i in func() is %d\n", func(i));
//    printf("value of i after func() call is %d\n", i);
//    
//    
//    printf("Working with stuctures: \n");
//
//    Employee p = {42, "Jack", "Administrator"};
//    Employee* p2 = &p;
//
//    // Accessing using member access operator
//    printf("Employee details: ID - %d, Name: %s, Role: %s\n", p.id, p.name, p.role);
//
//    // Accessing using pointer access operator
//    printf("Employee2 details: ID - %d, Name: %s, Role: %s\n", p2->id, p2->name, p2->role);
//    
//    printf("Working with auto iterating over vector: \n");
//    // Auto type for iterating
//    std::vector<uint8_t> v =  {1, 2, 3, 4, 6};
//    
//    for (auto it = v.begin(); it != v.end(); ++it) {
//        printf("value a index %d\n", *it);
//    }
//    
//    // Calling f with NULL create a function ambiguty error
//    // f(NULL); // Throws error, as compiler does not know which functiosn to call
//    f(nullptr); // Solve issue with C++ 11
//    return 0;
//}
