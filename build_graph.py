import numpy as np

class DataSet:# Constructor to initialize the parameters
    """A class to represent a quadratic dataset and its plotting.
 """
    def __init__(self, a=1, b=0, c=0,x_min = -100, x_max = 100, num_points= 100):
        self.a = a
        self.b = b
        self.c = c
        self.x_min = x_min
        self.x_max = x_max
        self.num_points = num_points
        self.x = np.linspace(self.x_min, self.x_max, self.num_points) 

    def quad_formula(self):
        y = self.a * self.x**2 +  self.b * self.x + self.c
        return self.x, y  
