#pragma once
#include <tuple>


enum Direction : int
{
	North, 
	East,
	South,
	West
};

class Rover
{
public:
	Rover(int x, int y, int d) : 
		m_X(x), m_Y(y), m_D(d) {

	}

	~Rover() {

	}

	void MoveForward()
	{
		switch (m_D)
		{
		case Direction::North:									
			++m_Y;
			break;

		case Direction::East:
			++m_X;
			break;

		case Direction::South:
			--m_Y;
			break;

		case Direction::West:
			--m_X;
			break;
		}
	}
	
	void MoveBackward() 
	{
		switch (m_D)
		{
		case Direction::North:
			--m_Y;
			break;

		case Direction::East:
			--m_X;
			break;

		case Direction::South:
			++m_Y;
			break;

		case Direction::West:
			++m_X;
			break;
		}
	}

	void TurnLeft()
	{
		switch (m_D)
		{
		case Direction::North:
			m_D = Direction::West;
			break;

		case Direction::East:
			m_D = Direction::North;
			break;

		case Direction::South:
			m_D = Direction::East;
			break;

		case Direction::West:
			m_D = Direction::South;
			break;
		}
	}

	void TurnRight()
	{
		switch (m_D)
		{
		case Direction::North:
			m_D = Direction::East;
			break;

		case Direction::East:
			m_D = Direction::South;
			break;

		case Direction::South:
			m_D = Direction::West;
			break;

		case Direction::West:
			m_D = Direction::North;
			break;
		}
	}

	std::tuple<int, int, int> getStatus() {
		return std::make_tuple(m_X, m_Y, m_D);
	}

private:
	int m_X;
	int m_Y;
	int m_D;

};