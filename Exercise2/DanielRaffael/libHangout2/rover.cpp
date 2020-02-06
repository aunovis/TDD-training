#include "rover.h"
#include <vector>
#include <array>

namespace Hangout2
{
	bool Grid::IsFree(Pos position)
	{
		return !m_data[position.y * GetSize() + position.x];
	}

	Grid::Grid() : m_data(64) { }
	Grid::Grid(std::vector<bool> data) : m_data(data){ }

	int Grid::GetSize() const
	{
		return static_cast<int>(std::sqrt(m_data.size()));
	}

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
			const auto gridSize = m_grid.GetSize();

			Pos new_pos;

			if (cmd == 'f')
			{
				new_pos.x = (xdiff + m_position.x) % gridSize;
				new_pos.y = (ydiff + m_position.y) % gridSize;
			}
			else if (cmd == 'b')
			{
				new_pos.x = (m_position.x - xdiff) % gridSize;
				new_pos.y = (m_position.y - ydiff) % gridSize;
			}

			if (new_pos.x < 0)
				new_pos.x += gridSize;
			if (new_pos.y < 0)
				new_pos.y += gridSize;

			if (m_grid.IsFree(new_pos))
				m_position = new_pos;
			else
			{
				m_queuedCommands.clear();
				return TickResult::ObstacleEncountered;
			}
		}
		else if (cmd == 'l' || cmd == 'r')
		{
			const int offset = cmd == 'l' ? 1 : -1;
			int new_direction = static_cast<int>(m_direction) + offset;
			if (new_direction < 0)
				new_direction += 4;
			new_direction %= 4;
			m_direction = static_cast<Dir>(new_direction);
		}

		return TickResult::Running;
	}
}
