import matplotlib.pyplot as plt
from build_graph import DataSet



form_graph = DataSet(a=1, b=-3, c=4)
x,y = form_graph.quad_formula()
plt.style.use('bmh')
# Create a new figure and axis for the plot
figure, graph = plt.subplots()

graph.plot(x,y)


graph.grid(True)
plt.show()
