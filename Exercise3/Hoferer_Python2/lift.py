class Lift:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        print("\n")
        print("Hello, I am Lifty, I am starting at floor", self.current_floor)

    def order(self, order):
        print("Getting your request for a lift:", order[0], order[1].name)
        self.move_to_floor(order[0])

    def move_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.current_floor = self.current_floor + 1
            print("Moving up, passing floor", self.current_floor)
            return self.move_to_floor(target_floor)
        elif target_floor < self.current_floor:
            self.current_floor = self.current_floor - 1
            print("Moving down, Passing floor", self.current_floor)
            return self.move_to_floor(target_floor)
        else:
            print("Arrived at floor", target_floor, "... opening doors")
            return

    def choose_target_floor(self, floor):
        print("Getting your request for target floor:", floor)
        self.move_to_floor(floor)
