using System;
using System.ComponentModel;
using MarsRover;
using Xunit;

namespace MarsRoverTests
{
    public class MarsRoverTests
    {
        [Fact]
        public void ExecutesForwardCommand()
        {
            var rover = new Rover(3, 4, Direction.West);
            var command = new [] {'f'};
            rover.Execute(command);
            Assert.Equal((2, 4), rover.Position);
        }
    }
}
