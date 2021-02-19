import threading


class Drivetrain(threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        pass

    def run(self):
        while(True):
            print("Drivetrain running")

    def drive_train_periodic(self):
        pass

    def tank_drive(self):
        pass