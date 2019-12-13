 # -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:03:03 2017

@author: mhg
"""
#       Python Code For Post-Process Gerris3D Output File
        
    ##Initiation: FUNCTIONS + Load
# REMARKS: make arrays with sizes[x,1] arrays with sizes[x,]
# Make sure LvPts and other don't take all variables (13 columns) but take only 4 columns
from __future__ import division
import os.path
print('\n CODE START .... ')
from Functions import np,initialize,Progressive,LAPS,time,findlevel,remove_air
#%% Main code
for sim in np.loadtxt(open('Steps').readlines(),dtype=int)[:-1]:
#This [:-1] is made so that the file Steps is written with a non relevant value at the end, this is done meanwhile i figure out how to load a file with a one item list in some cases, or a mutiple items list in other, in a common command line.
    print('Processing Simlation ... ', sim)
    t0=time.time()
    #Variables are level,T1,T0,T3,P,U,V,W
    OriginalPts=np.load(os.path.expanduser('data-'+str(sim)+'.npy'));
    OriginalPts[:,0:3]=np.around(OriginalPts[:,0:3]*2**10)
    OriginalPts[:,0:3]=OriginalPts[:,0:3]*2**-10
    OriginalPts[:,3]=findlevel(OriginalPts)
    MainPts=remove_air(OriginalPts);
    np.save('MainPts'+str(sim)+'.npy',MainPts)
    MainPts=MainPts[:,0:4]
    del OriginalPts
    Gi_splash=initialize(MainPts)
    Gi_splash=Progressive(MainPts,Gi_splash,'full')
    Gi_splash2=np.zeros_like(Gi_splash);Gi_splash2[:]=Gi_splash[:]
    Gi_splash=LAPS(MainPts,Gi_splash,Gi_splash2,'full')
    #pltxz(MainPts[Gi_splash,:])
    np.save('Gi_splash'+str(sim)+'.npy',Gi_splash)
    te=time.time()
    print('Simulation step:',sim,'Processed in',(te-t0)//60,'minutes', (te-t0\
          -(te-t0)//60)//1, 'seconds')

