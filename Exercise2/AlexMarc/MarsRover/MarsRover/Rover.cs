namespace MarsRover
{
    public class Rover
    {
        private (int x, int y) _position;
        public (int x, int y) Position => _position;

        public Direction Direction { get; private set; }

        private World _world;

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
                        var origin = _position;
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

                        WrapAroundWorld();
                        if (HitsObstacleAt(_position))
                        {
                            _position = origin;
                            throw new ObstacleException();
                        }
                        break;

                    case 'r':
                    case 'l':
                        Direction = (Direction)(((int)Direction + (command == 'r' ? 1 : -1) + 4) % 4);
                        break;
                }
            }
        }

        public void LandOn(World world)
        {
            _world = world;
        }

        private void WrapAroundWorld()
        {
            if (_world != null)
            {
                _position.x = (_position.x + _world.Dimension.x) % _world.Dimension.x;
                _position.y = (_position.y + _world.Dimension.y) % _world.Dimension.y;
            }
        }

        private bool HitsObstacleAt((int x, int y) position)
        {
            return (_world != null) && _world.Obstacles.Contains(position);
        }
    }
}
