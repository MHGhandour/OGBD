#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 05:32:34 2019

@author: mhg
"""

from Functions import np,initialize,Progressive,LAPS,time,Decompose,keepLv,Neighbouring
for sim in [18300,18400,18500,18900,20000]:
    #MainPts=np.load('/media/mhg/DATA/NPY/MainPts'+str(sim)+'.npy')
    #Gi_splash=np.load('/media/mhg/DATA/NPY/Gi_splash'+str(sim)+'.npy')
    MainPts=np.load('/media/mhg/DATA2/NPY/MainPts'+str(sim)+'.npy')
    Gi_splash=np.load('/media/mhg/DATA2/NPY/Gi_splash'+str(sim)+'.npy')
    if(Gi_splash.shape!=MainPts[:,0].shape):
        print('sim',str(sim),'skipped, and need to be reconstructed')
    else:
        drops=MainPts[~Gi_splash,:]
        del MainPts,Gi_splash
        drops=drops[(drops[:,0]>-4)*(drops[:,0]<4)*(drops[:,1]>-4)*(drops[:,1]<4)*(drops[:,2]<10),:]
        if(drops.shape[0]!=0):   
            t0=time.time()
            minlv=min(drops[:,3]).astype(int);maxlv=max(drops[:,3]).astype(int)
            LvPts=[]
            Pts_L1=[]
            Li_1=[]
            Gi_Lv=[]
            XInterval=[]
            YApply=[]
            ZApply=[]
            ID_IRef=[]
            for level in range(minlv,maxlv+1):
                i=level-minlv;
                Gi_Lv.append(keepLv(drops,level-1,level,level+1))
                LvPts.append(drops[Gi_Lv[i],:])
                Li_1.append(keepLv(LvPts[i],level))
                Pts_L1.append(LvPts[i][Li_1[i],:])
                if(Pts_L1[i].shape[0]==0):
                    XInterval.append([])
                    YApply.append([])
                    ZApply.append([])
                    ID_IRef.append([])
                else:
                    A=(Decompose(LvPts[i],Pts_L1[i]))
                    XInterval.append(A[0])
                    YApply.append(A[1])
                    ZApply.append(A[2])
                    ID_IRef.append(A[3])
            del A
            droplets=[]
            dropspassed=np.zeros_like(drops[:,0],dtype=bool)
            #%%
            while(np.sum(~dropspassed)):
                level=min(drops[~dropspassed,3]).astype(int)
                Gi_drops=np.zeros_like(dropspassed);Gi_drops3=np.zeros_like(Gi_drops)
                Gi_drops[np.where(drops[:,3]==level*~dropspassed)[0][0]]=True
                #%%
                while(1):
                    for i in range(level-minlv,maxlv-minlv+1):
                            index_in=Gi_drops[Gi_Lv[i]]
                            index_passed=np.zeros_like(index_in)
                            in1=index_in[Li_1[i]]
                            while(np.sum(in1)>0):
                                Li_drops=Neighbouring(XInterval[i],YApply[i],ZApply[i],ID_IRef[i][in1,:])
                                index_passed=index_passed+index_in
                                Gi_drops[Gi_Lv[i]]=Gi_drops[Gi_Lv[i]]+Li_drops;
                                index_in=Gi_drops[Gi_Lv[i]]*~(index_passed)
                                in1=index_in[Li_1[i]]
                    Gi_drops2=np.zeros_like(Gi_drops);Gi_drops2[:]=Gi_drops[:]
                    if(~np.sum(Gi_drops2^Gi_drops3,dtype=bool)):
                        break
                    for i in range(level-minlv,maxlv-minlv+1):
                            index_in=Gi_drops[Gi_Lv[i]]
                            index_passed=np.zeros_like(index_in)
                            in1=index_in[Li_1[i]]
                            while(np.sum(in1)>0):
                                Li_drops=Neighbouring(XInterval[i],YApply[i],ZApply[i],ID_IRef[i][in1,:])
                                index_passed=index_passed+index_in
                                Gi_drops[Gi_Lv[i]]=Gi_drops[Gi_Lv[i]]+Li_drops;
                                index_in=Gi_drops[Gi_Lv[i]]*~(index_passed)
                                in1=index_in[Li_1[i]]
                    Gi_drops3=np.zeros_like(Gi_drops);Gi_drops3[:]=Gi_drops[:]
                    if(~np.sum(Gi_drops2^Gi_drops3,dtype=bool)):
                        break
            
                droplets.append(drops[Gi_drops,:])
                dropspassed=dropspassed+Gi_drops
            
            #%%
            
            print('droplets',sim,'counted in',time.time()-t0,'s')
            np.save('NPY/droplets-'+str(sim)+'.npy',droplets)
