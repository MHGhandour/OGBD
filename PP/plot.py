# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 01:39:34 2018

@author: mhg
"""    
import matplotlib.pyplot as plt
import numpy as np
def plt3d(*a):
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
    for i in range(len(a)):
        ax.scatter(a[i][:,0],a[i][:,1],a[i][:,2])
    return

      
def pltxy(*a):
    plt.show()
    for i in range(len(a)):
        plt.scatter(a[i][:,0],a[i][:,1],marker='.')
    return
    
def pltxz(*a):
    plt.show()
    for i in range(len(a)):
        plt.scatter(a[i][:,0],a[i][:,2],marker='.',linewidths=0.1)
    return
    
def histo(x,sim):
    import matplotlib.pyplot as plt
    n_bins = 75
    plt.hist(x, bins=n_bins,histtype='step', label='iteration'+str(sim))
    plt.legend(loc='upper right')

    