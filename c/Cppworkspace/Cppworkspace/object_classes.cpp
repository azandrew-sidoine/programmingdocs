//
//  object_classes.cpp
//  Cppworkspace
//
//  Created by LIKSOFT on 24/02/2021.
//

#include "object_classes.hpp"


class Point
{
private:
    double x, y;
    
public:
    Point() {
        x = y = 0;
    }
    
    double getX();
    
    void setX(double value);
    
    double getY();
    
    void setY(double value);
};


void Point::setX(double value)
{
    x = value;
}

double Point::getX()
{
    return x;
}

void Point::setY(double value)
{
    y = value;
}

double Point::getY()
{
    return y;
}

int main()
{
    Point p = Point{};
    Point* p_ptr = &p;

    p_ptr->setX(4);
    p_ptr->setY(-2);

    printf("Coordinates of the point are: %f, %f", p.getX(), p.getY());

    return 0;
}
