#perform 2d transforamtion on basic objects

import numpy as np
import matplotlib.pyplot as plt

def translate(coords,tx,ty):
    translation_matrix=np.array([[1,0,tx],[1,0,ty],[0,0,1]])
    return np.dot(translation_matrix,coords)
    
    
    
    
def rotate(coords,theta):
    rad=np.radians(theta)
    rotation_matrix=np.array([[np.cos(rad),-np.sin(rad),0],[np.sin(rad),np.cos(rad),0],[0,0,1]])
    return np.dot(rotation_matrix,coords)

def scale(coords,sx,sy):
    scaling_matrix=np.array([[sx,0,0],[0,sy,0],[0,0,1]])
    return np.dot(scaling_matrix,coords)
    
    
def plot_polygon(coords,color="blue",label="ori"):
    xs=coords[0,:]
    ys=coords[1,:]
    xs=np.append(xs,xs[0])
    ys=np.append(ys,ys[0])
    plt.plot(xs,ys,marker='o',color=color,label=label)  


triangle=np.array([[0,1,0.5,0],[0,0,1,0],[1,1,1,1]])

triangle_translated=translate(triangle,1,1)
triangle_rotated=rotate(triangle,90)
triangle_scaled=scale(triangle,1,2)

plt.figure(figsize=(10,8))

plot_polygon(triangle,color="red",label="original triangle")
plot_polygon(triangle_translated,color="green",label="translated triangle")
plot_polygon(triangle_rotated,color="blue",label="rotated triangle")
plot_polygon(triangle_scaled,color="purple",label="scaled triangle")


plt.axis('equal')
plt.legend()
plt.grid(True)
plt.title("2d transformations")
plt.show()