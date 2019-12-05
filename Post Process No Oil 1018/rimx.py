#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:24:05 2019

@author: mhg
"""

from __future__ import division
import numpy as np 
from plot import plot3d,histo,plotxy
import matplotlib.pyplot as plt
fig_handle=plt.figure()  
rimy=np.load('rimy.npy')
rimxy=np.append(rimy,np.zeros([rimy.shape[0],1]),axis=1)
for i in range(0,rimy.shape[0]):
    nbr=np.int(rimy[i,0])
    couronne=np.load('MainPts-'+str(nbr)+'.npy')
    circle1=np.where(couronne[:,2]==rimy[i,1])
    circle1=couronne[circle1[0],:]
    r=(circle1[:,0]**2+circle1[:,1]**2)**0.5
    r=np.sum(r)/r.shape[0]
    plt.subplot(3,3,i+1)     
    plotxy(circle1)
    circle2=plt.Circle((0, 0), r,color='r', fill=False)
    ax = plt.gca()
    ax.add_artist(circle2)
    plt.show()
    rimxy[i,2]=r
    
    #plt.plot([rimy,rimy,rimy])    
#    plt.subplot(1,5,k+5)  
