from src.lib.robot_manager.Subsystem import Subsystem

class Intake(Subsystem):

    intake = [0, 0, 0] #angle (orientation), intake speed, conveyer speed

    def __init__(self):
        pass

    def set_angle_intake(self, angle):
        self.intake[0] = angle
        pass

    def set_intake_speed(self, intake_speed):
        self.intake[1] = intake_speed
        pass

    def set_conveyer(self, conveyer_speed):
        self.intake[2] = conveyer_speed
        pass

    def periodic(self):
        print("Intake running")

    def is_finished(self):
        return False