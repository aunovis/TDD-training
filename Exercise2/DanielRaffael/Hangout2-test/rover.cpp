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
}
