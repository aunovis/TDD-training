namespace MarsRover
{
    public class Rover
    {
        private (int x, int y) _position;
        public (int x, int y) Position => _position;

        private Direction Direction { get; }

        public Rover(int x, int y, Direction direction)
            : this((x, y), direction)
        { }

        public Rover((int x, int y) position, Direction direction)
        {
            _position = position;
            Direction = direction;
        }

        public void Execute(char[] commands)
        {
            foreach (var command in commands)
            {
                var move = command == 'f' ? 1 : (command == 'r' ? -1 : 0);
                switch (Direction)
                {
                    case Direction.North:
                        _position.y -= move;
                        break;
                    case Direction.South:
                        _position.y += move;
                        break;
                    case Direction.West:
                        _position.x -= move;
                        break;
                    case Direction.East:
                        _position.x += move;
                        break;
                }
            }
        }

    }
}
