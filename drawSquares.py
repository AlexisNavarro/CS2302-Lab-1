# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:54:30 2019

@author: Alexis
"""

import numpy as np 
import matplotlib.pyplot as plt

def new_squares(ax,n,x,y,w): #x = 0 and y = 0
    if n>0:
        left=x-w            #example 0-500=-500 which gives you the new squares
        right=x+w
        top=y+w
        bottom=y-w
        p = np.array([[left,bottom],[left,top],[right,top],[right,bottom],[left,bottom]]) #new p coordinates to create new squares
        ax.plot(p[:,0],p[:,1],color='k')
        new_squares(ax,n-1,left,bottom,w/2)
        new_squares(ax,n-1,left,top,w/2)
        new_squares(ax,n-1,right,top,w/2)
        new_squares(ax,n-1,right,bottom,w/2)
         
def draw_squares(ax,n,p,w): #this method was used to work on different approaches
    if n>0:
       # print(n)
        print(p)
        i1 = [1,2,3,0,1]
        #q=((p-p[i1])//2)*w
        #print(midpoint)
        q = (p*w-p[i1]*(1-w))/2
        print(q)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_squares(ax,n-1,q,w/2)
              

         
         
plt.close("all") 
#orig_size = 1000
#p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
fig, ax = plt.subplots()
midpoint=500
new_squares(ax,4,0,0,midpoint)
#draw_squares(ax,2,p,.0)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')

