using System.Numerics;

namespace MarsRover
{
    public class Rover
    {
        public (int, int) Position { get; }
        private Direction Direction { get; }

        public Rover(int x, int y, Direction direction)
            : this((x, y), direction)
        { }

        public Rover((int, int) position, Direction direction)
        {
            Position = position;
            Direction = direction;
        }

        public void Execute(char[] commands)
        {
            var v = new Vector<int>([-1,0]);
            foreach (var command in commands)
            {
                switch (command)
                {
                    case 'f':

                }
            }
        }

    }
}
