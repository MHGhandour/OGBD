# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:36:42 2018

@author: mhg
"""
import numpy as np
dropletsize=np.load('dropletsize.npy')
A=dropletsize[:,[2]]/(dropletsize[:,[0]]**2+dropletsize[:,[1]]**1)**0.5
#droplets=np.append(droplets,A,axis=1)
A=np.arctan(A)*180/3.14;
B=np.append(dropletsize[:,[3]],A,axis=1)
#np.save('plot.npy',B)
plotxy(B)