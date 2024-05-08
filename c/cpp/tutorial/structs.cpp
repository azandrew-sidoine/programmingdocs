#include <iostream>

struct Person {
    char name[50];
    int age;
    float salary;
};

int main()
{
    Person p{"Azandrew", 32, 500000};

    std::cout << "Printing person details:\n";
    std::cout << "Name: " << p.name << std::endl;
    std::cout << "Age: " << p.age << std::endl;
    std::cout << "Salary: " << static_cast<float>(p.salary) << std::endl;

    return 0;
}