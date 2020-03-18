from enum import Enum


class LiftStatus(Enum):
    OPEN_DOORS = 1
    CLOSED_DOORS = 2
    MOVING_UP = 3
    MOVING_DOWN = 4
    CLOSING_DOORS = 5
    OPENING_DOORS = 6
    ARRIVING_WITH_DING = 7
