import time

from main import append_new_line
from liftstatus import *


def give_status(text):
    time.sleep(1)
    append_new_line("status.txt", "Lifty: " + text)
    print(text)


class Lift:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        self.status = LiftStatus.OPEN_DOORS
        give_status("Hello, I am Lifty, I am starting at floor: " + str(self.current_floor))

    def __del__(self):
        self.status = LiftStatus.OPEN_DOORS
        give_status("End of test, thanks for driving with Lifty!")

    def close_the_doors(self):
        self.status = LiftStatus.CLOSING_DOORS
        give_status("Closing my doors...")
        self.status = LiftStatus.CLOSED_DOORS
        give_status("Doors are closed now")

    def open_the_doors(self):
        self.status = LiftStatus.OPENING_DOORS
        give_status("Opening my doors...")
        self.status = LiftStatus.OPEN_DOORS
        give_status("Doors are opened now")

    def ding(self, target_floor):
        self.status = LiftStatus.ARRIVING_WITH_DING
        give_status("DING! Arrived at floor: " + str(target_floor))
        self.open_the_doors()

    def move_to_floor(self, tracker, target_floor):
        if target_floor > self.current_floor:
            self.current_floor = self.current_floor + 1
            self.status = LiftStatus.MOVING_UP
            give_status("Moving up, passing by floor: " + str(self.current_floor))
            tracker = tracker + 1
            return self.move_to_floor(tracker, target_floor)
        elif target_floor < self.current_floor:
            self.current_floor = self.current_floor - 1
            self.status = LiftStatus.MOVING_DOWN
            give_status("Moving down, passing by floor: " + str(self.current_floor))
            tracker = tracker + 1
            return self.move_to_floor(tracker, target_floor)
        else:
            if tracker == 0:
                give_status("Already here at floor " + str(target_floor) + "! Leaving my doors open ...")
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
        give_status("Bringing you to the requested floor...")
        self.close_the_doors()
        self.move_to_floor(0, floor)
