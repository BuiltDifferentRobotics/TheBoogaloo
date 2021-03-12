from src.lib.robot_manager.Subsystem import Subsystem


class Drivetrain(Subsystem):

    drivetrain_motors = [0, 0]  # left_speed, right_speed

    def __init__(self):
        pass

    def tank_drive(self, left_speed, right_speed):
        self.drivetrain_motors[0] = left_speed
        self.drivetrain_motors[1] = right_speed

    def periodic(self):
        self.tank_drive(left_speed=1, right_speed=1)
        print("Drivetrain running")

    def is_finished(self):
        return False