#include "Point.hpp"

Point::Point() : Point(0, 0) {}

Point::Point(int x_, int y_) : x(x_), y(y_) {}

void Point::Move(int dx, int dy) {
  x += dx;
  y += dy;
}

void Point::Move(int dx) { x += dx; }

const Point Point::Copy() const { return Point{x, y}; }

int Point::GetX() const { return x; }

int Point::GetY() const { return y; }

Point::~Point() {}