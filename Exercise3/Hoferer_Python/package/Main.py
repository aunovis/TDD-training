
DIRECTION_NONE = 0
DIRECTION_UP = 1
DIRECTION_DOWN = -1

class Lift:

    def __init__(self, position):
        self.position = position

    @property
    def floor(self):
        return self.position

