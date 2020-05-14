using System.Collections.Generic;
using System.Linq;

namespace ElevatorSimulator
{
    public class Elevator
    {
        public int CurrentFloor { get; private set; }
        public Direction CurrentDirection { get; private set; }
        //public List<(Direction direction, int destination)> Calls { get; }
        public List<(int floor, Direction direction)> OutsideCalls { get; }

        public Elevator(int startFloor)
        {
            CurrentFloor = startFloor;
            CurrentDirection = Direction.None;
            OutsideCalls = new List<(int floor, Direction direction)>();
        }

        public void Call(int floor, Direction direction)
        {
            OutsideCalls.Add((floor, direction));
        }

        public void Tick()
        {
            if (!OutsideCalls.Any()) return;

            if (OutsideCalls[0].floor > CurrentFloor)
            {
                CurrentDirection = Direction.Up;
                CurrentFloor++;
            }
            else if (OutsideCalls[0].floor < CurrentFloor)
            {
                CurrentDirection = Direction.Down;
                CurrentFloor--;
            }
            else
            {
                CurrentDirection = OutsideCalls[0].direction;
                OutsideCalls.RemoveAt(0);
            }
        }
    }
}