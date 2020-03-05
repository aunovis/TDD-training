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
    }
}
