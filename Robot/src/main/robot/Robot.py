from src.lib.robot_manager.RobotManager import SubsystemManager
from src.main.robot.subsystems.Drivetrain import Drivetrain
from src.main.robot.subsystems.Shooter import Shooter

class Robot:

    driveTrain = None
    shooter = None
    serialController = None

    subsystemManager = None

    test_counter = None

    def __init__(self):
        self.driveTrain = Drivetrain()
        self.shooter = Shooter()

        self.subsystemManager = SubsystemManager()

        self.test_counter = 0

        self.subsystemManager.add(self.shooter)
        self.subsystemManager.add(self.driveTrain)

    def robotPeriodic(self):
        self.subsystemManager.run()


if __name__ == '__main__':
    robot = Robot()
    robot.robotPeriodic()