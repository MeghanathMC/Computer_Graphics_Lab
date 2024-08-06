#develop a program to demonstrate basic geometric operations on 3d object

import numpy as np
import matplotlib.pyplot as plt

# cube=np.array([
    # [0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,0],
    # [0,0,1],[1,0,1],[1,1,1],[0,1,1],[0,0,1],
    # [1,0,1],[1,0,0],[1,1,0],[1,1,1],[1,0,1]
    # ])

cube=np.array([
    [0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,0],
    [0,0,1],[1,0,1],[1,1,1],[0,1,1],[0,0,1],
    [1,0,1],[1,0,0],[1,1,0],[0,1,1],[1,0,1]
])

scaled_cube=cube*[0.5,0.5,0.5]


fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

ax.plot(cube[:,0],cube[:,1],cube[:,2],'r-',label="original")

ax.plot(scaled_cube[:,0],scaled_cube[:,1],scaled_cube[:,2],'g-',label="scaled")


ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("z-axis")

ax.legend()
plt.show()   