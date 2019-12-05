# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:08:59 2018

@author: mhg
"""

from Functions import np,Phases,Alpha
Pts=np.load('gouttes.npy')
[Ids,XInterval,Ref_Pts,s1,s2y,s2z]=Phases(Pts)
[s1,s2]=Pts.shape;
ida=np.ones((s1,1),dtype=bool);
idx=np.empty_like(ida);
gouttelettes=[[]];
while(sum(ida)[0]):
    idx[:]=False;
    idx[np.where(ida)[0][0],:]=True;
    idx=Alpha(XInterval,Ref_Pts,idx,s1,s2y,s2z);
    gouttelettes.append(Pts[idx[:,0],:])
    ida[idx]=False    

np.save('gouttelettes',gouttelettes)
