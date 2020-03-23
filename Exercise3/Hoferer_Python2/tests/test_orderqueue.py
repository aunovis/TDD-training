import pytest

from direction import Direction
from orderqueue import OrderQueue


@pytest.mark.parametrize(
    'init_order, added_order', [
        ((5, Direction.UP), (-2, Direction.DOWN)),
        ((2, Direction.DOWN), (-100, Direction.UP)),
        ((2, Direction.UP), (0, Direction.DOWN)),
        ((1, Direction.DOWN), (20, Direction.DOWN))
    ]
)
def test_order_queue_basics(init_order, added_order):
    x = OrderQueue(init_order)
    assert x.get_queue() == [init_order]
    x.add_order_to_queue(added_order)
    assert x.get_queue() == [init_order, added_order]
    x.remove_order_from_queue(added_order)
    assert x.get_queue() == [init_order]
