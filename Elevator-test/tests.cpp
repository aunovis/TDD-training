#include "gmock/gmock.h"

#include "elevator.h"

using namespace testing;

namespace elevator::tests
{
	TEST(ElevatorTests, LiftInstallation)
	{
		const size_t expected_floor_count = 7;

		LiftInstallation installation;
		Lift lift;
		std::tie(installation, lift) = lift_create_installation(expected_floor_count);

		ASSERT_THAT(installation.floor_count, Eq(expected_floor_count));
		ASSERT_THAT(lift.current_floor, Eq(0));
		ASSERT_THAT(lift.destination_floor, Eq(0));
	}
}
