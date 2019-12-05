# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 01:39:34 2018

@author: mhg
"""
def plot3d(a):
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()
    ax.scatter(a[:,0],a[:,1],a[:,2],marker='.')
    return
    
    
def plotxy(a):
    import numpy as np
    import matplotlib.pyplot as plt
    import numpy as np
    plt.show()
    plt.scatter(a[:,0],a[:,1],marker='.')
    return
    
def histo(x,sim):
    import matplotlib.pyplot as plt
    n_bins = 75
    plt.hist(x, bins=n_bins,histtype='step', label='interation'+str(sim))
    plt.legend(loc='upper right')

    