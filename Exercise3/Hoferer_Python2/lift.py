import time

from gui import Gui


def close_the_doors():
    print("...-> closing doors <-...")
    time.sleep(0.2)


def open_the_doors():
    print("...<- opening doors ->...")
    time.sleep(0.2)


def ding():
    print("DING!")
    time.sleep(0.2)


class Lift:
    def __init__(self, gui, current_floor=0):
        self.current_floor = current_floor
        self.gui = gui
        self.gui.change_to("test")
        print("\n")
        print("Hello, I am Lifty, I am starting at floor", self.current_floor)

    def __del__(self):
        self.gui.close_gui()

    def order(self, order):
        print("Getting your request for a lift:", order[0], order[1].name)
        close_the_doors()
        self.move_to_floor(0, order[0])

    def move_to_floor(self, tracker, target_floor):
        time.sleep(0.5)
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
        close_the_doors()
        self.move_to_floor(0, floor)
