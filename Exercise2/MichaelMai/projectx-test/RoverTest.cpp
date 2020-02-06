#include "gmock/gmock.h"

#include "Rover.h"

using namespace testing;

namespace projectx::tests
{
	TEST(RoverTests, MoveForward) {

		Rover r(0, 0, 0);			// 0: N, 1: O, 2: S, 3: W

		r.MoveForward();

		std::tuple<int, int, int> result = r.getStatus();
		
		ASSERT_EQ(0, std::get<0>(result));
		ASSERT_EQ(1, std::get<1>(result));
		ASSERT_EQ(0, std::get<2>(result));
	}

	TEST(RoverTests, MoveBackward) {

		Rover r(0, 0, 0);			// 0: N, 1: O, 2: S, 3: W

		r.MoveBackward();
		
		std::tuple<int, int, int> result = r.getStatus();

		ASSERT_EQ(0, std::get<0>(result));
		ASSERT_EQ(-1, std::get<1>(result));
		ASSERT_EQ(0, std::get<2>(result));
	}

	TEST(RoverTests, TurnLeft) {

		Rover r(0, 0, 0);			// 0: N, 1: O, 2: S, 3: W

		r.TurnLeft();

		std::tuple<int, int, int> result = r.getStatus();

		ASSERT_EQ(0, std::get<0>(result));
		ASSERT_EQ(0, std::get<1>(result));
		ASSERT_EQ(3, std::get<2>(result));
	}

	TEST(RoverTests, TurnRight) {

		Rover r(0, 0, 0);			// 0: N, 1: O, 2: S, 3: W

		r.TurnRight();

		std::tuple<int, int, int> result = r.getStatus();

		ASSERT_EQ(0, std::get<0>(result));
		ASSERT_EQ(0, std::get<1>(result));
		ASSERT_EQ(1, std::get<2>(result));
	}	
}