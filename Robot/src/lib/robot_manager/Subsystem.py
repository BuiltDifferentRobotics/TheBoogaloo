from typing import final
from abc import abstractmethod

class Subsystem():

    def __init__(self):
        pass

    """
    Runs periodically until isFinished is true
    """

    @abstractmethod
    def periodic(self):
        pass

    """
    
    Returns true when the command should end
    
    """

    @abstractmethod
    def is_finished(self):
        return False

    """
    
    Runs once when ending
    
    """

    @abstractmethod
    def end(self):
        pass

    """
    Handles execution logic of a command for CommandScheduler
    """
    @final
    def execute(self):
        while not self.is_finished():
            self.periodic()

        self.end()
