//
//  rational.hpp
//  Cppworkspace
//
//  Created by LIKSOFT on 01/03/2021.
//

#ifndef __RATIONAL_
#define __RATIONAL_

#include <stdio.h>
#include <string>
#include <utility>


class Rational
{
    int  _n  =  0; int _d = 0;
    static const int _bufsize = 120;
    mutable char* _buf = nullptr;

    public:
        Rational(): _n(0), _d(1) { reset(); }
        Rational(const int& n): _n(n), _d(1) {}
        Rational(const int& n, const int& d): _n(n), _d(d) {}
        Rational(const Rational& rhs) : _n(rhs.numerator()), _d(rhs.denominator()) {}

        // Adding move constructor
        Rational(Rational&&) noexcept;
        ~Rational();

        const int& numerator() const
        {
            return _n;
        }
        const int& denominator() const
        {
            return _d;
        }

        // pubblic methods
        void  reset();
        void swap(Rational& rhs);

        // Operators overloading defitions
        Rational&  operator = (Rational);
        Rational  operator + (const Rational&) const;
        Rational  operator - (const Rational&) const;
        Rational  operator * (const Rational&) const;
        Rational  operator / (const Rational&) const;
        operator std::string () const;
        std::string string() const;
        const char*  c_str() const;
};

#endif /* rational_hpp */
