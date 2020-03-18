import time

from main import append_new_line
from liftstatus import *


def give_status(text):
    time.sleep(1)
    append_new_line("status.txt", "Lift 1: " + text)
    print(text)


class Lift:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        self.status = LiftStatus.OPEN_DOORS
        give_status("Hello, I am Lifty, I am starting at floor " + str(self.current_floor))

    def __del__(self):
        self.status = LiftStatus.OPEN_DOORS
        give_status("End of test, thanks for driving with Lifty!")

    def close_the_doors(self, order):
        give_status("Getting your request for a lift: " + str(order[0]) + " " + order[1].name)
        self.status = LiftStatus.CLOSING_DOORS
        give_status("...-> closing doors <-...")
        self.status = LiftStatus.CLOSED_DOORS
        give_status("Doors are closed now")

    def open_the_doors(self):
        self.status = LiftStatus.OPENING_DOORS
        give_status("...<- opening doors ->...")
        self.status = LiftStatus.OPEN_DOORS
        give_status("Doors are opened now")

    def ding(self, target_floor):
        self.status = LiftStatus.ARRIVING_WITH_DING
        give_status("DING! Arrived at floor " + str(target_floor))
        self.open_the_doors()

    def order(self, order):
        self.close_the_doors(order)
        self.move_to_floor(0, order[0])

    def move_to_floor(self, tracker, target_floor):
        if target_floor > self.current_floor:
            self.current_floor = self.current_floor + 1
            self.status = LiftStatus.MOVING_UP
            give_status("Moving up, passing floor " + str(self.current_floor))
            tracker = tracker + 1
            return self.move_to_floor(tracker, target_floor)
        elif target_floor < self.current_floor:
            self.current_floor = self.current_floor - 1
            self.status = LiftStatus.MOVING_DOWN
            give_status("Moving down, Passing floor " + str(self.current_floor))
            tracker = tracker + 1
            return self.move_to_floor(tracker, target_floor)
        else:
            if tracker == 0:
                give_status("Already here at floor " + str(target_floor) + "! Leaving doors open ...")
            else:
                self.ding(target_floor)
            return

    def choose_target_floor(self, floor):
        give_status("Getting your request for target floor: " + str(floor))
        self.close_the_doors()
        self.move_to_floor(0, floor)


