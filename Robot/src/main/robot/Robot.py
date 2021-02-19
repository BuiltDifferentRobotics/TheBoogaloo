import threading

from src.main.robot.subsystems.Conveyer import Conveyer
from src.main.robot.subsystems.Drivetrain import Drivetrain
from src.main.robot.subsystems.SerialController import SerialController
from src.main.robot.subsystems.Shooter import Shooter


class Robot:

    def __init__(self):
        pass

    def robotPeriodic(self):
        shooter = Shooter(1, "shooter thread")
        serialController = SerialController(2, "serialController thread")
        conveyer = Conveyer(3, "conveyer thread")
        driveTrain = Drivetrain(4, "driveTrain thread")

        shooter.start()
        serialController.start()
        conveyer.start()
        driveTrain.start()

        shooter.join()
        serialController.join()
        conveyer.join()
        driveTrain.join()

        print("DONE")


if __name__ == '__main__':
    robot = Robot()
    robot.robotPeriodic()

