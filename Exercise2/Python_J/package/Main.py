class Roversimulator:
    size = 0
    position = (0,0)
    orientation = 'N'


    def __init__(self, a):
        self.size = a

    def initRobot(self, a, b):
        self.position = a
        self.orientation = b

    def drive(self, a):
        return a

    def getRoverPosition(self, ):
        return "test"

    def getRoverOrientation(self, ):
        return "test"

    def addObstacle(self, a):
        return a


def main():
    return True


if __name__ == '__main__':  # pragma: no cover
    main()
