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
}
