import threading

class Conveyer():
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        pass

    def run(self):
        print("Conveyer Running")