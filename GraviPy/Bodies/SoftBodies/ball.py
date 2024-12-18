from GraviPy.Bodies.particle import Particle
from GraviPy.Bodies.spring_link import Spring_link
import numpy as np
import math

class Ball():
    """
    Represents a ball object in a physics simulation.

    Args:
        position (list[float]): The initial position of the ball in 3D space. Defaults to [0, 0, 0].
        mass (float): The mass of the ball. Defaults to 1.
        velocity (list[float]): The initial velocity of the ball in 3D space. Defaults to [0, 0, 0].
        radius (float): The radius of the ball. Defaults to 100.
        charge (float): The charge of the ball. Defaults to 0.
        drag_coeff (float): The drag coefficient of the ball. Defaults to 0.
        elasticity (float): The elasticity of the ball. Defaults to 0.
        N_particles (int): The number of particles used to construct the ball. Defaults to 20.
        damping (float): The damping coefficient of the ball. Defaults to 0.4.
        name (str): The name of the ball. Defaults to an empty string.
        environment (Environment): The environment in which the ball exists. Defaults to None.

    Attributes:
        environment (Environment): The environment in which the ball exists.
        position (list[float]): The current position of the ball in 3D space.
        radius (float): The radius of the ball.
        mass (float): The mass of the ball.
        elasticity (float): The elasticity of the ball.
        velocity (list[float]): The current velocity of the ball in 3D space.
        force (list[float]): The total force acting on the ball.
        drag (float): The drag coefficient of the ball.
        number_of_particles (int): The number of particles used to construct the ball.
        name (str): The name of the ball.
        charge (float): The charge of the ball.
        damping (float): The damping coefficient of the ball.
    """

    def __init__(self, position=[0,0,0], mass=1, velocity=[0,0,0], radius=100, charge=0, drag_coeff=0, elasticity=0, N_particles=20, damping=0.4, name="", environment=None):
        self.environment = environment
        self.position = position
        self.radius = radius
        self.mass = mass
        self.elasticity = elasticity
        self.velocity = velocity
        self.force = [0, 0, 0]
        self.drag = drag_coeff
        self.number_of_particles = N_particles
        self.name = name
        self.charge = charge
        self.damping = damping
        self.construct_ball()

    # Rest of the code...
class Ball():
    def __init__(self, position=[0,0,0], mass =1, velocity=[0,0,0], radius=100, charge =0,drag_coeff=0,elasticity=0, N_particles=20, damping=0.4, name="",environment=None)->None:
        
        self.environment = environment
        self.position = position
        self.radius = radius
        self.mass = mass
        self.elasticity = elasticity
        self.velocity = velocity
        self.force = [0, 0,0]
        self.drag = drag_coeff
        self.number_of_particles = N_particles
        self.name = name
        self.charge = charge
        self.damping = damping
        self.construct_ball()
        



    def fibonacci_sphere(self):
        points = []
        phi = math.pi * (3. - math.sqrt(5.))  # golden angle in radians

        for i in range(self.number_of_particles):
            y = 1 - (i / float(self.number_of_particles - 1)) * 2  # y goes from 1 to -1
            radius = math.sqrt(1 - y*y) * self.radius  # radius at y

            theta = phi * i  # golden angle increment

            x = math.cos(theta) * radius
            z = math.sin(theta) * radius

            points.append([x, y * self.radius, z])
        
        # translate center of ball to pos
        points = [(x + self.position[0], y + self.position[1], z + self.position[2]) for x, y, z in points]

        return points
    
    def nearest_neighbours(self, particle, n=3):
        #find nearest neighbours
        distances = []
        for i in self.particles:
            distances.append((i, np.linalg.norm(particle.position - i.position)))
        distances = sorted(distances, key=lambda x: x[1])
        return distances[:n]
        
        
    def construct_ball(self):
        self.particles = []
        self.spring_links = []
        
        #add particles
        for i in self.fibonacci_sphere():
            self.particles.append(Particle(position=i, mass=self.mass/self.number_of_particles, velocity=self.velocity, radius=5, charge=self.charge, drag_coeff=self.drag, name=self.name, environment=self.environment))
            
        #add spring links
        #add springs between nearest neighbours without repetition
        for i in self.particles:
            for j in self.nearest_neighbours(i, 4):
                if i != j[0]:
                    self.spring_links.append(Spring_link(i, j[0], k=1, l0=np.linalg.norm(i.position-j[0].position), damping=self.damping))
            
            
        #add particles to environment
        for i in self.particles:
            self.environment.add_particle(i)
            
        #add spring links to environment
        for i in self.spring_links:
            self.environment.add_spring_link(i)