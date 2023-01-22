#include <cstdio>

struct Employee {
    int id;
    const char* name;
    const char* role;
};

int main() {

    Employee p = {42, "Jack", "Administrator"};
    Employee* p2 = &p;

    // Accessing using member access operator
    printf("Employee details: ID - %d, Name: %s, Role: %s\n", p.id, p.name, p.role);

    // Accessing using pointer access operator
    printf("Employee2 details: ID - %d, Name: %s, Role: %s\n", p2->id, p2->name, p2->role);

    // This modifies value at the refence p2 causing the default p value be modify as well
    p2->name = "Joh Doe";
    p2->role = "Developper";

    printf("\nAfter update...\n");
    printf("Employee details: ID - %d, Name: %s, Role: %s\n", p.id, p.name, p.role);

    // Accessing using pointer access operator
    printf("Employee2 details: ID - %d, Name: %s, Role: %s\n", p2->id, p2->name, p2->role);
}