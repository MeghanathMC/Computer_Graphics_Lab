import matplotlib.pyplot as plt
import numpy as np

def bresenham_line(x0,y0,x1,y1):
    dx,dy=x1-x0,y1-y0
    p=2*dy-dx
       
    points=[(x0,y0)]
        
    while x0<x1:
        x0+=1
        if p<0:
            p+=2*dy
        else:
            y0+=1
            p+=2*dy-2*dx
            points.append((x0,y0))
    
    x_points,y_points=zip(*points)
    plt.plot(x_points,y_points,"o-")
    
    plt.title("Bresenham Line Algorithm")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.grid(True)
    plt.show()


bresenham_line(20,10,30,18)