#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:51:19 2019

@author: mhg
"""

from __future__ import division
import os.path
print('\n CODE START >>>')
from Functions import np,initialize_cavity,Progressive,LAPS,time,findlevel,remove_water
#%% Main code
for sim in [25000]:
    t0=time.time()
    #%%
    #Variables are level,T1,T0,T3,U,V,W,P,K1,DV
    OriginalPts=np.load(os.path.expanduser('/media/mhg/DATA/datanoOil8/data-'+str(sim)+'.npy'));
    MainPts=np.load(os.path.expanduser('/media/mhg/DATA2/NPY/MainPts'+str(sim)+'.npy'));
    MainPts=MainPts[:,0:4]
    
    
    
    
    
    
    
    np.save('/media/mhg/DATA2/NPY/VoidPts'+str(sim)+'.npy',MainPts)
    MainPts=MainPts[:,0:4]
    del OriginalPts
    Norm=np.linalg.norm(MainPts[:,0:3],axis=1)
    start_index=np.where(Norm==min(Norm))[0][0]
    level=MainPts[start_index,3].astype(int)
    Gi_splash=initialize_cavity(MainPts,level)
    Gi_splash=Progressive(MainPts,Gi_splash)
    Gi_splash2=np.zeros_like(Gi_splash);Gi_splash2[:]=Gi_splash[:]
    Gi_splash=LAPS(MainPts,Gi_splash,Gi_splash2)
    #pltxz(MainPts[Gi_splash,:])
    np.save('/media/mhg/DATA2/NPY/Gi_splash'+str(sim)+'.npy',Gi_splash)
    te=time.time()
    print('Simulation step:',sim,'Processed in',(te-t0)//60,'minutes')