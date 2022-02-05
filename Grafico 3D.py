#importling librarlies
from mpl_toolkits import mplot3d
import numpy as up
import matplotlib.pyplot as plt
import np

#defining surface and axes
x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x ** 2 + y ** 3)
fig = plt.figure()

#systax for 3-D plotting
ax = plt.axes(projection = '3d')

#syntax for plotting
ax.plot_surface(x, y, z, cmap = 'viridis', edgecolor = 'green')
ax.set_title('Surfice plot python.hub')
plt.show()

