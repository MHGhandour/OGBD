# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:29:23 2018

@author: mhg
"""
from __future__ import division
import numpy as np
def CenterSize(droplet):
    drp=np.zeros((droplet.shape[0],4))
    drp[:,0:4]=droplet[:,0:4];drp[:,3]=drp[:,3]*(((2**(-droplet[:,4]))*6400)**3);
    a=np.array([sum(drp[:,0]*drp[:,3]),sum(drp[:,1]*drp[:,3]),sum(drp[:,2]*\
    drp[:,3]),sum(drp[:,3])])
    a[0:3]=a[0:3]/a[3];a[3]=a[3]*3/(4*np.pi);a[3]=2*(a[3]**(1./3));4
    return(a);
    
def Cellvolume(droplet):
    drp=np.zeros((droplet.shape[0],5))
    drp[:,0:4]=droplet[:,0:4];drp[:,3]=(((2**(-droplet[:,4]))*6400)**3);
    a=np.array([sum(drp[:,0]*drp[:,3]),sum(drp[:,1]*drp[:,3]),sum(drp[:,2]*\
    drp[:,3]),sum(drp[:,3])])
    a[0:3]=a[0:3]/a[3];a[3]=a[3]*3/(4*np.pi);a[3]=2*(a[3]**(1./3));4
    return(a);

from plot import plot3d,histo,plotxy
for sim in range (5350,5400,50):
    #plt.figure()    
    gouttelettes=np.load('gouttelettes-'+str(sim)+'.npy').tolist();
    j=0;
    del gouttelettes[0]
    for i in range(0,len(gouttelettes)):
         if (gouttelettes[i-j].shape[0]<3):
             del gouttelettes[i-j]
             j=j+1
    
    dropletsize=np.zeros((len(gouttelettes)-1,4))
    for i in range(1,len(gouttelettes)):
        dropletsize[i-1,:]=CenterSize(gouttelettes[i]);
    
    #np.save('dropletsize.npy',dropletsize)
#    histo(dropletsize[:,3],sim)
#    plt.yticks(np.arange(0,400,100))
#    plt.xticks(np.arange(0,1000,100))
    #plt.savefig('histo'+str(sim)+'.png')
    #plt.close()

for sim in range (5350,5400,50):
    #plt.figure()    
    gouttelettes=np.load('gouttelettes-'+str(sim)+'.npy').tolist();
    j=0;
    del gouttelettes[0]
    for i in range(0,len(gouttelettes)):
         if (gouttelettes[i-j].shape[0]<3):
             del gouttelettes[i-j]
             j=j+1
    
    dropletvolume=np.zeros((len(gouttelettes)-1,4))
    for i in range(1,len(gouttelettes)):
        dropletvolume[i-1,:]=Cellvolume(gouttelettes[i]);

dropletproportion=dropletsize/dropletvolume
A=np.where(dropletproportion[:,3]>0.5)[0]
d_eau=[]
for i in range(0,len(A)):
    d_eau.append(gouttelettes[A[i]])

for i in range(0,len(A)):
    npy2vtk(d_eau[i],'d_eau-'+str(i)+'.vtk')

