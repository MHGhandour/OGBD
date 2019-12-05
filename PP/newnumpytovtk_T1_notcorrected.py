#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 08:56:38 2019

@author: mhg
"""
from __future__ import division
from Functions import SortRows,reshape,np,findlevel
from plot import plt,plt3d,plt3d2,plt3D,pltxy,pltxz
#%%
def npy2vtk(Original,filename):
    #
    def X(pts2,a):
        pts=np.zeros_like(pts2)
        pts[:]=pts2[:]
        pts[:,0:3]=pts[:,0:3]+a*2**(-(pts[:,[3]]+1))*np.array([1,0,0])
        return(pts)
    def Y(pts2,a):
        pts=np.zeros_like(pts2)
        pts[:]=pts2[:]
        pts[:,0:3]=pts[:,0:3]+a*2**(-(pts[:,[3]]+1))*np.array([0,1,0])
        return(pts)
    def Z(pts2,a):
        pts=np.zeros_like(pts2)
        pts[:]=pts2[:]
        pts[:,0:3]=pts[:,0:3]+a*2**(-(pts[:,[3]]+1))*np.array([0,0,1])
        return(pts)
    def repeated(Pts):
        Pts=SortRows(Pts,0,1,2)
        a=(Pts[0:-1,0:3]==Pts[1:Pts.shape[0],0:3])
        return(np.append(True,(~(a[:,0]*a[:,1]*a[:,2]))))
    Allpoints=np.append(X(Y(Z(Original,-1),-1),-1),X(Y(Z(Original,1),-1),-1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,-1),1),-1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,1),1),-1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,-1),-1),1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,1),-1),1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,-1),1),1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,1),1),1),axis=0)
    s=Original.shape[0];
    Allpoints=np.append(Allpoints,np.transpose([np.array(range(0,s*8))]),axis=1)    
    Allpoints=SortRows(Allpoints,0,1,2)# The last column of SortRows is now 
                                       # the sorted indices     
    #                                       
    g2=repeated(Allpoints) #g2 represents the points present only once in Allpoints
    g=Allpoints[g2,-1].astype(int) # g is the indices of the points repeated once,
                #this indices need to be replaced by indices from 1 to g.shape
    cells2=(np.zeros((8*s,),dtype=int))# cells to need to be refer for all points
                #but with indices from 1 to g.shape
    cells2[:]=-1
    cells2[g]=np.array(range(0,g.shape[0])) # the g indices in cells2 are 
                                        #replaced with indices from 1 to g.shape
    g3=~g2;#g3 is the indices of repeated points
    for i in range(0,8):
        g4=np.append(g3[1:g3.shape[0]],False)# g4 is the indices of previous cell of g3
        cells2[Allpoints[g3,-1].astype(int)]=cells2[Allpoints[g4,-1].astype(int)]
                                    #by the reference of Allpoints last column, 
                                    #each cell get the value of the previous cell
        g3=g3[0:-1]*g3[1:g3.shape[0]]# g3 is now for the repeated point 
                                    #twice or more (i=0)
        g3=np.append(False, g3)
    #
    points=Allpoints[g2,0:-1];#points are all the vertexes not repeated
    #
    cells1=np.zeros((s,0),dtype=int)# cells one is 8 columnes with indices from
    #1 to 8*Original.shape. cells on is comfortable to vtk but with repeated indices
    for i in range(0,8):
        cells1=np.append(cells1,reshape(np.array(range(0,s)))+s*i,axis=1)
    #
    cells=cells2[cells1]
    # replace the repeated indice in cells1 by the corresponding once
    cells=np.append(np.ones((cells.shape[0],1),dtype=int)*8,cells,axis=1)
    
    del Allpoints
    #
 
    f=open(filename, 'w')
    f.write('# vtk DataFile Version 2.0\nGerris simulation version 1.3.2 ')
    f.write('(131206-155120) - Generated via Python Post Processing code -')
    f.write('Author: Mohamed Houssein GHANDOUR\nASCII\nDATASET UNSTRUCTURED_GRID')
    f.write('\nPOINTS ' + str(points.shape[0]) + ' float\n')   
    f.close()
    f=open(filename, 'ab')
    np.savetxt(f,points[:,0:3], fmt='%1.6f', delimiter=' ', newline='\n')
    f.close()
    f=open(filename, 'a')
    f.write('\nCELLS ' + str(cells.shape[0]) + ' ' + str(cells.shape[0]*9)+'\n')
    f.close()
    f=open(filename, 'ab')
    np.savetxt(f,cells, fmt='%1d', newline='\n')
    f.close()
    f=open(filename, 'a')
    f.write('\nCELL_TYPES ' + str(cells.shape[0]) + '\n')
    f.close()
    f=open(filename, 'ab')
    np.savetxt(f,np.ones((cells.shape[0],1))*11, fmt='%1d', newline='\n')
    f.close()
    #Variables are level,T1,T0,T3,U,V,W,P,K1,DV
    f=open(filename, 'a')
    f.write('\nPOINT_DATA ' + str(points.shape[0]) + \
            '\n SCALARS T1 float \n LOOKUP_TABLE default \n')
    f.close()
    f=open(filename, 'ab')
    np.savetxt(f, points[:,[4]],  fmt='%1.6f', delimiter=' ', newline='\n')
    f.close()

