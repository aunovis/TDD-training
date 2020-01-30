import unittest
from package import Main


class TestMain(unittest.TestCase):
    def testRoversimulator(self):
        roversim = Main.Roversimulator(5)
        roversim.initRobot((0, 0), 'S')
        command1 = ["f", "b", "f", "l", "f", "f", "f", "f", "r", "f",
                    "f", "f", "f", "b", "r", "b", "l", "l", "f", "f", "r", "f", "f"]
        self.assertEqual(roversim.drive(command1), "success")
        self.assertEqual(roversim.getRoverPosition(), (2, 2))
        self.assertEqual(roversim.getRoverOrientation(), "N")
        roversim.addObstacle((2, 1))
        self.assertEqual(roversim.drive("f"), "Obstacle at 2,1")


if __name__ == '__main__':
    unittest.main()
