using ElevatorSimulator;
using Xunit;

namespace ElevatorSimulatorUnitTests
{
    public class ElevatorTests
    {
        [Fact]
        public void InitialFloorTest()
        {
            var elevator = new Elevator(5);
            Assert.Equal(5, elevator.CurrentFloor);
        }

        [Fact]
        public void OutsideCallTest()
        {
            var elevator = new Elevator(5);
            elevator.Call(4, Direction.Up);
            elevator.Tick();
            Assert.Equal(4, elevator.CurrentFloor);
            Assert.Equal(Direction.Down, elevator.CurrentDirection);
            elevator.Tick();
            Assert.Equal(4, elevator.CurrentFloor);
            Assert.Equal(Direction.Up, elevator.CurrentDirection);
        }
    }
}
