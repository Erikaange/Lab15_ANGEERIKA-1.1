import numpy as np

class DataSet:# Constructor to initialize the parameters
    """A class to represent a quadratic dataset and its plotting.
    The quadratic function is of the form:
        y = ax² + bx + c
 """
    def __init__(self, a=1, b=0, c=0,x_min = -100, x_max = 100, num_points= 100):
        """Initializes the DataSet object with given coefficients and x-range settings.

        Args:
            a : Coefficient of x². Defaults to 1.
            b : Coefficient of x. Defaults to 0.
            c : Constant term. Defaults to 0.
            x_min : Minimum value for x. Defaults to -100.
            x_max : Maximum value for x. Defaults to 100.
            num_points : Number of x points to generate. Defaults to 100"""
        self.a = a
        self.b = b
        self.c = c
        self.x_min = x_min
        self.x_max = x_max
        self.num_points = num_points

        # Generate evenly spaced x-values
        self.x = np.linspace(self.x_min, self.x_max, self.num_points) 

    def quad_formula(self):
        """
                Computes the y-values for the quadratic formula using the initialized x-values.
        
                Returns:
                    tuple: A tuple containing the x-values and the corresponding y-values.
                """
        # Calculate y using the quadratic formula
        y = self.a * self.x**2 +  self.b * self.x + self.c
        return self.x, y  
