# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 14:11:03 2019

@author: Alexis
"""

import numpy as np
import matplotlib.pyplot as plt

def drawTrees(ax,n,xMove,yMove, x,y):
    if n>0:
        q=np.array([[x , y], [x - xMove, y - yMove]])#split both sides of the tree which saves a lot of time
        q1=np.array([[x , y], [x + xMove, y - yMove]])
        
        ax.plot(q[:,0], q[:,1], color='k')
        ax.plot(q1[:,0], q1[:,1], color='k')
        
        drawTrees(ax, n-1, xMove/2, yMove, x-xMove, y-yMove)#use of two recursive calls to create both sides of the tree
        drawTrees(ax,n-1, xMove/2, yMove, x+xMove, y-yMove)
        
plt.close("all")         
fig, ax = plt.subplots()
drawTrees(ax,5,20,10,0,0)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('Trees.png')

