//
//  rational.cpp
//  Cppworkspace
//
//  Created by LIKSOFT on 01/03/2021.
//

#include "rational.hpp"

Rational::~Rational()
{
    reset();
}

// pubblic methods
void Rational::reset()
{
    _n = 0; _d = 1;
    if (_buf) {
        delete [] _buf;
    }
    _buf = nullptr;
}

// Operators overloading defitions
Rational&  Rational::operator = (Rational rhs)
{
    // A temporary copy of the rhs param is made when assigning value
    // The copy will goes out of scope when the operator complete
    swap(rhs);
    return *this;
}

Rational Rational::operator + (const Rational& rhs) const
{
    return Rational{(_n * rhs.denominator()) + (_d * rhs.numerator()), _d * rhs.denominator()};
}

Rational Rational::operator - (const Rational& rhs) const
{
    return Rational((_n * rhs.denominator()) - (_d * rhs.numerator()), _d * rhs.denominator());
}

Rational  Rational::operator * (const Rational& rhs) const
{
    return Rational(_n * rhs.numerator(), _d * rhs.denominator());
}

Rational Rational::operator / (const Rational& rhs) const
{
    return Rational(_n * rhs.denominator(), _d * rhs.numerator());
}

Rational::operator std::string () const
{
    return string();
}

std::string Rational::string() const
{
    return std::string(c_str());
}
const char*  Rational::c_str() const
{
    if (!_buf) {
        _buf = new char[_bufsize]();
    }
    snprintf(_buf, _bufsize, "%d/%d", _n, _d);
    return _buf;
}

// Move constructor
Rational::Rational(Rational&& rhs) noexcept
{
    _n = std::move(rhs.numerator());
    _d = std::move(rhs.denominator());
    rhs.reset();
}


void Rational::swap(Rational& rhs)
{
    // Note : The pointer allow us to access the private members value
    std::swap(_n, rhs._n);
    std::swap(_d, rhs._d);
}
