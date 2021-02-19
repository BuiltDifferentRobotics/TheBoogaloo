import threading

from src.main.robot.subsystems import SerialController


class Shooter(threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        pass

    def run(self):
        while True:
            print(SerialController.stupid)
            if SerialController.stupid % 5 == 0:
                print("stupid number")
                print(SerialController.stupid)
