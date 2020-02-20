using System.Collections.Generic;
using MarsRover;
using Xunit;

namespace MarsRoverTests
{
    public class MarsRoverTest
    {
        [Fact]
        public void MovesRoverAndReportsObstacle()
        {
            var testCases = new List<((int Row, int Column, char Direction) Start, string Sequence, (int Row, int Column, char Direction, (int Row, int Column) Obstacle) Result)>
            {
                (Start: (Row: 2, Column: 2, Direction: 'N'), Sequence: @"FFLFF", Result: (Row: 0, Column: 0, Direction:'W', Obstacle: (Row: -1, Column: -1))),
                (Start: (Row: 2, Column: 2, Direction: 'E'), Sequence: @"FLFF", Result: (Row: 0, Column: 0, Direction:'N', Obstacle: (Row: -1, Column: -1))),
                (Start: (Row: 2, Column: 2, Direction: 'S'), Sequence: @"FRFF", Result: (Row: 0, Column: 0, Direction:'W', Obstacle: (Row: -1, Column: -1))),
                (Start: (Row: 2, Column: 2, Direction: 'W'), Sequence: @"FFRFF", Result: (Row: 0, Column: 0, Direction:'N', Obstacle: (Row: -1, Column: -1))),

                (Start: (Row: 2, Column: 2, Direction: 'N'), Sequence: @"BRBB", Result: (Row: 0, Column: 0, Direction:'E', Obstacle: (Row: -1, Column: -1))),
                (Start: (Row: 2, Column: 2, Direction: 'E'), Sequence: @"BBRBB", Result: (Row: 0, Column: 0, Direction:'S', Obstacle: (Row: -1, Column: -1))),
                (Start: (Row: 2, Column: 2, Direction: 'S'), Sequence: @"BBLBB", Result: (Row: 0, Column: 0, Direction:'E', Obstacle: (Row: -1, Column: -1))),
                (Start: (Row: 2, Column: 2, Direction: 'W'), Sequence: @"BLBB", Result: (Row: 0, Column: 0, Direction:'S', Obstacle: (Row: -1, Column: -1))),

                (Start: (Row: 2, Column: 1, Direction: 'N'), Sequence: @"F", Result: (Row: 2, Column: 1, Direction:'N', Obstacle: (Row: 1, Column: 1))),
                (Start: (Row: 1, Column: 0, Direction: 'E'), Sequence: @"F", Result: (Row: 1, Column: 0, Direction:'E', Obstacle: (Row: 1, Column: 1))),
                (Start: (Row: 0, Column: 1, Direction: 'S'), Sequence: @"F", Result: (Row: 0, Column: 1, Direction:'S', Obstacle: (Row: 1, Column: 1))),
                (Start: (Row: 1, Column: 2, Direction: 'W'), Sequence: @"F", Result: (Row: 1, Column: 2, Direction:'W', Obstacle: (Row: 1, Column: 1))),

                (Start: (Row: 0, Column: 1, Direction: 'N'), Sequence: @"B", Result: (Row: 0, Column: 1, Direction:'N', Obstacle: (Row: 1, Column: 1))),
                (Start: (Row: 1, Column: 2, Direction: 'E'), Sequence: @"B", Result: (Row: 1, Column: 2, Direction:'E', Obstacle: (Row: 1, Column: 1))),
                (Start: (Row: 2, Column: 1, Direction: 'S'), Sequence: @"B", Result: (Row: 2, Column: 1, Direction:'S', Obstacle: (Row: 1, Column: 1))),
                (Start: (Row: 1, Column: 0, Direction: 'W'), Sequence: @"B", Result: (Row: 1, Column: 0, Direction:'W', Obstacle: (Row: 1, Column: 1))),

                (Start: (Row: 0, Column: 0, Direction: 'N'), Sequence: @"F", Result: (Row: 0, Column: 0, Direction:'N', Obstacle: (Row: 2, Column: 0))),
                (Start: (Row: 0, Column: 2, Direction: 'E'), Sequence: @"F", Result: (Row: 0, Column: 2, Direction:'E', Obstacle: (Row: 0, Column: 0))),
                (Start: (Row: 2, Column: 0, Direction: 'S'), Sequence: @"F", Result: (Row: 2, Column: 0, Direction:'S', Obstacle: (Row: 0, Column: 0))),
                (Start: (Row: 0, Column: 0, Direction: 'W'), Sequence: @"F", Result: (Row: 0, Column: 0, Direction:'W', Obstacle: (Row: 0, Column: 2))),

                (Start: (Row: 2, Column: 0, Direction: 'N'), Sequence: @"B", Result: (Row: 2, Column: 0, Direction:'N', Obstacle: (Row: 0, Column: 0))),
                (Start: (Row: 0, Column: 0, Direction: 'E'), Sequence: @"B", Result: (Row: 0, Column: 0, Direction:'E', Obstacle: (Row: 0, Column: 2))),
                (Start: (Row: 0, Column: 2, Direction: 'S'), Sequence: @"B", Result: (Row: 0, Column: 2, Direction:'S', Obstacle: (Row: 2, Column: 2))),
                (Start: (Row: 2, Column: 2, Direction: 'W'), Sequence: @"B", Result: (Row: 2, Column: 2, Direction:'W', Obstacle: (Row: 2, Column: 0))),

                (Start: (Row: 2, Column: 2, Direction: 'N'), Sequence: @"FFLFFLFFLFF", Result: (Row: 2, Column: 2, Direction:'E', Obstacle: (Row: -1, Column: -1))),
                (Start: (Row: 2, Column: 0, Direction: 'E'), Sequence: @"FFLFFLFFLFF", Result: (Row: 2, Column: 0, Direction:'S', Obstacle: (Row: -1, Column: -1))),
                (Start: (Row: 0, Column: 0, Direction: 'S'), Sequence: @"FFLFFLFFLFF", Result: (Row: 0, Column: 0, Direction:'W', Obstacle: (Row: -1, Column: -1))),
                (Start: (Row: 0, Column: 2, Direction: 'W'), Sequence: @"FFLFFLFFLFF", Result: (Row: 0, Column: 2, Direction:'N', Obstacle: (Row: -1, Column: -1))),
            };

            testCases.ForEach(testCase =>
            {
                // Given
                var size = (Rows: 3, Columns: 3);
                var sut = new MarsRover.MarsRover(testCase.Start.Row, testCase.Start.Column, testCase.Start.Direction)
                {
                    CalcNext = (current, part) => part == MapPart.Row ? (current + 1) % size.Rows : (current + 1) % size.Columns,
                    CalcPrev = (current, part) => part == MapPart.Row ? (current + size.Rows - 1) % size.Rows : (current + size.Columns - 1) % size.Columns,
                    IsObstacle = (row, column) => testCase.Result.Obstacle.Row == row && testCase.Result.Obstacle.Column == column
                };

                // When
                var actual = sut.RunCommands(testCase.Sequence);

                // Then
                Assert.Equal(testCase.Result.Row, actual.Position.Row);
                Assert.Equal(testCase.Result.Column, actual.Position.Column);
                Assert.Equal(testCase.Result.Direction, actual.Position.Direction);
                Assert.Equal(testCase.Result.Obstacle.Row, actual.Obstacle.Row);
                Assert.Equal(testCase.Result.Obstacle.Column, actual.Obstacle.Column);
            });
        }
    }
}
