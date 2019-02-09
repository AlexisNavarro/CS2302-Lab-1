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


def multiCircles(ax,n,xCenter,yCenter,radius):# don't need w here since it really doesn't affect what we need
    if n>0:
       center = [xCenter, yCenter]
       x,y = circle(center, radius)
       ax.plot(x,y,color='k')
       
       leftCirc=xCenter+(radius*(2/3))#equations to affect the positions on the new circles just how it was done before
       rightCirc=xCenter-(radius*(2/3))
       topCirc=yCenter+(radius*(2/3))
       bottomCirc=yCenter-(radius*(2/3))
       radius=radius/3
       
       multiCircles(ax,n-1,xCenter,yCenter,radius) # referenced to create more circles like how it was done in squares.py
       multiCircles(ax,n-1, leftCirc,yCenter,radius) 
       multiCircles(ax,n-1, rightCirc,yCenter,radius) 
       multiCircles(ax,n-1,xCenter ,topCirc,radius) 
       multiCircles(ax,n-1, xCenter,bottomCirc,radius) 
       
xCenter=0#initialize new variables
yCenter=0
plt.close("all") 
fig, ax = plt.subplots() 
multiCircles(ax, 3,xCenter,yCenter,1000)# get rid of the original center since we will have various centers for left and right axis
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('multiCircles.png')