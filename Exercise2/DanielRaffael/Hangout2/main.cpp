#include <cstdlib>
#include <iostream>
#include <random>
#include <algorithm>

#include "rover.h"

using namespace Hangout2;

Grid GenerateStartingGrid(Pos startPoint)
{
	std::default_random_engine generator{};
	std::uniform_real_distribution<double> distribution{ 1.0, 10.0 };
	do
	{
		std::vector<bool> terrain(9 * 9);
		std::generate_n(std::begin(terrain), terrain.size(), [&] { return distribution(generator) > 8; });

		Grid grid{ terrain };

		if (grid.IsFree(startPoint))
			return terrain;
	} while (true);
}

void PrintRoverState(const Rover& rover, const Grid& grid)
{
	for (int y = grid.Size() - 1; y >= 0; y--)
	{
		for (int x = 0; x < grid.Size(); x++)
		{
			if (rover.Position().x == x && rover.Position().y == y)
			{
				switch (rover.Direction())
				{
				case Dir::N:
					std::cout << "^";
					break;
				case Dir::W:
					std::cout << "<";
					break;
				case Dir::S:
					std::cout << "v";
					break;
				case Dir::E:
					std::cout << ">";
					break;
				}
			}
			else if (grid.IsFree({ x, y }))
				std::cout << ".";
			else
				std::cout << "@";

			std::cout << " ";
		}
		std::cout << std::endl;
	}
}

int main(int argc, char** argv)
{
	const Pos startPoint{ 4, 4 };
	const auto grid = GenerateStartingGrid(startPoint);
	Rover rover{ grid, startPoint, Dir::N };

	std::cout << "Type to move:" << std::endl;
	std::cout << "  f - move forward" << std::endl;
	std::cout << "  b - move backward" << std::endl;
	std::cout << "  l - turn left" << std::endl;
	std::cout << "  r - turn right" << std::endl;
	std::cout << "or type quit to quit." << std::endl;

	while (true)
	{
		PrintRoverState(rover, grid);

		std::cout << "> ";
		std::string input;
		std::cin >> input;

		if (input == "quit")
			break;

		rover.QueueCommands(input.c_str());
		while (true)
		{
			auto result = rover.Tick();
			if (result == TickResult::Idle)
				break;
			if (result == TickResult::ObstacleEncountered)
			{
				std::cout << "Obstacle encountered!!! Halting movement." << std::endl;
				break;
			}
		}
	}

	return EXIT_SUCCESS;
}
