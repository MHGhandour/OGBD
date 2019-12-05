# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:34:56 2018

@author: mhg
"""

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from plot import plot3d,histo,plotxy


def CenterSize(droplet):
    drp=np.zeros((droplet.shape[0],4))
    drp[:,0:4]=droplet[:,0:4];drp[:,3]=drp[:,3]*(((2**(-droplet[:,4]))*6400)**3);
    a=np.array([sum(drp[:,0]*drp[:,3]),sum(drp[:,1]*drp[:,3]),sum(drp[:,2]*\
    drp[:,3]),sum(drp[:,3])])
    a[0:3]=a[0:3]/a[3];a[3]=a[3]*3/(4*np.pi);a[3]=2*(a[3]**(1./3));4
    return(a);
    
    
    
    
sim=5350
gouttelettes=np.load('gouttelettes-'+str(sim)+'.npy').tolist();
j=0;
del gouttelettes[0]
for i in range(0,len(gouttelettes)):
     if (gouttelettes[i-j].shape[0]<3):
         del gouttelettes[i-j]
         j=j+1
    
dropletsize=np.zeros((len(gouttelettes)-1,4))
for i in range(0,len(gouttelettes)):
    dropletsize[i-1,:]=CenterSize(gouttelettes[i]);

A=np.where((dropletsize[:,3]>175)*(dropletsize[:,3]<225))[0]
d200=[]
for i in range(0,len(A)):
    d200.append(gouttelettes[A[i]])
del d200[0]
d200prime=gouttelettes[A[0]]
for i in range(0,len(A)):
    d200prime=np.append(d200prime,(gouttelettes[A[i]]),axis=0)
del d200prime[0]
#200=dropletsize[A,:]
for i in range(0,len(A)):
    npy2vtk(d200[i],'d200-'+str(i)+'.vtk')
