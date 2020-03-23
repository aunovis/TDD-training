from main import give_status
from liftstatus import *


class Lift:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        self.status = None
        self.set_status(LiftStatus.START)
        self.set_status(LiftStatus.OPEN_DOORS)

    def __del__(self):
        self.set_status(LiftStatus.FINISH)

    def close_the_doors(self):
        self.set_status(LiftStatus.CLOSING_DOORS)
        self.set_status(LiftStatus.CLOSED_DOORS)

    def open_the_doors(self):
        self.set_status(LiftStatus.OPENING_DOORS)
        self.set_status(LiftStatus.OPEN_DOORS)

    def ding(self, target_floor):
        self.set_status(LiftStatus.ARRIVING_WITH_DING, target_floor)
        self.open_the_doors()

    def move_to_floor(self, tracker, target_floor):
        if target_floor > self.current_floor:
            self.current_floor = self.current_floor + 1
            self.set_status(LiftStatus.MOVING_UP)
            tracker = tracker + 1
            return self.move_to_floor(tracker, target_floor)
        elif target_floor < self.current_floor:
            self.current_floor = self.current_floor - 1
            self.set_status(LiftStatus.MOVING_DOWN)
            tracker = tracker + 1
            return self.move_to_floor(tracker, target_floor)
        else:
            self.ding(target_floor)
            return

    def order(self, order):
        give_status("You wait at floor " + str(order[0]) + " and pressed the " + order[1].name + " button")
        give_status("Coming to your floor...")
        self.close_the_doors()
        self.move_to_floor(0, order[0])

    def choose_target_floor(self, floor):
        give_status("You pressed the button to get to floor " + str(floor))
        if self.current_floor == floor:
            give_status("Already here at floor " + str(floor) + "! Leaving my doors open ...")
        else:
            give_status("Bringing you to the requested floor...")
            self.close_the_doors()
            self.move_to_floor(0, floor)

    def set_status(self, lift_status, target_floor=None):
        self.status = lift_status
        give_status(self.lift_output(lift_status, target_floor))

    def lift_output(self, i, target_floor=None):
        switcher = {
            LiftStatus.MOVING_UP: "Moving up, passing by floor: " + str(self.current_floor),
            LiftStatus.MOVING_DOWN: "Moving down, passing by floor: " + str(self.current_floor),
            LiftStatus.ARRIVING_WITH_DING: "DING! Arrived at floor: " + str(target_floor),
            LiftStatus.OPENING_DOORS: "Opening my doors...",
            LiftStatus.OPEN_DOORS: "Doors are opened now",
            LiftStatus.CLOSING_DOORS: "Closing my doors...",
            LiftStatus.CLOSED_DOORS: "Doors are closed now",
            LiftStatus.START: "Hello, I am Lifty, I am starting at floor: " + str(self.current_floor),
            LiftStatus.FINISH: "End of tests, thanks for driving with Lifty!"
        }
        return switcher.get(i, "Invalid status")
