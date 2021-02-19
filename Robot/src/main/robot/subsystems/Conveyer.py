import threading


class Conveyer(threading.Thread):

    def __init__(self, threadID, name, thingy):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.thingy = thingy
        pass

    def run(self):
        while(True):
            self.thingy.iterate()
            print("Conveyer Running")