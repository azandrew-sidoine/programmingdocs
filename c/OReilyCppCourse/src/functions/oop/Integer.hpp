#ifndef INTEGER_H
#define INTEGER_H
#pragma once
	
class Integer  
{
	private:
		int* value_{new int(0)};
	public:
		// Default constructor
		Integer() = default;
		// Integer();
		// Parameterized constructor
		Integer(int value);
		
		// Copy constructor
		Integer(const Integer& source);
	
		// Move constructor
		Integer(Integer&& source);

		int GetValue() const;

		void SetValue(int value);

		// Operators overloading
		// operator= (const Integer rhs);

		// Destructor
		~Integer();

};
#endif