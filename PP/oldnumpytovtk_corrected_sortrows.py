def npy2vtk(Original,filename):
    import numpy as np
    #Original=np.load('MainPts-5350.npy')
    #%%
    def X(pts,a):
        pts=pts+a*2**(-(pts[:,[3]]+1))*np.array([1,0,0,0,0])
        return(pts)
    def Y(pts,a):
        pts=pts+a*2**(-(pts[:,[3]]+1))*np.array([0,1,0,0,0])
        return(pts)
    def Z(pts,a):
        pts=pts+a*2**(-(pts[:,[3]]+1))*np.array([0,0,1,0,0])
        return(pts)
    def repeated(Pts):
        Pts=SortRows(Pts,0,1,2)
        a=(Pts[0:-1,0:3]==Pts[1:Pts.shape[0],0:3])
        #a=np.sum(np.array(a),axis=1)
        #a=np.where(a==3)[0]
        return(np.append(True,(~(a[:,0]*a[:,1]*a[:,2]))))
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
    #%%
    Allsorted=SortRows(Allsorted,0,1,2)
    #%%
    g=np.zeros((Allsorted.shape[0],8),dtype=int);g[:]=-1
    i=0
    j=0
    k=0
    g[j,k]=(Allsorted[i,5]).astype(int)
    sf=g.shape[0]
    while(i<sf-1):
        if (Allsorted[i,0]==Allsorted[i+1,0]):
            if(Allsorted[i,1]==Allsorted[i+1,1]):
                if(Allsorted[i,2]==Allsorted[i+1,2]):
                    k=k+1;
                    g[j,k]=((Allsorted[i+1,5])).astype(int)
                else:
                    j=j+1
                    k=0
                    g[j,k]=(Allsorted[i+1,5]).astype(int)
            else :
                j=j+1
                k=0
                g[j,k]=(Allsorted[i+1,5]).astype(int)
        else:
            j=j+1
            k=0
            g[j,k]=(Allsorted[i+1,5]).astype(int)
        i=i+1;
    #%%    
    #f=f[0:np.where(np.isnan(f[:,0]))[0][0],:]
    g=g[0:np.where(g[:,0]==-1)[0][0],:]
    #%%
    points=Allpoints[g[:,0],:];
    cells2=(np.array(range(0,8*s+1)))
    #%%
    for i in range(0,8):
        cells2[g[:,i]]=np.array([range(0,g.shape[0])])    
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
    np.savetxt(f, points[:,[4]],  fmt='%1.6f', delimiter=' ', newline='\n')
    f.close()
