import unittest
from package.Main import *


class TestMain(unittest.TestCase):

    def test_init_lift(self):
        for expected_position in range(0, 11):
            # When
            sut = Lift(expected_position)
            # Then
            self.assertEqual(expected_position, sut.floor)

    def test_response_to_call(self):
        direction = DIRECTION_UP
        for source_floor in range(0, 11):
            lift_floor = 5
            sut = Lift(lift_floor)
            # when
            current_floor, lift_direction = sut.call_lift(source_floor, direction)
            # then
            self.assertEqual(lift_floor, current_floor)
            if current_floor < source_floor:
                self.assertEqual(DIRECTION_UP, lift_direction)
            elif current_floor == source_floor:
                self.assertEqual(DIRECTION_NONE, lift_direction)
            else:
                self.assertEqual(DIRECTION_DOWN, lift_direction)
            self.assertEqual(lift_floor, current_floor)


if __name__ == '__main__':
    unittest.main()
