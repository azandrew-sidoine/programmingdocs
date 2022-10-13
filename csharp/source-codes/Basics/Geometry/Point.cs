using Geometry.Contracts;

namespace Geometry
{
    public class Point
    {
        public readonly ICoord Coord;

        public static Point Create(ICoord p)
        {
            return new Point(p);
        }

        private Point(ICoord p)
        {
            Coord = p;
        }

        public Point Move(double dx, double dy)
        {
            var p = new Point(new Coord(Coord.X + dx, Coord.Y + dy ));
            return p;
        }

        public ICoord GetCoordinate()
        {
            return Coord;
        }
    }
}
