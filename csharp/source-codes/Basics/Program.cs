using System;
using Geometry;

namespace Basics
{
    class Program
    {
        static void Main(string[] args)
        {
            Func<(double, double), double> Func = ((double x, double y) p) => p.x * p.y;

            Func<(double, double), double> Func2 = ((double x, double y) p) => p.x + p.y;

            Coord coords = new Coord(1.0, 2.0);

            Point p = Point.Create(coords);
            Console.WriteLine("Hello {0}!", "Azandrew Sidoine");

            Console.WriteLine("Coordinates: {0}", p.GetCoordinate());

            p = p.Move(-3.0, 4.0);

            p = p.Move(4.5, 7.0);

            Console.WriteLine("New P Coordinates: {0}", p.GetCoordinate());

            Console.WriteLine("Multiplication Result: {0}", HigherOrderFunc(Func, 10, 20));

            Console.WriteLine("Addition  Result: {0}", HigherOrderFunc(Func2, 10, 20));

            Console.WriteLine("Path: {0}", $"{nameof(Finger.RTHB)}.data");
        }

        internal enum Finger
        {
               RTHB = 1,
                RINDX = 2,
                RMID = 3,
                RRING = 4,
                RPINK = 5,
                LTHB = 6,
                LINDX = 7,
                LMID = 8,
                LRING = 9,
                LPINK = 10
        }

        public static K  HigherOrderFunc<T, K>(Func<(T, T), K> func, T num1, T num2)
        {
            return func((num1, num2));
        }
    }
}
