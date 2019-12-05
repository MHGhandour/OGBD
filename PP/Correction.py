from __future__ import division
import os.path
print('\n CODE START >>>')
from Functions import np,initialize,Progressive,LAPS,time,findlevel,remove_air
from plot import plt,plt3d,plt3d2,plt3D,pltxy,pltxz
#%% Main code
for sim in range(2200,8900,100):
    t0=time.time()
    MainPts=np.load('NPY/MainPts'+str(sim)+'.npy')
    Gi_splash=np.load('NPY/Gi_splash'+str(sim)+'.npy')
    MainPts=MainPts[:,0:4]
    Gi_splash2=np.zeros_like(Gi_splash);Gi_splash2[:]=Gi_splash[:]
    Gi_splash=Progressive(MainPts,Gi_splash)
    if(~np.sum(Gi_splash2^Gi_splash,dtype=bool)):
        Gi_splash=LAPS(MainPts,Gi_splash,Gi_splash2)
    #pltxz(MainPts[Gi_splash,:])
    np.save('NPY/Gi_splash'+str(sim)+'.npy',Gi_splash)
    te=time.time()
    print('Simulation step:',sim,'Corrected in',(te-t0)//60,'minutes')
