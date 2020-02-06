using MarsRover;
using System;
using System.Linq;
using Xunit;

namespace MarsRoverTests
{
    public class MapTest
    {
        [Fact]
        public void InitsMap()
        {
            var sut = new Map(3, 2);

            Assert.False(sut.IsObstacle(0, 0));
            Assert.False(sut.IsObstacle(1, 0));
            Assert.False(sut.IsObstacle(2, 0));
            Assert.False(sut.IsObstacle(0, 1));
            Assert.False(sut.IsObstacle(1, 1));
            Assert.False(sut.IsObstacle(2, 1));
        }

        [Fact]
        public void AddsObstacle()
        {
            var sut = new Map(3, 2);

            sut.AddObstacle(1, 1);

            Assert.False(sut.IsObstacle(0, 0));
            Assert.False(sut.IsObstacle(1, 0));
            Assert.False(sut.IsObstacle(2, 0));
            Assert.False(sut.IsObstacle(0, 1));
            Assert.True(sut.IsObstacle(1, 1));
            Assert.False(sut.IsObstacle(2, 1));
        }

        [Fact]
        public void GetsNextMapPart()
        {
            var sut = new Map(4, 3);
            var testCases = new[]
            {
                (Current: 0, Part: MapPart.Row, Expected: 1),
                (Current: 1, Part: MapPart.Row, Expected: 2),
                (Current: 2, Part: MapPart.Row, Expected: 3),
                (Current: 3, Part: MapPart.Row, Expected: 0),

                (Current: 0, Part: MapPart.Column, Expected: 1),
                (Current: 1, Part: MapPart.Column, Expected: 2),
                (Current: 2, Part: MapPart.Column, Expected: 0),
            };

            var results = testCases.Select(testCase => sut.Next(testCase.Current, testCase.Part)).ToArray();

            Assert.Equal(testCases.Select(testCase => testCase.Expected), results);
        }

        [Fact]
        public void GetsPreviousMapPart()
        {
            var sut = new Map(4, 3);
            var testCases = new[]
            {
                (Current: 3, Part: MapPart.Row, Expected: 2),
                (Current: 2, Part: MapPart.Row, Expected: 1),
                (Current: 1, Part: MapPart.Row, Expected: 0),
                (Current: 0, Part: MapPart.Row, Expected: 3),

                (Current: 2, Part: MapPart.Column, Expected: 1),
                (Current: 1, Part: MapPart.Column, Expected: 0),
                (Current: 0, Part: MapPart.Column, Expected: 2),
            };

            var results = testCases.Select(testCase => sut.Previous(testCase.Current, testCase.Part)).ToArray();

            Assert.Equal(testCases.Select(testCase => testCase.Expected), results);
        }

        [Fact]
        public void GetCurrentMapPart()
        {
            var sut = new Map(4, 3);
            var testCases = new[]
            {
                (Current: 4, Part: MapPart.Row, Expected: 0),
                (Current: 3, Part: MapPart.Row, Expected: 3),
                (Current: 2, Part: MapPart.Row, Expected: 2),
                (Current: 1, Part: MapPart.Row, Expected: 1),
                (Current: 0, Part: MapPart.Row, Expected: 0),
                (Current: -1, Part: MapPart.Row, Expected: 3),

                (Current: 3, Part: MapPart.Column, Expected: 0),
                (Current: 2, Part: MapPart.Column, Expected: 2),
                (Current: 1, Part: MapPart.Column, Expected: 1),
                (Current: 0, Part: MapPart.Column, Expected: 0),
                (Current: -1, Part: MapPart.Column, Expected: 2),
            };

            var results = testCases.Select(testCase => sut.Current(testCase.Current, testCase.Part)).ToArray();

            Assert.Equal(testCases.Select(testCase => testCase.Expected), results);
        }
    }
}
