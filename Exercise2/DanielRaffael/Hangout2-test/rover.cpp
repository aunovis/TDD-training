#include "gmock/gmock.h"

#include "rover.h"

using namespace testing;

namespace Hangout2::tests
{
	TEST(RoverTests, DefaultRoverState)
	{
		Grid grid{};
		Rover rover{ grid, {0, 0}, Dir::N };

		ASSERT_THAT(rover.Direction(), Eq(Dir::N));
		ASSERT_THAT(rover.Position().x, Eq(0));
		ASSERT_THAT(rover.Position().y, Eq(0));
	}

	TEST(RoverTests, InitializePositionAndDirection)
	{
		Grid grid{};
		Rover rover{ grid, {99, 512}, Dir::E };

		ASSERT_THAT(rover.Direction(), Eq(Dir::E));
		ASSERT_THAT(rover.Position().x, Eq(99));
		ASSERT_THAT(rover.Position().y, Eq(512));
	}

	TEST(RoverTests, NorthFacingRoverMovesForward)
	{
		Grid grid{};
		Rover rover{ grid, {0, 0}, Dir::N };

		rover.QueueCommands("ff");
		rover.Tick();
		ASSERT_THAT(rover.Position().y, Eq(1));
		rover.Tick();
		ASSERT_THAT(rover.Position().y, Eq(2));

		ASSERT_THAT(rover.Position().x, Eq(0));
	}

	TEST(RoverTests, WestFacingRoverMovesBackwards)
	{
		Grid grid{};
		Rover rover{ grid, {0, 0}, Dir::W };

		rover.QueueCommands("bbbb");
		rover.Tick();
		rover.Tick();
		ASSERT_THAT(rover.Position().x, Eq(2));
		rover.Tick();
		rover.Tick();
		ASSERT_THAT(rover.Position().x, Eq(4));

		ASSERT_THAT(rover.Position().y, Eq(0));
	}

	TEST(RoverTests, NorthFacingRoverTurnsAround)
	{
		Grid grid{};
		Rover rover{ grid, {0, 0}, Dir::N };

		rover.QueueCommands("llll");
		rover.Tick();
		ASSERT_THAT(rover.Direction(), Eq(Dir::W));
		rover.Tick();
		ASSERT_THAT(rover.Direction(), Eq(Dir::S));
		rover.Tick();
		ASSERT_THAT(rover.Direction(), Eq(Dir::E));
		rover.Tick();
		ASSERT_THAT(rover.Direction(), Eq(Dir::N));

		rover.QueueCommands("rrrr");
		rover.Tick();
		ASSERT_THAT(rover.Direction(), Eq(Dir::E));
		rover.Tick();
		ASSERT_THAT(rover.Direction(), Eq(Dir::S));
		rover.Tick();
		ASSERT_THAT(rover.Direction(), Eq(Dir::W));
		rover.Tick();
		ASSERT_THAT(rover.Direction(), Eq(Dir::N));
	}

	TEST(RoverTests, NorthFacingRoverTurnsAroundTwice)
	{
		Grid grid{};
		Rover rover{ grid, {0, 0}, Dir::N };

		rover.QueueCommands("llllllll");
		rover.Tick();
		rover.Tick();
		rover.Tick();
		rover.Tick();
		rover.Tick();
		rover.Tick();
		rover.Tick();
		rover.Tick();
		ASSERT_THAT(rover.Direction(), Eq(Dir::N));
	}

	TEST(RoverTests, DefaultGridState)
	{
		Grid grid;

		auto size = grid.GetSize();

		ASSERT_THAT(size, 8);
	}

	TEST(RoverTests, CustomGridState)
	{
		Grid grid{ {false,false,false,
			        false,false,false,
			        false,false,false} };

		auto size = grid.GetSize();

		ASSERT_THAT(size, 3);
	}

	TEST(RoverTests, MoveOutOfGrid)
	{
		Grid grid{ {false,false,false,
					false,false,false,
					false,false,false} };
		Rover rover{ grid, {0, 0}, Dir::N };

		rover.QueueCommands("fff");
		rover.Tick();
		ASSERT_THAT(rover.Position().y, Eq(1));
		rover.Tick();
		ASSERT_THAT(rover.Position().y, Eq(2));
		rover.Tick();
		ASSERT_THAT(rover.Position().y, Eq(0));
	}

	TEST(RoverTests, RoverMovesAgainstObstacles)
	{
		Grid grid{ {true,true,false,
					true,false,false,
					false,false,false} };
		Rover rover{ grid, {0, 2}, Dir::S };

		rover.QueueCommands("f");
		ASSERT_THAT(rover.Tick(), Eq(TickResult::ObstacleEncountered));
		ASSERT_THAT(rover.Position().x, Eq(0));
		ASSERT_THAT(rover.Position().y, Eq(2));

		rover.QueueCommands("lfrff");
		ASSERT_THAT(rover.Tick(), Eq(TickResult::Running));
		ASSERT_THAT(rover.Tick(), Eq(TickResult::Running));
		ASSERT_THAT(rover.Tick(), Eq(TickResult::Running));
		ASSERT_THAT(rover.Tick(), Eq(TickResult::Running));
		ASSERT_THAT(rover.Tick(), Eq(TickResult::ObstacleEncountered));
	}
}
