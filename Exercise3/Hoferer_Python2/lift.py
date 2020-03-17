import time

from main import append_new_line


def set_status(text):
    time.sleep(1)
    append_new_line("status.txt", text)
    print(text)


def close_the_doors():
    set_status("...-> closing doors <-...")


def open_the_doors():
    set_status("...<- opening doors ->...")


def ding():
    set_status("DING!")


class Lift:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        set_status("Hello, I am Lifty, I am starting at floor " + str(self.current_floor))

    def __del__(self):
        set_status("End of test, thanks for driving with Lifty!")

    def order(self, order):
        set_status("Getting your request for a lift: " + order[0] + " " + order[1].name)
        close_the_doors()
        self.move_to_floor(0, order[0])

    def move_to_floor(self, tracker, target_floor):
        if target_floor > self.current_floor:
            self.current_floor = self.current_floor + 1
            set_status("Moving up, passing floor " + str(self.current_floor))
            tracker = tracker + 1
            return self.move_to_floor(tracker, target_floor)
        elif target_floor < self.current_floor:
            self.current_floor = self.current_floor - 1
            set_status("Moving down, Passing floor " + str(self.current_floor))
            tracker = tracker + 1
            return self.move_to_floor(tracker, target_floor)
        else:
            if tracker == 0:
                set_status("Already here at floor " + str(target_floor) + "! Leaving doors open ...")
            else:
                set_status("Arrived at floor" + str(target_floor))
                ding()
                open_the_doors()
            return

    def choose_target_floor(self, floor):
        set_status("Getting your request for target floor: " + str(floor))
        close_the_doors()
        self.move_to_floor(0, floor)
