import pytest

from lift import *
from direction import *


@pytest.mark.parametrize(
    'start_pos, output', [
        (1, 1),
        (15, 15)
    ]
)
def test_lift_init_with_floor(start_pos, output):
    y = Lift(start_pos)
    assert y.current_floor == output


def test_lift_init():
    x = Lift()
    assert x.current_floor == 0


@pytest.mark.parametrize(
    'start_pos, order, output', [
        (0, (5, Direction.UP), 5),
        (-1, (2, Direction.DOWN), 2),
        (10, (2, Direction.UP,), 2),
        (100, (1, Direction.DOWN), 1)
    ]
)
def test_order_lift(start_pos, order, output):
    x = Lift(start_pos)
    x.order(order)
    assert x.current_floor == output


@pytest.mark.parametrize(
    'start_pos, order, target_pos, output', [
        (-10, (5, Direction.UP), 8, 8),
        (20, (2, Direction.DOWN), -1, -1),
        (0, (2, Direction.UP), 100, 100),
        (5, (1, Direction.DOWN), 5, 5),
        (2, (4, Direction.UP), 4, 4),
        (100, (100, Direction.UP), 4, 4)
    ]
)
def test_lift_transport(start_pos, order, target_pos, output):
    x = Lift(start_pos)
    x.order(order)
    x.choose_target_floor(target_pos)
    assert x.current_floor == output
