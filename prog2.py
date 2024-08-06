#develop a program to demonstrate basic geometric operations on 2d object
import numpy as np

import matplotlib.pyplot as plt


triangle=np.array([[0,0],[1,0],[0.5,1],[0,0]])

translated_triangle=triangle+[1,2]

plt.plot(*triangle.T,'r-',label="original triangle")
plt.plot(*translated_triangle.T,'g-',label="translated-triangle")

plt.axis("equal")
plt.legend()
plt.show()
