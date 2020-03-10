class Lift:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        print("\n")
        print("Hello, I am Lifty, I am starting at floor", self.current_floor)

    def order(self, order):
        print("Getting your request for a lift:", order[0], order[1].name)
        self.move_to_floor(order[0])

    def move_to_floor(self, floor):
        if floor == self.current_floor:
            print("I am already at the requested floor ... opening doors")
        else:
            print("Moving to requested floor")
            print("Finally arrived at floor", floor, "... opening doors")
            self.current_floor = floor

    def choose_target_floor(self, floor):
        print("Getting your request for target floor:", floor)
        self.move_to_floor(floor)
