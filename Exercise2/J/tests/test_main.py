import unittest
from package import Main

class TestMain(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1)

    def testFunction(self):
        result = Main.test(1)
        self.assertEqual(result, 1)
		
if __name__ == '__main__':
    unittest.main()