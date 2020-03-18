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
        (5, (2, Direction.UP,), 2),
        (8, (1, Direction.DOWN), 1)
    ]
)
def test_order_lift(start_pos, order, output):
    x = Lift(start_pos)
    x.order(order)
    assert x.current_floor == output


@pytest.mark.parametrize(
    'start_pos, order, source_floor, target_floor', [
        (0, (5, Direction.UP), 5, 10)
    ]
)
def test_fast_order(start_pos, order, source_floor, target_floor):
    x = Lift(start_pos)
    x.order(order)
    assert x.current_floor == source_floor
    x.choose_target_floor(target_floor)
    assert x.current_floor == target_floor


@pytest.mark.parametrize(
    'start_pos, order, source_floor, target_floor', [
        (-5, (5, Direction.UP), 8, 8),
        (10, (2, Direction.DOWN), -1, -1),
        (0, (2, Direction.UP), 4, 4),
        (5, (1, Direction.DOWN), 5, 5),
        (2, (4, Direction.UP), 4, 4),
        (10, (15, Direction.UP), 12, 12)
    ]
)
def test_lift_transport(start_pos, order, source_floor, target_floor):
    x = Lift(start_pos)
    x.order(order)
    assert x.current_floor == source_floor
    x.choose_target_floor(target_floor)
    assert x.current_floor == target_floor
