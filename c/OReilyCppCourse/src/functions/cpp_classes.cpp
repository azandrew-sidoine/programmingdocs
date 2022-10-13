#include <cstdlib>
#include <cstdio>
#include "oop/Point.hpp"
#include "oop/Integer.hpp"

int main(int argc, const char** argv) {

    Point point = Point{0, 0};

    printf("X: %d, Y: %d\n", point.GetX(), point.GetY());

    point.Move(0, 10);

    printf("X: %d, Y: %d\n", point.GetX(), point.GetY());

    // Copy the object
    auto point1 = point.Copy();

    point.Move(5);

    printf("Point - X: %d, Y: %d\n", point.GetX(), point.GetY());

    printf("Point1 - X: %d, Y: %d\n", point1.GetX(), point1.GetY());

    // Working with integer class

    auto intValue = Integer{0};
    intValue.SetValue(5);
    // This call will invoke Integer class copy constructor
    Integer intValue2 = intValue;
    intValue.SetValue(22);
    printf("Intvalue : %d\n", intValue.GetValue());
    printf("Intvalue 2: %d\n", intValue2.GetValue());
    return 0;
}