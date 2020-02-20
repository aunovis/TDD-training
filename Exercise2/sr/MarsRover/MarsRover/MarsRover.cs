namespace MarsRover
{
    public delegate int CalculatePositionDelegate(int current, MapPart part);
    public delegate bool IsObstacleDelegate(int row, int column);

    public class MarsRover
    {
        private int _row;
        private int _column;
        private char _direction;

        public CalculatePositionDelegate CalcNext { get; set; }
        public CalculatePositionDelegate CalcPrev { get; set; }
        public IsObstacleDelegate IsObstacle { get; set; }

        public MarsRover(int row, int column, char direction)
        {
            _row = row;
            _column = column;
            _direction = direction;
        }

        public ((int Row, int Column, char Direction) Position, (int Row, int Column) Obstacle) RunCommands(string commands)
        {
            foreach (var next in commands)
            {
                switch (next)
                {
                    case 'L':
                        TurnLeft();
                        break;
                    case 'R':
                        TurnRight();
                        break;
                    case 'F':
                        {
                            var obstacle = MoveForward();
                            if (obstacle.Row >= 0 && obstacle.Column >= 0)
                            {
                                return (Position: (_row, _column, _direction), Obstacle: obstacle);
                            }
                            break;
                        }
                    case 'B':
                        {
                            var obstacle = MoveBackward();
                            if (obstacle.Row >= 0 && obstacle.Column >= 0)
                            {
                                return (Position: (_row, _column, _direction), Obstacle: obstacle);
                            }
                            break;
                        }
                }
            }
            return (Position: (_row, _column, _direction), Obstacle: (-1, -1));
        }

        private void TurnLeft()
        {
            switch (_direction)
            {
                case 'N':
                    _direction = 'W';
                    break;
                case 'E':
                    _direction = 'N';
                    break;
                case 'S':
                    _direction = 'E';
                    break;
                case 'W':
                    _direction = 'S';
                    break;
            }
        }

        private void TurnRight()
        {
            switch (_direction)
            {
                case 'N':
                    _direction = 'E';
                    break;
                case 'E':
                    _direction = 'S';
                    break;
                case 'S':
                    _direction = 'W';
                    break;
                case 'W':
                    _direction = 'N';
                    break;
            }
        }

        private (int Row, int Column) MoveForward()
        {
            switch (_direction)
            {
                case 'N':
                    {
                        var next = CalcPrev(_row, MapPart.Row);
                        if (IsObstacle(next, _column)) return (next, _column);
                        _row = next;
                        return (-1, -1);
                    }
                case 'E':
                    {
                        var next = CalcNext(_column, MapPart.Column);
                        if (IsObstacle(_row, next)) return (_row, next);
                        _column = next;
                        return (-1, -1);
                    }
                case 'W':
                    {
                        var next = CalcPrev(_column, MapPart.Column);
                        if (IsObstacle(_row, next)) return (_row, next);
                        _column = next;
                        return (-1, -1);
                    }
                case 'S':
                    {
                        var next = CalcNext(_row, MapPart.Row);
                        if (IsObstacle(next, _column)) return (next, _column);
                        _row = next;
                        return (-1, -1);
                    }
                default:
                    return (-1, -1);
            }
        }

        private (int Row, int Column) MoveBackward()
        {
            switch (_direction)
            {
                case 'N':
                    {
                        var next = CalcNext(_row, MapPart.Row);
                        if (IsObstacle(next, _column)) return (next, _column);
                        _row = next;
                        return (-1, -1);
                    }
                case 'E':
                    {
                        var next = CalcPrev(_column, MapPart.Column);
                        if (IsObstacle(_row, next)) return (_row, next);
                        _column = next;
                        return (-1, -1);
                    }
                case 'W':
                    {
                        var next = CalcNext(_column, MapPart.Column);
                        if (IsObstacle(_row, next)) return (_row, next);
                        _column = next;
                        return (-1, -1);
                    }
                case 'S':
                    {
                        var next = CalcPrev(_row, MapPart.Row);
                        if (IsObstacle(next, _column)) return (next, _column);
                        _row = next;
                        return (-1, -1);
                    }
                default:
                    return (-1, -1);
            }
        }
    }
}
