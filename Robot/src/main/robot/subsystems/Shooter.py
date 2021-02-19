import threading

from src.main.robot.subsystems import SerialController


class Shooter(threading.Thread):

    def __init__(self, threadID, name, serial):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.serial = serial
        pass

    def run(self):
        while True:
            print(self.serial.counter)
            if self.serial.counter % 5 == 0:
                print("stupid number")
