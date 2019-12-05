from __future__ import division
import matplotlib.pyplot as plt

def CenterSize(droplet):
    drp=np.zeros((droplet.shape[0],4))
    drp[:,0:4]=droplet[:,0:4];drp[:,3]=drp[:,3]*(((2**(-droplet[:,4]))*6400)**3);
    a=np.array([sum(drp[:,0]*drp[:,3]),sum(drp[:,1]*drp[:,3]),sum(drp[:,2]*\
    drp[:,3]),sum(drp[:,3])])
    a[0:3]=a[0:3]/a[3];a[3]=a[3]*3/(4*np.pi);a[3]=2*(a[3]**(1./3));4
    return(a);
    
    
import numpy as np
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
    histo(dropletsize[:,3],sim)
    plt.yticks(np.arange(0,400,100))
    plt.xticks(np.arange(0,1000,100))
    #plt.savefig('histo'+str(sim)+'.png')
    #plt.close()
    
#figure()
#%%Alpha distribution
plt.figure()
for sim in range (5350,5400,50):
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
    A=dropletsize[:,[2]]/(dropletsize[:,[0]]**2+dropletsize[:,[1]]**1)**0.5
    #droplets=np.append(droplets,A,axis=1)
    A=np.arctan(A)*180/3.14;
    B=np.append(dropletsize[:,[3]],A,axis=1)
    #np.save('plot.npy',B)
    plotxy(B)