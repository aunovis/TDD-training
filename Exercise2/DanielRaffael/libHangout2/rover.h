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
		N = 0,
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
		std::vector<bool> m_data;

	public:
		Grid(std::vector<bool> height);
		Grid();

		bool IsFree(Pos position);
		int GetSize() const;
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
