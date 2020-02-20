import operator

class Roversimulator:
    size = 0
    position = (0, 0)
    orientation = (0, 0)
    obstacles= []
    compass = {
        'N': (0, -1),
        'W': (1, 0),
        'S': (0, 1),
        'O': (-1, 0)
    }
    revCompass = {
        (0, -1): 'N',
        (1, 0): 'W',
        (0, 1): 'S',
        (-1, 0): 'O'
    }
    turntable = [[(0, -1), (1, 0)],
                 [(1, 0), (0, 1)],
                 [(0, 1), (-1, 0)],
                 [(-1, 0), (0, -1)]]

    def __init__(self, a):
        self.size = a

    def initRobot(self, a, b):
        self.position = a
        self.setOrientation(b)

    def getOrientation(self):
        return self.revCompass[self.orientation]

    def setOrientation(self, a):
        self.orientation = self.compass[a]

    def drive(self, a):
        try:
            for command in a:
                self._handleCommand(command)
            return "success"
        except ValueError as e:
            return e.args[0] 

    def addObstacle(self, a):
        self.obstacles.append(a)

    def _handleCommand(self, command):
        if command == 'f':
            self._setNewPosition(operator.add)
        elif command == 'b':
            self._setNewPosition(operator.sub)
        elif command == 'l':
            self._turnRobot(0)
        elif command == 'r':
            self._turnRobot(1)

    def _setNewPosition(self, op):
        newPosition = (self._sphere(op(self.position[0], self.orientation[0])), self._sphere(op(self.position[1], self.orientation[1])))
        if(self.checkCollision(newPosition)):
            raise ValueError(f"Obstacle at {newPosition[0]},{newPosition[1]}")
        else:
            self.position = newPosition

    def _turnRobot(self, direction):
        for entry in self.turntable:
            if entry[direction] == self.orientation:
                self.orientation = entry[1 - direction]
                break

    def _sphere(self, coordinate):
        if coordinate > self.size:
            return 0
        elif coordinate < 0:
            return self.size
        else:
            return coordinate
    
    def checkCollision(self, position):
        for obstacle in self.obstacles:
            if(obstacle == position):
                return True
        return False


def main():
    return True


if __name__ == '__main__':  # pragma: no cover
    main()
