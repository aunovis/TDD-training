using MarsRover;
using Xunit;

namespace MarsRoverTests
{
    public class MarsRoverTests
    {
        [Fact]
        public void ExecutesForwardNorthCommand()
        {
            var rover = new Rover(3, 4, Direction.North);
            var command = new[] { 'f' };
            rover.Execute(command);
            Assert.Equal((3, 3), rover.Position);
        }

        [Fact]
        public void ExecutesForwardWestCommand()
        {
            var rover = new Rover(3, 4, Direction.West);
            var command = new[] { 'f' };
            rover.Execute(command);
            Assert.Equal((2, 4), rover.Position);
        }

        [Fact]
        public void ExecutesForwardSouthCommand()
        {
            var rover = new Rover(3, 4, Direction.South);
            var command = new[] { 'f' };
            rover.Execute(command);
            Assert.Equal((3, 5), rover.Position);
        }

        [Fact]
        public void ExecutesForwardEastCommand()
        {
            var rover = new Rover(3, 4, Direction.East);
            var command = new[] { 'f' };
            rover.Execute(command);
            Assert.Equal((4, 4), rover.Position);
        }

        [Fact]
        public void ExecutesBackwardNorthCommand()
        {
            var rover = new Rover(3, 4, Direction.North);
            var command = new[] { 'b' };
            rover.Execute(command);
            Assert.Equal((3, 5), rover.Position);
        }

        [Fact]
        public void ExecutesBackwardWestCommand()
        {
            var rover = new Rover(3, 4, Direction.West);
            var command = new[] { 'b' };
            rover.Execute(command);
            Assert.Equal((4, 4), rover.Position);
        }

        [Fact]
        public void ExecutesBackwardSouthCommand()
        {
            var rover = new Rover(3, 4, Direction.South);
            var command = new[] { 'b' };
            rover.Execute(command);
            Assert.Equal((3, 3), rover.Position);
        }

        [Fact]
        public void ExecutesBackwardEastCommand()
        {
            var rover = new Rover(3, 4, Direction.East);
            var command = new[] { 'b' };
            rover.Execute(command);
            Assert.Equal((2, 4), rover.Position);
        }

        [Fact]
        public void ExecutesTurnLeftCommand()
        {
            var rover = new Rover(3, 4, Direction.North);
            var command = new[] { 'l' };
            rover.Execute(command);
            Assert.Equal(Direction.West, rover.Direction);
            rover.Execute(command);
            Assert.Equal(Direction.South, rover.Direction);
            rover.Execute(command);
            Assert.Equal(Direction.East, rover.Direction);
            rover.Execute(command);
            Assert.Equal(Direction.North, rover.Direction);
        }

        [Fact]
        public void ExecutesTurnRightCommand()
        {
            var rover = new Rover(3, 4, Direction.North);
            var command = new[] { 'r' };
            rover.Execute(command);
            Assert.Equal(Direction.East, rover.Direction);
            rover.Execute(command);
            Assert.Equal(Direction.South, rover.Direction);
            rover.Execute(command);
            Assert.Equal(Direction.West, rover.Direction);
            rover.Execute(command);
            Assert.Equal(Direction.North, rover.Direction);
        }
    }
}
