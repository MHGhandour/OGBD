from __future__ import division
import numpy as np
def CenterSize(droplet):
    drp=np.zeros_like(droplet)
    drp[:]=droplet[:];drp[:,4]=drp[:,4]*(((2**(-droplet[:,3]))*6400)**3);
    a=np.array([sum(drp[:,0]*drp[:,4]),sum(drp[:,1]*drp[:,4]),sum(drp[:,2]*\
    drp[:,4]),sum(drp[:,4])])
    a[0:3]=a[0:3]/a[3];a[3]=a[3]*3/(4*np.pi);a[3]=2*(a[3]**(1./3));
    return(a);
    
    

for sim in range (35200,35250,100):
    #plt.figure()
    #MainPts=np.load('/media/mhg/DATA/datanoOil8/MainPts'+str(sim)+'.npy')
    #Gi_splash=np.load('/media/mhg/DATA/datanoOil8/Gi_splash'+str(sim)+'.npy')
    gouttelettes=np.load('NPY/droplets-'+str(sim)+'.npy').tolist();
    j=0
    for i in range(0,len(gouttelettes)):
         if (gouttelettes[i-j].shape[0]<3):
             del gouttelettes[i-j]
             j=j+1
    
    dropletsize=np.zeros((len(gouttelettes),4))
    for i in range(0,len(gouttelettes)):
        dropletsize[i,:]=CenterSize(gouttelettes[i]);
    
    #np.save('dropletsize.npy',dropletsize)
    histo(dropletsize[:,3],sim)
    plt.yticks(np.arange(0,400,25))
    plt.xticks(np.arange(0,2000,200))
    
    plt.savefig('histo/histo'+str(sim).zfill(5)+'.png')
    plt.close()
    A=dropletsize[:,[2]]/(dropletsize[:,[0]]**2+dropletsize[:,[1]]**1)**0.5
    #droplets=np.append(droplets,A,axis=1)
    A=np.arctan(A)*180/3.14;
    B=np.append(dropletsize[:,[3]],A,axis=1)
    pltxy(*[B])
    plt.yticks(np.arange(-105,106,15))
    plt.xticks(np.arange(0,2000,200))
    plt.savefig('Alpha/alpha'+str(sim).zfill(5)+'.png')
    plt.close()
#figure()
