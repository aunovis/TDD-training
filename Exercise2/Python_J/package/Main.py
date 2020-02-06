class Roversimulator:
    size = 0
    position = (0,0)
    orientation = (0,0)
    compass = {
        'N': (0, -1),
        'W': (1, 0),
        'S': (0, 1),
        'O': (0, 1)
    }
    revCompass = {
        (0, -1): 'N',
        (1, 0): 'W',
        (0, 1): 'S',
        (0, 1): 'O'
    }
    


    def __init__(self, a):
        self.size = a

    def initRobot(self, a, b):
        self.position = a
        self.setOrientation(b)

    def getOrientation(self):
        return self.revCompass[self.orientation]

    def setOrientation(self,a):
        self.orientation = self.compass[a]

    def drive(self, a):
        return a

    def addObstacle(self, a):
        return a

    def __handleCommand(self, command):
        pass


def main():
    return True


if __name__ == '__main__':  # pragma: no cover
    main()
