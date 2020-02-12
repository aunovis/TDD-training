using System.Collections.Generic;

namespace MarsRover
{
    public class World
    {
        public World(int x, int y)
        {
            Dimension = (x, y);
            Obstacles = new List<(int x, int y)>();
        }

        public (int x, int y) Dimension { get; }
        public List<(int x, int y)> Obstacles { get; }
    }
}
