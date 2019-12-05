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
print('\n CODE START >>>')
from Functions import np,initialize,Progressive,LAPS,time,findlevel,remove_air
#%% Main code
for sim in [18400,18500,18900,20000]:
    t0=time.time()
    #%%
    #Variables are level,T1,T0,T3,U,V,W,P,K1,DV
    #OriginalPts=np.load(os.path.expanduser('/media/mhg/DATA2/datanpynooil/data-'+str(sim)+'.npy'));
    OriginalPts=np.load(os.path.expanduser('/media/mhg/DATA/datanoOil8/data-'+str(sim)+'.npy'));
    OriginalPts[:,0:3]=np.around(OriginalPts[:,0:3]*2**10)
    OriginalPts[:,0:3]=OriginalPts[:,0:3]*2**-10
    OriginalPts[:,3]=findlevel(OriginalPts)
    MainPts=remove_air(OriginalPts);
    np.save('/media/mhg/DATA2/NPY/MainPts'+str(sim)+'.npy',MainPts)
    MainPts=MainPts[:,0:4]
    del OriginalPts
    Gi_splash=initialize(MainPts)
    Gi_splash=Progressive(MainPts,Gi_splash)
    Gi_splash2=np.zeros_like(Gi_splash);Gi_splash2[:]=Gi_splash[:]
    Gi_splash=LAPS(MainPts,Gi_splash,Gi_splash2)
    #pltxz(MainPts[Gi_splash,:])
    np.save('/media/mhg/DATA2/NPY/Gi_splash'+str(sim)+'.npy',Gi_splash)
    te=time.time()
    print('Simulation step:',sim,'Processed in',(te-t0)//60,'minutes')
