from src.lib.robot_manager.Subsystem import Subsystem

class Hopper_Conveyer_Shooter(Subsystem):

    def __init__(self):
        pass

    def shoot(self, distance):
        pass

    def set_current_potion(self, potion_type):
        pass

    def periodic(self):
        print("Hopper_Conveyer_Shooter running")

    def is_finished(self):
        return False