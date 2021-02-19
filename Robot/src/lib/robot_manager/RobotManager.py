import multiprocessing

class SubsystemManager:

    subsystems = []

    def __init__(self):
        pass

    def add(self, subsystem):
        process = multiprocessing.Process(target=subsystem.execute)
        self.subsystems.append(process)

    def run(self):

        print(self.subsystems)
        for subsystem in self.subsystems:
            subsystem.start()

        for subsystem in self.subsystems:
            subsystem.join()


