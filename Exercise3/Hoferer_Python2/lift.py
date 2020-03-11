def close_the_doors():
    print("...-> closing doors <-...")


def open_the_doors():
    print("...<- opening doors ->...")


def ding():
    print("DING!")


class Lift:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        print("\n")
        print("Hello, I am Lifty, I am starting at floor", self.current_floor)

    def order(self, order):
        print("Getting your request for a lift:", order[0], order[1].name)
        close_the_doors()
        self.move_to_floor(0, order[0])

    def move_to_floor(self, tracker, target_floor):
        if target_floor > self.current_floor:
            self.current_floor = self.current_floor + 1
            print("Moving up, passing floor", self.current_floor)
            tracker = tracker + 1
            return self.move_to_floor(tracker, target_floor)
        elif target_floor < self.current_floor:
            self.current_floor = self.current_floor - 1
            print("Moving down, Passing floor", self.current_floor)
            tracker = tracker + 1
            return self.move_to_floor(tracker, target_floor)
        else:
            if tracker == 0:
                print("Already here! Leaving doors open ...", target_floor)
            else:
                print("Arrived at floor", target_floor)
                ding()
                open_the_doors()
            return

    def choose_target_floor(self, floor):
        print("Getting your request for target floor:", floor)
        close_the_doors
        self.move_to_floor(0, floor)
