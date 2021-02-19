from src.lib.robot_manager.Subsystem import Subsystem

class Shooter(Subsystem):

    def __init__(self):
        pass

    def periodic(self):
        print("Shooter running")


    def is_finished(self):
        return False
