# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:34:37 2018

@author: mhg
"""
import numpy as np
MainPts=np.load('MainPts-5350.npy')
np.where(MainPts[:,3]==0)

#%i have deleted all the emplty cells, should i reput them may be inside the count function?