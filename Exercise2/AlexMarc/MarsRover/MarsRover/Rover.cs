namespace MarsRover
{
    public class Rover
    {
        private (int x, int y) _position;
        public (int x, int y) Position => _position;

        public Direction Direction { get; private set; }

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
                switch (command)
                {
                    case 'f':
                    case 'b':
                        {
                            var move = command == 'f' ? 1 : -1;
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

                            break;
                        }
                    case 'r':
                    case 'l':
                        Direction = (Direction)(((int)Direction + (command == 'r' ? 1 : -1) + 4) % 4);
                        break;
                }
            }
        }

    }
}
