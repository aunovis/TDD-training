using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Text;
using MarsRover;
using Microsoft.VisualStudio.TestPlatform.ObjectModel.DataCollector.InProcDataCollector;
using Xunit;

namespace MarsRoverTests
{
    public class MarsRoverTest
    {
        [Fact]
        public void SetsInitialPosition()
        {
            var expectedRow = 1;
            var expectedColumn = 2;
            var expectedDirection = Direction.North;

            var sut = new MarsRover.MarsRover(expectedRow, expectedColumn, expectedDirection);

            Assert.Equal(expectedRow, sut.Row);
            Assert.Equal(expectedColumn, sut.Column);
            Assert.Equal(expectedDirection, sut.Direction);
        }
    }
}
