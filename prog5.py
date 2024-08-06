import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

cube = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]])
faces = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [0, 3, 7, 4], [1, 2, 6, 5]]

def plot_cube(ax, vertices, color='blue', alpha=0.25):
    ax.add_collection3d(Poly3DCollection([vertices[f] for f in faces], facecolors=color, alpha=alpha, linewidths=1, edgecolors='r'))
    ax.set(xlim=[0, 2], ylim=[0, 2], zlim=[0, 2], box_aspect=[1, 1, 1])

def transform(v, t=[0, 0, 0], s=[1, 1, 1], angle=0, axis='z'):
    v = (v + t) * s
    c, s = np.cos(angle), np.sin(angle)
    R = np.array({'x': [[1, 0, 0], [0, c, -s], [0, s, c]], 'y': [[c, 0, s], [0, 1, 0], [-s, 0, c]], 'z': [[c, -s, 0], [s, c, 0], [0, 0, 1]]}[axis])
    return v @ R.T

fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'projection': '3d'})
plot_cube(ax1, cube)
plot_cube(ax2, transform(cube, [1, 1, 1], [0.5, 0.5, 0.5], np.pi/4), 'green')
ax1.set_title('Original Cube')
ax2.set_title('Transformed Cube')
plt.show()
