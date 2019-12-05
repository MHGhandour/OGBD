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
    OriginalPts=np.load(os.path.expanduser('/media/mhg/DATA/NoOil8/data/data-'+str(sim)+'.npy'));
    MainPts=np.load(os.path.expanduser('/media/mhg/DATA2/NPY/MainPts'+str(sim)+'.npy'));
    Gi_splash=np.load(os.path.expanduser('/media/mhg/DATA2/NPY/Gi_splash'+str(sim)+'.npy'));
    MainPts=MainPts[Gi_splash,0:5]
    VoidPts=remove_water(OriginalPts)
    np.save('/media/mhg/DATA2/NPY/VoidPts'+str(sim)+'.npy',VoidPts)
    VoidPts=VoidPts[:,0:5]
    del OriginalPts,Gi_splash
    #%%
    A=MainPts[0:-1,:]-MainPts[1:MainPts.shape[0],:]
    A=A.astype(bool)
    A=A[:,0]
    A=np.where(A)[0]
    A=np.append(0,A,A.shape[0])
    B=np.zeros(A.shape[0]-1)
    for i in range(A.shape[0]-1):
        B[i]=(max(MainPts[A[i]:A[i+1],2]))
    Xi=MainPts[A,0]
    A2=MainPts[0:-1,:]-MainPts[1:MainPts.shape[0],:]
    A2=A2.astype(bool)
    A2=A2[:,0]
    A2=np.where(A2)[0]
    A2=np.append(0,A2,A2.shape[0])
    Xi2=MainPts[A2,0]
    Bulles=np.zeros((0,5))
    if(~np.sum(~(Xi==Xi2)).astype(bool)):
        for i in range(A2.shape[0]-1):
            Voids=VoidPts[A2[i]:A2[i+1],:]
            C=(Voids[:,2]<B[i])
            Bulles=np.append(Bulles,Voids[C],axis=0)
            
            