import unittest
from package import Main


class TestMain(unittest.TestCase):
    def testIf(self):
        Main.initMap(5)
        Main.initRobot((0,0),'S')
        command1 = ["f","b","f","l","f","f","f","f","r","f","f","f","f","b","r","b","l","l","f","f","r","f","f"]
        self.assertEqual(Main.drive(command1), "success")
        self.assertEqual(Main.getRoverPosition(), (2,2))
        self.assertEqual(Main.getRoverOrientation(), "N")
        Main.addObstacle((2,1))
        self.assertEqual(Main.drive("f"), "Obstacle at 2,1")


if __name__ == '__main__':
    unittest.main()
