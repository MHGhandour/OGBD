# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:44:45 2018

@author: mhg
"""
from __future__ import division
import numpy as np 
from plot import plt,plt3d,plt3d2,plt3D,pltxy,pltxz,histo
import pickle as pl
k=0
rimposition=np.array([[],[]])
for nbr in range(100,2400,100):
    k=k+1
    MainPts=np.load('NPY/MainPts'+str(nbr)+'.npy')
    Gi_splash=np.load('NPY/Gi_splash'+str(nbr)+'.npy')
    couronne=MainPts[Gi_splash,:]
    del MainPts, Gi_splash
    i=max(couronne[:,2])
    b=len(np.where(couronne[:,2]==i)[0])
    a=np.array([[i,b]])
    while(i>0):
        i=i-2**(-9)    
        b=len(np.where(couronne[:,2]==i)[0])
        if(b>0):
            a=np.append(a,[[i,b+a[-1,1]]],axis=0)
    limrim=a[-1,1]*9/100
    rimy=a[np.where(abs(a[:,1]-limrim)==min(abs(a[:,1]-limrim))),0][0][0]
    rimposition=np.append(rimposition,np.array([[nbr], [rimy]]),axis=1)
#    fig_handle=plt.figure(nbr) 
#    plt.plot(couronne[0:-1:10,0],couronne[0:-1:10,2],'.',markersize=0.1)
#    plt.plot([rimy,rimy,rimy])    
#   pl.dump(fig_handle,file('rim','w'))

rimposition=np.transpose(rimposition)
np.save('rimy.npy',rimposition)