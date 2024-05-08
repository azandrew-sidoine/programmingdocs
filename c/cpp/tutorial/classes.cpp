#include <iostream>
// Just like C++ structs, the ; should not be omitted else it will result in
// compilation error
class Point {
  // public members declarations
public:
  double getX();
  double getY();
  void move(float dx);
  void move(float dx, float dy);

  // Constructors
  // Default constructor
  Point() = default;

  // Parameterized constructor
  Point(float x, float y) : x(x), y(y) {}

  // Initialize only x data member
  Point(float x) : Point(x, 0) {}
  // private fields / members
private:
  double x;
  double y;
};

// Display point
void printPoint(Point);

// Here we provide class methods definition
double Point::getX() { return x; }

double Point::getY() { return y; }

void Point::move(float dx) { x += dx; }

void Point::move(float dx, float dy) {
  x += dx;
  y += dy;
}

int main() {
  Point p{-5};
  printPoint(p);

  // 
  std::cout << "Moving point dx: 4" << std::endl;
  p.move(4);
  printPoint(p);

  //
  std::cout << "Moving point dx: -3, dy: -2" << std::endl;
  p.move(-3, -2);
  printPoint(p);

  return 0;
}

void printPoint(Point p) {
  std::cout << "Point origin: X = { " << p.getX() << " ; " << p.getY()
            << "}; \n";
}