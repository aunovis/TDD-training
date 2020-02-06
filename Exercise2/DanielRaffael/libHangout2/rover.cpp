#include "rover.h"

#include <array>

namespace Hangout2
{
	bool Grid::IsFree(Pos position) const
	{
		return !m_data[position.y * Size() + position.x];
	}

	Grid::Grid()
		: m_size{ DEFAULT_SIZE }
		, m_data(DEFAULT_SIZE* DEFAULT_SIZE)
	{ }

	Grid::Grid(std::vector<bool> data)
		: m_size{ static_cast<size_t>(std::sqrt(data.size())) }
		, m_data{ data }
	{ }


	Rover::Rover(const Grid& grid, Pos position, Dir direction)
		: m_grid{ grid }
		, m_position{ position }
		, m_direction{ direction }
	{
	}

	void Rover::QueueCommands(const char* commands)
	{
		const auto count = strlen(commands);
		m_queuedCommands.insert(std::end(m_queuedCommands), commands, commands + count);
	}

	TickResult Rover::Tick()
	{
		// Indexed by Dir                               N   W   S  E
		static constexpr std::array<int, 4> XMovements{ 0, -1,  0, 1 };
		static constexpr std::array<int, 4> YMovements{ 1,  0, -1, 0 };

		if (m_queuedCommands.empty())
			return TickResult::Idle;

		const char cmd = m_queuedCommands.front();
		m_queuedCommands.pop_front();

		if (cmd == 'f' || cmd == 'b')
		{
			const auto index = size_t(m_direction);
			const auto xdiff = XMovements[index];
			const auto ydiff = YMovements[index];
			const auto gridSize = int(m_grid.Size());

			Pos newPos;
			if (cmd == 'f')
			{
				newPos.x = (m_position.x + xdiff) % gridSize;
				newPos.y = (m_position.y + ydiff) % gridSize;
			}
			else if (cmd == 'b')
			{
				newPos.x = (m_position.x - xdiff) % gridSize;
				newPos.y = (m_position.y - ydiff) % gridSize;
			}

			if (newPos.x < 0)
				newPos.x += gridSize;
			if (newPos.y < 0)
				newPos.y += gridSize;

			if (m_grid.IsFree(newPos))
				m_position = newPos;
			else
			{
				m_queuedCommands.clear();
				return TickResult::ObstacleEncountered;
			}
		}
		else if (cmd == 'l' || cmd == 'r')
		{
			const int offset = cmd == 'l' ? 1 : -1;

			int new_direction = (static_cast<int>(m_direction) + offset) % 4;
			if (new_direction < 0)
				new_direction += 4;
			m_direction = static_cast<Dir>(new_direction);
		}

		return TickResult::Running;
	}
}
