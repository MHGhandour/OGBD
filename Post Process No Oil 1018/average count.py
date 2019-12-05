# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:14:46 2018

@author: mhg
"""

import numpy as np
dropletsize=np.load('dropletsize.npy')
A=np.zeros((40,2))
for i in range(25,1000,25):
    A[i/25,0:2]=[i,np.sum((dropletsize[:,[3]]<i) & (dropletsize[:,[3]]>=i-25))]
np.save('plot.npy',A)