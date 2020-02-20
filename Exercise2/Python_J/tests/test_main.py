import unittest
from package import Main


class TestMain(unittest.TestCase): 
    def testRoversimulator(self):
        roversim = Main.Roversimulator(3)
        roversim.initRobot((0, 0), 'S')
        self.assertEqual(roversim.orientation, (0,1))
        command = ["f"]
        self.assertEqual(roversim.drive(command), "success")
        self.assertEqual(roversim.position, (0, 1))
        self.assertEqual(roversim.getOrientation(), "S")
        command = ["b"]
        self.assertEqual(roversim.drive(command), "success")
        self.assertEqual(roversim.position, (0, 0))
        self.assertEqual(roversim.getOrientation(), "S")
        command = ["r"]
        self.assertEqual(roversim.drive(command), "success")
        self.assertEqual(roversim.position, (0, 0))
        self.assertEqual(roversim.getOrientation(), "W")
        command = ["l","l"]
        self.assertEqual(roversim.drive(command), "success")
        self.assertEqual(roversim.position, (0, 0))
        self.assertEqual(roversim.getOrientation(), "O")
        command = ["f","f","f","f"]
        self.assertEqual(roversim.drive(command), "success")
        self.assertEqual(roversim.position, (0, 0))
        self.assertEqual(roversim.getOrientation(), "O")
        command = ["r","b","b","b","b"]
        self.assertEqual(roversim.drive(command), "success")
        self.assertEqual(roversim.position, (0, 0))
        self.assertEqual(roversim.getOrientation(), "S")
        roversim.addObstacle((0, 1))
        self.assertEqual(roversim.drive("f"), "Obstacle at 0,1")


if __name__ == '__main__':
    unittest.main()
