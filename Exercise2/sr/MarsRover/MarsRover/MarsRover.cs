using System;
using System.Collections.Generic;
using System.Text;

namespace MarsRover
{
    public class MarsRover
    {
        public int Row { get; private set; }

        public int Column { get; private set; }

        public Direction Direction { get; private set; }

        public Func<int, MapPart, int> CalcNextPart { get; set; }
        public Func<int, MapPart, int> CalcPrevCalcNext { get; set; }
        public Func<int, MapPart, int> CalcCurrentCalcNext { get; set; }

        public MarsRover(int row, int column, Direction direction)
        {
            Row = row;
            Column = column;
            Direction = direction;
        }

        public bool RunSequence(IEnumerable<char> commands)
        {
            throw new NotImplementedException();
        }

        public bool Execute(char command)
        {
            throw new NotImplementedException();
        }

        public bool CanExecute(char nextCommand)
        {
            throw new NotImplementedException();
        }
    }
}
