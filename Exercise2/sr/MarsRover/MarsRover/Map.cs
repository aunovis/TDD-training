using System;
using System.Collections.Generic;
using System.Linq;

namespace MarsRover
{
    public class Map
    {
        public readonly int _rows;
        public readonly int _columns;

        public Map(int rows, int columns)
        {
            _obstacles = new List<(int Row, int Column)>();
            _rows = rows;
            _columns = columns;
        }

        public void AddObstacle(int row, int column)
        {
            _obstacles.Add((row, column));
        }

        public bool IsObstacle(int row, int column)
        {
            return _obstacles.Any(obstacle => obstacle.Row == row && obstacle.Column == column);
        }

        private readonly List<(int Row, int Column)> _obstacles;

        public int Next(int current, MapPart part)
            => CalculateNewPosition(current, part, 1);

        public int Previous(int current, MapPart part)
            => CalculateNewPosition(current, part, -1);

        public int Current(int current, MapPart part)
            => CalculateNewPosition(current, part, 0);

        private int CalculateNewPosition(int current, MapPart part, int direction)
        {
            var max = part == MapPart.Row ? _rows : _columns;
            return (current + max + direction) % max;
        }
    }
}