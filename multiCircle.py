# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:23:06 2019

@author: Alexis
"""


import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):# do not change this from the original
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y


def multiCircles(ax,n,xAxis,yAxis,radius):# don't need w here since it really doesn't affect what we need
    if n>0:
       center = [xAxis, yAxis]
       x,y = circle(center, radius)
       ax.plot(x,y,color='k')
       
       leftCirc=xAxis+(radius*(2/3))#equations to affect the positions on the new circles just how it was done before
       rightCirc=xAxis-(radius*(2/3))
       topCirc=yAxis+(radius*(2/3))
       bottomCirc=yAxis-(radius*(2/3))
       radius=radius/3
       
       multiCircles(ax,n-1,xAxis,yAxis,radius) # referenced to create more circles like how it was done in squares.py
       multiCircles(ax,n-1, leftCirc,yAxis,radius) 
       multiCircles(ax,n-1, rightCirc,yAxis,radius) 
       multiCircles(ax,n-1,xAxis,topCirc,radius) 
       multiCircles(ax,n-1, xAxis,bottomCirc,radius) 
       
xAxis=0#initialize new variables
yAxis=0
plt.close("all") 
fig, ax = plt.subplots() 
multiCircles(ax, 3,xAxis,yAxis,1000)# get rid of the original center since we will have various centers for left and right axis
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('multiCircles.png')