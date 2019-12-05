#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:02:24 2019

@author: mhg
"""
from __future__ import division
from Functions import SortRows,reshape,np,findlevel
#from plot import plt,plt3d,plt3d2,plt3D,pltxy,pltxz
 #%%
def npy2vtk_V_P(Original,filename):
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
    #g3=~g2;#g3 is the indices of repeated points
    g5=np.where(g2)[0]
    g5=np.append(g5,g2.shape[0])
    g6=g5[1:g5.shape[0]]-g5[0:-1]
    points=Allpoints[g2,0:-1]
    for i in range(2,9):
        g7=np.where(g6==i)[0]
        for j in range(1,i):
            g8=g5[g7]
            points[g7]=(points[g7]+Allpoints[g8+j,0:-1])
            cells2[Allpoints[g8+j,-1].astype(int)]=cells2[Allpoints[g8,-1].astype(int)]
        points[g7]=points[g7]/i
#    for i in range(0,8):
#        g4=np.append(g3[1:g3.shape[0]],False)# g4 is the indices of previous cell of g3
#        cells2[Allpoints[g3,-1].astype(int)]=cells2[Allpoints[g4,-1].astype(int)]
#                                    #by the reference of Allpoints last column, 
#                                    #each cell get the value of the previous cell
#        g3=g3[0:-1]*g3[1:g3.shape[0]]# g3 is now for the repeated point 
#                                    #twice or more (i=0)
#        g3=np.append(False, g3)
#    #
#    points=Allpoints[g2,0:-1];#points are all the vertexes not repeated
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
    #Variable: T0
    f=open(filename, 'a')
    f.write('\n SCALARS T0 float \n LOOKUP_TABLE default \n')
    f.close()
    f=open(filename, 'ab')
    np.savetxt(f, points[:,[5]],  fmt='%1.6f', delimiter=' ', newline='\n')
    f.close()    
    #Variable: T3
    #f=open(filename, 'a')
    #f.write('\n SCALARS T3 float \n LOOKUP_TABLE default \n')
    #f.close()
    #f=open(filename, 'ab')
    #np.savetxt(f, points[:,[6]],  fmt='%1.6f', delimiter=' ', newline='\n')
    #f.close()
    #Variable: P
    f=open(filename, 'a')
    f.write('\nSCALARS P float \n LOOKUP_TABLE default \n')
    f.close()
    f=open(filename, 'ab')
    np.savetxt(f, points[:,[6]],  fmt='%1.6f', delimiter=' ', newline='\n')
    f.close()
    #Variable: K1
    #f=open(filename, 'a')
    #f.write('\nSCALARS K1 float \n LOOKUP_TABLE default \n')
    #f.close()
    #f=open(filename, 'ab')
    #np.savetxt(f, points[:,[11]],  fmt='%1.6f', delimiter=' ', newline='\n')
    #f.close()    
    #Variable: DV
    #f=open(filename, 'a')
    #f.write('\nSCALARS DV float \n LOOKUP_TABLE default \n')
    #f.close()
    #f=open(filename, 'ab')
    #np.savetxt(f, points[:,[12]],  fmt='%1.6f', delimiter=' ', newline='\n')
    #f.close()
    
    
    #Velocity vector V
    #Variable: U
    f=open(filename, 'a')
    f.write('\nVECTORS velocity float \n')
    f.close()
    f=open(filename, 'ab')
    np.savetxt(f, points[:,[7,8,9]],  fmt='%1.6f', delimiter=' ', newline='\n')
    f.close()
##%%
#for i in range(200,30200,2000):
#    MainPts=np.load('NPY/MainPts'+str(i)+'.npy')
#    Gi_splash=np.load('NPY/Gi_splash'+str(i)+'.npy')
#    npy2vtk_V_P(MainPts[Gi_splash,:],'vtk/couronne-P-'+str(i)+'.vtk')
#    del MainPts,Gi_splash
#%%
#for sim in range(16200,18200,2000):
#    OriginalPts=np.load('/media/mhg/DATA/datanoOil8/data-'+str(sim)+'.npy');
#    OriginalPts[:,0:3]=np.around(OriginalPts[:,0:3]*2**10)
#    OriginalPts[:,0:3]=OriginalPts[:,0:3]*2**-10
#    OriginalPts[:,3]=findlevel(OriginalPts)
#    OriginalPts=SortRows(OriginalPts,0,1,2)
#    A=OriginalPts[:,4]==0
#    Gi_splash=np.load('/media/mhg/DATA/NPY/Gi_splash'+str(sim)+'.npy')
#    A[~A]=Gi_splash
#    Original=OriginalPts[A,:][:,[0,1,2,3,4]]
#    del OriginalPts,Gi_splash,A
#    npy2vtk(Original,'vtk/couronne-P-'+str(sim)+'.vtk')
#%%
for sim in range(4800,30200,100):
    print('outputing simulation:',sim)
    MainPts=np.load('/media/mhg/DATA2/NPY2/MainPts'+str(sim)+'.npy')
    Gi_splash=np.load('/media/mhg/DATA2/NPY2/Gi_splash'+str(sim)+'.npy')
    Original=MainPts[Gi_splash,:]
    Original=Original[:,[0,1,2,3,4,5,10,7,8,9]]
    del MainPts,Gi_splash
    npy2vtk_V_P(Original,'/media/mhg/Seagate Backup Plus Drive/VTK2/couronne-P-'+str(sim)+'.vtk')
#    
    #first_function=(MainPts[:,0]**2+MainPts[:,1]**2)<3**2
    #second_function=np.abs(MainPts[:,0]/2)-MainPts[:,1]<0.25
    #third_function=MainPts[:,2]>-2
    #section=np.logical_and(first_function,second_function,third_function)
    #SPts1=MainPts[section*Gi_splash[:,0],:]
    #SPts2=MainPts[section*(Gi_droplets[:,0]),:]
    #Pts3=MainPts[Gi_splash[:,0],:]
    #npy2vtk(Pts3,'vtk/couronne-new-'+str(sim)+'.vtk')
    #npy2vtk(SPts1,'vtk/couronne-new-'+str(sim)+'.vtk')
    #npy2vtk(SPts2,'vtk/gouttes-new-'+str(sim)+'.vtk')    
    