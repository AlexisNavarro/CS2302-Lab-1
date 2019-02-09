# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:30:49 2019

@author: Alexis
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    rad= rad*.2#change the size of the radius to make it smaller
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = (center[0]+rad*np.sin(t))+rad #add the radius to move the center to the left
    y = center[1]+rad*np.cos(t)# do not change the y since you only move left and right
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w)
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 50, [100,0], 100,.9)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')