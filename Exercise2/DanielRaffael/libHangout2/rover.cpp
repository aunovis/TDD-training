#include "rover.h"

namespace Hangout2
{
	bool Grid::IsFree(Pos position)
	{
		return false;
	}


	Rover::Rover(const Grid& grid, Pos position, Dir direction)
	{
	}

	void Rover::QueueCommands(const char* commands)
	{
		
	}

	TickResult Rover::Tick()
	{
		return TickResult::Idle;
	}
}
