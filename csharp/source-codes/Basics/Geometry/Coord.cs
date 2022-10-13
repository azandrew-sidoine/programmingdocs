using Geometry.Contracts;

namespace Geometry
{
    public class Coord : ICoord
    {

        public double X { get; }

        public double Y { get; }

        public Coord(double x, double y)
        {
            X = x;
            Y = y;
        }

        public override string ToString()
        {
            return $"{{ x: {X:f2}, y: {X:f2} }}";
        }
    }
}
