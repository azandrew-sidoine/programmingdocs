//
//  points.cpp
//  Cppworkspace
//
//  Created by LIKSOFT on 24/02/2021.
//
#include "points.hpp"

Point::Point() {
    _x = _y = 0;
}

// Copy constructor
Point::Point(const Point &p): _x(p.getX()), _y(p.getY()) {}

// Constructor with member initializer
// _privateMember(param)
Point::Point(const double& x, const double& y) : _x(x), _y(y) {}

// Function members
double Point::getX() const
{
    return _x;
}

double Point::getY() const
{
    return _y;
}

Point::~Point()
{
    // class destructor
}


void Point::move(const double& dx, const double& dy)
{
    _x += dx;
    _y += dy;
}


// Require rule of three
// C++ provides implicit implementation for the copy constructor
// copy operator and destructor
// And the rule of 3 says, if you override one of them, you should override all of them
const Point& Point::operator= (const Point& rhs)
{
    // We are comparing the reference cause this returns a memory address reference
    if (this != &rhs) { // copy operator overloding compare the addresses of the object
        _x = rhs.getX();
        _y = rhs.getY();
    }
    // Make sure the = operator is chainable
    return *this; // return a pointer to the copied object
}

Point::operator std::string() const
{
    char result[20];
    std::sprintf(result, "{x: %f, y: %f}", _x, _y);
    return std::string(result);
}

std::ostream& operator << (std::ostream& lhs, const Point& rhs)
{
    return lhs << std::string(rhs);
}
