#pragma once

#include <vector>
#include <deque>

namespace Hangout2
{
	struct Pos
	{
		int x, y;
	};

	enum class Dir
	{
		N,
		W,
		S,
		E,
	};

	enum class TickResult
	{
		Idle,
		Running,
		ObstacleEncountered,
	};

	class Grid
	{
	private:
		std::vector<bool> data;

	public:
		bool IsFree(Pos position);
	};

	class Rover
	{
	private:
		Pos m_position;
		Dir m_direction;
		Grid m_grid;

		std::deque<char> m_queuedCommands;

	public:
		Rover(const Grid& grid, Pos position, Dir direction);

		inline Pos Position() const { return m_position; }
		inline Dir Direction() const { return m_direction; }

		void QueueCommands(const char* commands);

		TickResult Tick();
	};
}
