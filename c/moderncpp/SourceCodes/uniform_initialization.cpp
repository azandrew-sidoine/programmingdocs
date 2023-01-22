#include <iostream>
#include <string>

class Point {

private:
  double _x, _y = 0;

public:
  Point() : _x(0), _y(0) {}

  Point(double x, double y) : _x(x), _y(y) {}

  double getX() const { return _x; }

  double getY() const { return _y; }
};

// Delegate constructor
class Point3D {
private:
  double _x, _y, _z = 0;

public:
  Point3D() : _x(0), _y(0), _z(0) {}

  Point3D(double x) : Point3D() { _x = x; }

  Point3D(double x, double y) : Point3D() {
    _x = x;
    _y = y;
  }

  Point3D(double x, double y, double z) : Point3D() {
    _x = x;
    _y = y;
    _z = z;
  }

  double getX() const { return _x; }

  double getY() const { return _y; }

  double getZ() const { return _z; }
};

int main() {

  // All instance are uniformly initialized
  Point p{0, 2};
  std::string str{"Hello World!"};
  int x{19};

  Point3D p1{};
  Point3D p2{0, 2};
  Point3D p3{-1, 4, -5};

  std::cout << "X: " << p.getX() << " Y: " << p.getY() << std::endl;
  std::cout << "String: " << str << std::endl;
  std::cout << "Number: " << x << std::endl;

  std::cout << "Printing 3d point values: " << std::endl;
  std::cout << "X: " << p1.getX() << " Y: " << p1.getY() << " Z: " << p1.getZ()
            << std::endl;
  std::cout << "X: " << p2.getX() << " Y: " << p2.getY() << " Z: " << p2.getZ()
            << std::endl;
  std::cout << "X: " << p3.getX() << " Y: " << p3.getY() << " Z: " << p3.getZ()
            << std::endl;

  return 0;
}