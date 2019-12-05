# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:03:03 2017

@author: mhg
"""


    #                       Au nom de DIEU
    #       Python Code For Post-Process Gerris3D Output File
    #	When needed two function can be added from PLOT.py file:
    #		plt3d & CheckRange
        
    ##Initiation: FUNCTIONS + Load
from Functions import np,Phases,Alpha,Organize,LetLev,RSHP
##%%
###from PLOT import plt3d;#,CheckRange;##Pts =np.loadtxt('text-1000',delimiter=' ');
#Pts=np.load('data.npy');
#Pts=Pts[:,[0,2,1,30,16,17,18,19,20,21,22,23,24]];
##%%Organize
#[MainPts,Pts]=Organize(Pts,0);
#np.save('MainPts.npy',MainPts);
#np.save('Pts.npy',Pts);
#%%LOAD
MainPts=np.load('MainPts.npy');
Pts=np.load('Pts.npy');
#%%Phases
[Ids,XInterval,Ref_Pts,s1,s2y,s2z]=Phases(Pts) #s1 and s2 are the shape Y_Apply and Z_Apply
#%%Alpha
index1=np.zeros((Ref_Pts.shape[0],1),dtype=bool);index1[0][0]=True;
index_main=Alpha(XInterval,Ref_Pts,index1,s1,s2y,s2z);
index_final=np.zeros((MainPts.shape[0],1),dtype=bool)
#%%
for level in range(0,3):    
    np.save('/media/mhg/64BCAE6C40E79E46/Correct/new',index_final);
    print('Processing Level .. ',level);
    index=LetLev(MainPts,np.array([level,level+1]));
    Pts=MainPts[index,:];
    index1=RSHP(LetLev(Pts,np.array([level])));
    index2=RSHP(LetLev(Pts,np.array([level+1])));
    index1[index1[:,0]]=index_main;    
    [Ids,XInterval,Ref_Pts,s1,s2y,s2z]=Phases(Pts)
    index_main=Alpha(XInterval,Ref_Pts,index1,s1,s2y,s2z);
    print(np.where(index_main[:,0]==0))
    index_final[index,:]=index_main;
    index_main=index_main[index2[:,0],:];
##%%    #np.save('index_final.npy',index_final)
#plt3d(MainPts[index_final[:,0],:]);
#    return None;
