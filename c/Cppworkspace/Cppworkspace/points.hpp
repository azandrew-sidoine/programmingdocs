//
//  points.hpp
//  Cppworkspace
//
//  Created by LIKSOFT on 24/02/2021.
//

#ifndef __POINTS_
#define __POINTS_

#include <string>
#include <iostream>


class Point
{
    double _x, _y = 0;
    
//    Point(); // Prevent to create an instance of Point calling the default constructor
    // With this, Point p; will generate error
public:
    // Default constructor
    Point();
    // Copy constructor
    Point(const Point&) ;
    // Constructor with parameter
    // Adding explicit to this prevent compiler to implicitly cast
    // constructor parameter
    Point(const double&, const double&);
    // Class destructor
    ~Point();
    
    // Operators overloading
    const Point& operator= (const Point& rhs);
    operator std::string () const;
    
    // Function members
    double getX() const;
    
    double getY() const;

    // Move the point from it origin to new coordinates
    void move(const double&, const double&);
};

#endif /* __POINTS_ */
