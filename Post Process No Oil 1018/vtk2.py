def npy2vtk(Original,filename):
    import numpy as np
    #Original=np.load('MainPts-5350.npy')
    #%%
    def X(pts,a):
        pts=pts+a*2**(-(pts[:,[4]]+1))*np.array([1,0,0,0,0])
        return(pts)
    def Y(pts,a):
        pts=pts+a*2**(-(pts[:,[4]]+1))*np.array([0,1,0,0,0])
        return(pts)
    def Z(pts,a):
        pts=pts+a*2**(-(pts[:,[4]]+1))*np.array([0,0,1,0,0])
        return(pts)
    
    def SortRows(a,i):
    	from operator import itemgetter #, attrgetter
    	a=np.array(sorted(a, key=itemgetter(i)));
    	return(a);
    Original=np.around(Original*2**9).astype(float)*2**-9
    Allpoints=np.append(X(Y(Z(Original,-1),-1),-1),X(Y(Z(Original,1),-1),-1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,-1),1),-1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,1),1),-1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,-1),-1),1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,1),-1),1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,-1),1),1),axis=0)
    Allpoints=np.append(Allpoints,X(Y(Z(Original,1),1),1),axis=0)
    s=Original.shape[0];
    cells1=np.zeros((s,0),dtype=int)
    #cells[:]=a[:]
    for i in range(0,8):
        cells1=np.append(cells1,np.transpose([np.array(range(0,s))])+s*i,axis=1)
    #%%   
    Allsorted=np.append(Allpoints,np.transpose([np.array(range(0,s*8))]),axis=1)    
    Allsorted=SortRows(Allsorted,2)
    Allsorted=SortRows(Allsorted,1)
    Allsorted=SortRows(Allsorted,0)
    #%%
    Allsorted=np.around(Allsorted*2**9).astype(float)*2**-9
    #%%
    f=np.zeros((Allsorted.shape[0],8),dtype=int);f[:]=-1
    i=0
    j=0
    k=0
    f[j,k]=(Allsorted[i,5]).astype(int)
    while(i<8*s-1):
        if (Allsorted[i,0]==Allsorted[i+1,0]):
            if(Allsorted[i,1]==Allsorted[i+1,1]):
                if(Allsorted[i,2]==Allsorted[i+1,2]):
                    k=k+1;
                    f[j,k]=((Allsorted[i+1,5])).astype(int)
                else:
                    j=j+1
                    k=0
                    f[j,k]=(Allsorted[i+1,5]).astype(int)
            else :
                j=j+1
                k=0
                f[j,k]=(Allsorted[i+1,5]).astype(int)
        else:
            j=j+1
            k=0
            f[j,k]=(Allsorted[i+1,5]).astype(int)
        i=i+1;
    #%%    
    #f=f[0:np.where(np.isnan(f[:,0]))[0][0],:]
    f=f[0:np.where(f[:,0]==-1)[0][0],:]
    #%%
    
    points=Allpoints[f[:,0],0:5]
    cells2=(np.array(range(0,8*s+1)))
    #%%
    for i in range(0,8):
        cells2[f[:,i]]=np.array([range(0,f.shape[0])])    
    cells2=np.delete(cells2,-1,axis=0)
    #%%
    
    cells=cells2[cells1]
    cells=np.append(np.ones((cells.shape[0],1),dtype=int)*8,cells,axis=1)
    
    del Allpoints,Allsorted
    #%%
 
    f=open(filename, 'w')
    f.write('# vtk DataFile Version 2.0\nGerris simulation version 1.3.2 (131206-155120) - Generated via Python Post Processing code - Author: Mohamed Houssein GHANDOUR\nASCII\nDATASET UNSTRUCTURED_GRID')
    f.write('\nPOINTS ' + str(points.shape[0]) + ' float\n')   
    f.close()
    f=open(filename, 'ab')
    np.savetxt(f,points[:,0:3], fmt='%1.6f', delimiter=' ', newline='\n')
    f.close()
    f=open(filename, 'a')
    f.write('\nCELLS ' + str(cells.shape[0]) + ' ' + str(cells.shape[0]*9)+'\n')
    #f=open('couronne.vtk','a')
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
    f=open(filename, 'a')
    f.write('\nPOINT_DATA ' + str(points.shape[0]) + '\n SCALARS T1 float \n LOOKUP_TABLE default \n')
    f.close()
    f=open(filename, 'ab')
    np.savetxt(f, points[:,[3]],  fmt='%1.6f', delimiter=' ', newline='\n')
    f.close()
