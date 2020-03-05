#pragma once

#include <cstdint>
#include <functional>
#include <tuple>

namespace elevator
{
	using FloorIndex = int32_t;

	enum class Direction
	{
		Up,
		Down,
	};

	struct LiftSignals
	{
		std::function<void(FloorIndex)> at_floor;
		std::function<void()> doors_opened;
		std::function<void()> doors_closed;
	};

	struct Lift
	{
		FloorIndex current_floor;		// Floor that the lift is current on/moving past
		FloorIndex destination_floor;	// Destination floor of the currently served request

		LiftSignals signals;			// Signals to observe what the lift is doing
	};

	struct Floor
	{
		bool has_request;
		Direction direction;
	};

	struct LiftInstallation
	{
		size_t floor_count;
		Floor floors[];
	};

	std::tuple<LiftInstallation, Lift> lift_create_installation(size_t floor_count)
	{
		return std::make_tuple(LiftInstallation{}, Lift{});
	}

	void lift_tick(LiftInstallation const& installation, Lift const& lift)
	{

	}
}
