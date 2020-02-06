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
		size_t m_size;
		std::vector<bool> m_data;

	public:
		static constexpr size_t DEFAULT_SIZE = 8;

		Grid();
		Grid(std::vector<bool> height);

		inline size_t Size() const { return m_size; }

		bool IsFree(Pos position) const;
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
