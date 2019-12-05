# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:08:59 2018

@author: mhg
"""

from Functions import np,initialize,Progressive,LAPS,time
sim=4200
MainPts=np.load('/media/mhg/DATA/NPY/MainPts'+str(sim)+'.npy')
Gi_splash=np.load('/media/mhg/DATA/NPY/Gi_splash'+str(sim)+'.npy')
#MainPts=np.load('NPY/MainPts'+str(sim)+'.npy')
#Gi_splash=np.load('NPY/Gi_splash'+str(sim)+'.npy')
drops=MainPts[~Gi_splash,:]
del MainPts,Gi_splash
droplets=[]
t0=time.time()
while(drops.shape[0]>0):
    Gi_goutte=np.zeros_like(drops[:,0],dtype=bool);Gi_goutte[0]=True
    Gi_goutte=Progressive(drops,Gi_goutte)
    Gi_goutte2=np.zeros_like(Gi_goutte);Gi_goutte2[:]=Gi_goutte[:]
    Gi_goutte=LAPS(drops,Gi_goutte,Gi_goutte2)
    droplets.append(drops[Gi_goutte,:])
    drops=drops[~Gi_goutte,:]
print('droplets',sim,'counted in',time.time()-t0,'s')
np.save('droplets-'+str(sim)+'.npy',droplets)
