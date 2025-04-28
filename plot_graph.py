# lab15_angeerika-1.
# Ange erika kengne heukoua
# This program draws the graph of a quadration equation
# 04/26/25




import matplotlib.pyplot as plt
from build_graph import DataSet


# Initialize the DataSet object with specific coefficients for the quadratic formula
form_graph = DataSet(a=1, b=-3, c=4)
# Generate x and y values using the quad_formula method
x,y = form_graph.quad_formula()
plt.style.use('classic')# Set the style for the plot

# Create a new figure and axis for the plot
figure, graph = plt.subplots()

graph.plot(x,y)# Plot the quadratic function (x versus y)
graph.set_title(f'Quadratic formula graph')# Set the title for the graph

# label the axis
graph.set_xlabel('x')
graph.set_ylabel('y')



graph.grid(True)# Add a grid
plt.show()# Display the plot
