# -*- coding: utf-8 -*-

"""
Created on Wed Nov 14 21:44:45 2018

@author: mhg
"""
from __future__ import division
import numpy as np 
from plot import plot3d,histo,plotxy
import pickle as pl
k=0
fig_handle=plt.figure()  
for nbr in range(2350,9350,1000):
    k=k+1
    couronne=np.load('MainPts-'+str(nbr)+'.npy')
    couronne[0:3,:]=couronne[0:3,:]*2**(-9)
    couronne[0:3,:]=np.round(couronne[0:3,:])
    couronne[0:3,:]=couronne[0:3,:]*2**(9)
    i=max(couronne[:,2])
    b=len(np.where(couronne[:,2]==i)[0])
    a=np.array([[i,b]])
    while(i>0):
        i=i-2**(-9)    
        b=len(np.where(couronne[:,2]==i)[0])
        if(b>0):
            a=np.append(a,[[i,b+a[-1,1]]],axis=0)
    #b=a[[0],:] 
    #for i in range(1,a.shape[0]):
    #        b=np.append(b,a[[i],:]+b[[-1],:],axis=0) 
    limrim=a[-1,1]*12/100
    rimy=a[np.where(abs(a[:,1]-limrim)==min(abs(a[:,1]-limrim))),0][0][0]

    import matplotlib.pyplot as plt  
    plt.subplot(3,3,k)     
    #plt.plot(a[:,0],a[:,1],'.')
    plt.plot(couronne[0:-1:10,0],couronne[0:-1:10,2],'.',markersize=0.1)
    plt.plot([rimy,rimy,rimy])    
#    plt.subplot(1,5,k+5)  
     
    #plt.ylim(bottom=rimy/2)  
pl.dump(fig_handle,file('rim','w'))