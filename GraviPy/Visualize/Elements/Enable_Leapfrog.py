import pygame as pg
from GraviPy.Visualize.xytopygame import xy_to_topygame as xy
from GraviPy.Integrators.leapfrog import leapfrog
class EnableLeapfrog():
    """
    A class that enables the LeapFrog integration method for visualization. 
    This class is used together with the menu to enable the Euler integration through a click

    Args:
        visualize (object): The visualization object.
        environment (object): The environment object.

    Attributes:
        visualize (object): The visualization object.
        environment (object): The environment object.
        active (bool): Indicates if the Euler integration is active.
        name (str): The name of the integration method.
    """
    
    def __init__(self, visualize, environment) -> None:
        self.visualize = visualize
        self.environment = environment
        self.active = False
        self.name = "Leapfrog"
        pass
    
    def show(self):
        if self.active:
            self.environment.set_integrator(leapfrog(self.environment))
        pass