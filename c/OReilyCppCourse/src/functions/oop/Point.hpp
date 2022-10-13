#ifndef POINT_H
#define POINT_H
#pragma once
	
class Point  
{
	private:
		int x;
		int y;
	public:

		Point();
		Point(int x_, int y_);

		void Move(int dx, int dy);

		void Move(int dx);

		const Point Copy() const;
	
		int GetX() const;
		int GetY() const;

		~Point();

};
#endif