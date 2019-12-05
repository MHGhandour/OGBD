
# Functions
#from tempfile import mkdtemp
#import os.path as path

#%% General functions
from __future__ import division
from multiprocessing import Pool
import numpy as np
import os.path
import time
Gigs=65; #I suppose i have only 38GB to use
max_ram=Gigs*1024*1024*1024;
RAM_constraint=0


def findlevel(Pts):
    Lvl=Pts[:,[3,4,5]]
    Lvl[:]=10;
    x=Pts[:,0];y=Pts[:,1];z=Pts[:,2];
    Lvl[x%0.001953125==0,0]=8
    Lvl[x%0.00390625==0,0]=7
    Lvl[x%0.0078125==0,0]=6
    Lvl[x%0.015625==0,0]=5
    Lvl[x%0.03125==0,0]=4
    Lvl[x%0.0625==0,0]=3
    Lvl[x%0.125==0,0]=2
    Lvl[x%0.25==0,0]=1
    Lvl[x%0.5==0,0]=0
    
    Lvl[y%0.001953125==0,1]=8
    Lvl[y%0.00390625==0,1]=7
    Lvl[y%0.0078125==0,1]=6
    Lvl[y%0.015625==0,1]=5
    Lvl[y%0.03125==0,1]=4
    Lvl[y%0.0625==0,1]=3
    Lvl[y%0.125==0,1]=2
    Lvl[y%0.25==0,1]=1
    Lvl[y%0.5==0,1]=0
    
    Lvl[z%0.001953125==0,2]=8
    Lvl[z%0.00390625==0,2]=7
    Lvl[z%0.0078125==0,2]=6
    Lvl[z%0.015625==0,2]=5
    Lvl[z%0.03125==0,2]=4
    Lvl[z%0.0625==0,2]=3
    Lvl[z%0.125==0,2]=2
    Lvl[z%0.25==0,2]=1
    Lvl[z%0.5==0,2]=0
    check=(Lvl[:,0]==Lvl[:,1])*(Lvl[:,1]==Lvl[:,2])
    if(np.where(~check)[0].shape[0]==0):
        return(Lvl[:,0])
    else:
        return('error in levels')


def keepLv(MainPts,*arr):
        s=MainPts.shape[0];
        idx=np.zeros((s,),dtype=bool);
        for i in range(len(arr)):
            idx2=MainPts[:,3]==arr[i]
            idx =idx + idx2
        return(idx);
    
def SortRows(a,*o): #o for order
    if(len(o)==3):
        b=np.lexsort((a[:,o[2]],a[:,o[1]],a[:,o[0]]))
    else:
        if(len(o)==2):
            b=np.lexsort((a[:,o[1]],a[:,o[0]]))
        else: 
            b=np.lexsort((a[:,o[0]],))
    return(a[b,:])

def reshape(arr): #Takes one array shape [s,] give [s.1] 
    s=arr.shape[0]
    arr=arr.reshape(s,1)
    return(arr);
   
def remove_air(OriginalPts):
    j=OriginalPts[:,4]==0
    b=np.where(j==True);
    MainPts=np.delete(OriginalPts,b,axis=0);

    MainPts=SortRows(MainPts,0,1,2)
    a=(MainPts[0:-2,0:3]==MainPts[1:-1,0:3])
    a=np.sum(np.array(a),axis=1)
    a=np.where(a==3)[0]
    MainPts=np.delete(MainPts,a,0)
    #print(a.shape,'row deleted, because of duplicate cells')
    return(MainPts);
def remove_water(OriginalPts):
    j=OriginalPts[:,4]==0
    b=np.where(j==False);
    MainPts=np.delete(OriginalPts,b,axis=0);

    MainPts=SortRows(MainPts,0,1,2)
    a=(MainPts[0:-2,0:3]==MainPts[1:-1,0:3])
    a=np.sum(np.array(a),axis=1)
    a=np.where(a==3)[0]
    MainPts=np.delete(MainPts,a,0)
    #print(a.shape,'row deleted, because of duplicate cells')
    return(MainPts);

#%% Decompose Function

def IntervalRange(LvPts,Pts_L1,Col):
        def whereis(i):
            I=np.where(LvPts[:,Col]>=Pts_L1[j1[i],Col]-clv)[0][0];
            J=np.where(LvPts[:,Col]<=Pts_L1[j1[i],Col]+clv)[0][-1];
            return(I,J)    
    #this function produces XPts, YPts and ZPts
        
        #t0=time.time()
        s=Pts_L1.shape[0];
        lv=min(min(LvPts[:,3]),Pts_L1[0,3])
        clv=2**(-lv)
        R=np.zeros((s,2),dtype=int)
        j2=np.where((Pts_L1[0:-1,Col]-Pts_L1[1:s,Col]).astype(bool))[0]
        j1=j2+1
        j1=np.append(0,j1);j2=np.append(j2,s-1)
        for i in range(j1.shape[0]):
            [I,J]=whereis(i)
            R[j1[i]:(j2[i]+1),:]=np.ones((j2[i]-j1[i]+1,1))*[I,J];
        
        #print('IntervalRange took',time.time()-t0,'seconds')
        return(R);
       
def XI_IDing(XPts):
	i=0;s=XPts.shape[0];m=0;
	XInterval=XPts[[i],:];X=np.zeros((s,1),dtype=int);X[i,0]=m;
	for i in range(1,s):
	    if(np.logical_or(XPts[i,0]!=XPts[i-1,0],XPts[i,1]!=XPts[i-1,1])):
	      m=m+1;
	      XInterval=np.append(XInterval,XPts[[i],:],axis=0);
	    X[i,0]=m;
	return(X,XInterval);

def YZI_IDing(YZPts):
	i=0;s=YZPts.shape[0];m=0;
	Id_ref=np.append(np.array([[m]]),YZPts[[i],:],axis=1);
	YZ=np.zeros((s,1),dtype=int);YZ[i,0]=m;
	for i in range(1,s):
         if(np.logical_or(YZPts[i,0]!=YZPts[i-1,0],YZPts[i,1]!=YZPts[i-1,1])):
             m=m+1;
             Id_ref=np.append(Id_ref,np.append(np.array([[m]]),YZPts[[i],:],\
             axis=1),axis=0);
         YZ[i,0]=m;    
	return(YZ,Id_ref)


def Fill(YId_ref,ZId_ref,s1,s2y,s2z,yaxe,zaxe):
    #axe is the axe correction for y and z
    global RAM_constraint
    global max_ram
    if((s1*(s2y+s2z))<max_ram):
        #print('no RAM Constraint, Filling ...')
        #t0=time.time()
        RAM_constraint=0
#ERROR: i tried here to make a direct filling without the use of the for loop 
#but apperrently it is too complicated, and not so sure to be that effective
#and i am time running, so i leave it to later
        YApply=np.zeros((s1,s2y),dtype='bool');
        for i in range(0,s2y):
            YApply[yaxe[YId_ref[0,i]:YId_ref[1,i]+1],i]=True
        #YApply=YApply[yaxe,:]
        ZApply=np.zeros((s1,s2z),dtype='bool')
        for i in range(0,s2z):
            ZApply[zaxe[ZId_ref[0,i]:ZId_ref[1,i]+1],i]=True
            #ZApply=ZApply[zaxe,:]
        #te=time.time()
        #print('Filled in', te-t0, 'seconds')
        return(YApply,ZApply)
    else:
        if(np.logical_and(s1*s2y<max_ram,s1*s2z<max_ram)):
            RAM_constraint=1
            print('RAM constraint 1, Filling ...')
            #t0=time.time()
            YApply=np.zeros((s1,s2y),dtype='bool');
            for i in range(0,s2y):
                YApply[yaxe[YId_ref[0,i]:YId_ref[1,i]+1],i]=True
                #YApply[:,i]=YApply[yaxe,i]
            np.save('temp/YApply.npy',YApply)
            del YApply
            ZApply=np.zeros((s1,s2z),dtype='bool')
            for i in range(0,s2z):
                ZApply[zaxe[ZId_ref[0,i]:ZId_ref[1,i]+1],i]=True
                #ZApply[:,i]=ZApply[zaxe,i]
            np.save('temp/ZApply.npy',ZApply)
            del ZApply
            #te=time.time()
            #print('Filled in', te-t0, 'seconds')
            return('temp/YApply.npy','temp/ZApply.npy')
        else:
            RAM_constraint=2
            fill_constrained(YId_ref,yaxe,'Y',s1,s2y)
            fill_constrained(ZId_ref,zaxe,'Z',s1,s2z)
            return('temp/YApply.npy','temp/ZApply.npy')
             
def fill_constrained(Id_ref,axe,AXIS,s1,s2):        
    #print('s1,s2',s1,s2)
    fILE='temp/'+AXIS+'Apply.npy'
    print('RAM Constraint state 2, Filling ...')
    t0=time.time()
    Apply = np.memmap(fILE, dtype='bool', mode='w+', shape=(s1,s2))
    for i in range(0,s2):
         Apply[axe[Id_ref[0,i]:Id_ref[1,i]+1],i]=True
         #Apply[:,i]=Apply[axe,i]
    te=time.time()
    print('Filled in', te-t0, 'seconds')
    return();


def IID_Referencing(XPts,YPts,ZPts,Ids,yaxe,zaxe):
     global s2y,s2z,s1
     s1=max(yaxe)+1;s1=np.int(s1);
     [X,XInterval]=XI_IDing(XPts);
     [Y,YId_ref]=YZI_IDing(YPts);Y=Y[Ids[:,1],:];
     YId_ref=np.transpose(YId_ref[:,1:3]);
     s2y=YId_ref.shape[1]; 
     [Z,ZId_ref]=YZI_IDing(ZPts);Z=Z[Ids[:,2],:];
     ZId_ref=np.transpose(ZId_ref[:,1:3]);
     s2z=ZId_ref.shape[1];
#     yaxe=np.zeros_like(Ids2[:,0])
#     zaxe=np.zeros_like(yaxe)
#     for i in range(0,Ids2.shape[0]):
#         yaxe[i]=Ids2[:,0][Ids2[i,0]==Ids2[:,1]]
#         zaxe[i]=Ids2[:,0][Ids2[i,0]==Ids2[:,2]]
     [YApply,ZApply]=Fill(YId_ref,ZId_ref,s1,s2y,s2z,yaxe,zaxe);
     ID_IRef=np.transpose(np.array([X,Y,Z]))
     ID_IRef=ID_IRef.reshape(ID_IRef.shape[1],ID_IRef.shape[2])
     return(XInterval,YApply,ZApply,ID_IRef);

def AppendID(Pts):
    s=Pts.shape[0]
    Pts=np.append(Pts,np.transpose([range(0,s)]),axis=1)
    return(Pts)
    
def Decompose(LvPts,Pts_L1): 
    global s2y,s2z,RAM_constraint
    #print('SORTING ...')
    #t0=time.time()
    #LvPts=SortRows(LvPts,0,1,2); #ERROR: is this even necessary?
    LvPts=AppendID(LvPts)
    #Pts_L1=SortRows(Pts_L1,0,1,2); #SAME HERE
    Pts_L1=AppendID(Pts_L1)
    XPts=IntervalRange(LvPts,Pts_L1,0);
    #
    LvPts=SortRows(LvPts,1);
    yaxe=LvPts[:,-1].astype(int)
    Pts_L1=SortRows(Pts_L1,1);
    Pts_L1=AppendID(Pts_L1)
    YPts=IntervalRange(LvPts,Pts_L1,1);
    #
    LvPts=SortRows(LvPts,2);
    zaxe=LvPts[:,-1].astype(int)
    Pts_L1=SortRows(Pts_L1,2);
    Pts_L1=AppendID(Pts_L1)
    ZPts=IntervalRange(LvPts,Pts_L1,2);
    #
    #ERROR: is all this duplicate Ids really necessary?? Probably+
    #
    Ids1=(Pts_L1[:,[-3,-2,-1]].astype(int));
    Ids1[Pts_L1[:,-3].astype(int),:]=Pts_L1[:,[-3,-2,-1]].astype(int)
#    Ids2=np.zeros_like(LvPts[:,0:3],dtype=int);
#    Ids2[LvPts[:,-3].astype(int),:]=LvPts[:,[-3,-2,-1]].astype(int)
    #te=time.time()
    #print('Sorted in', te-t0, 'seconds')
    [XInterval,YApply,ZApply,ID_IRef]=IID_Referencing(XPts,YPts,ZPts,Ids1,yaxe,zaxe)
    
    return(XInterval,YApply,ZApply,ID_IRef);

#%% Neighbouring Function
def Distribute(ID_Iin,XInterval):
	s=ID_Iin.shape[0];
	#m=Pts_in[0,0];
	#M=Pts_in[-1,0];
	i=0;
	A=np.empty((1,4));A[:]=np.nan;A=A.astype(int);
	B=np.empty((1,4));B[:]=np.nan;B=B.astype(int);
	A[-1,0]=i; 
	A[-1,2]=XInterval[ID_Iin[i,0],0];
	A[-1,3]=XInterval[ID_Iin[i,0],1];
	for i in range(1,s):
		if(ID_Iin[i,0]!=ID_Iin[i-1,0]):
	        	A[-1,1]=i-1;
	        	A=np.append(A,B,axis=0)
	        	A[-1,0]=i;
	        	A[-1,2]=XInterval[ID_Iin[i,0],0];
	        	A[-1,3]=XInterval[ID_Iin[i,0],1];
	A[-1,1]=s-1;Dist=A;
	return(Dist);

def extract(YApply,ZApply,Dist,J,K,s2y,s2z):
    global RAM_constraint;
    SX=Dist[0,3]-Dist[0,2]+1;index_o=np.zeros((SX,),dtype='bool');
    if(RAM_constraint==0):
        #print('        no RAM constraint, extracting ...')
        #t0=time.time()
        index_o=np.sum((YApply[Dist[0,2]:Dist[0,3]+1,J]*ZApply[Dist[0,2]:\
                             Dist[0,3]+1,K]),axis=1)
        #te=time.time()
        #print('        Extracted in',te-t0, 'seconds')
        return(index_o);
        #ERROR i should here get index_o directly
    if(RAM_constraint==1):
        #print('        RAM constraint 1, extracting ...')
        #t0=time.time()
        max_ram2=max_ram-np.size(YApply);
        interval=np.int(max_ram2/s2z)#,np.int(max_ram2/8));#Error why the
        #                                                     #second element?
        YApp=np.load(YApply,mmap_mode='r+');
        ZApp=np.load(ZApply,mmap_mode='r+');
        for i in range(0,SX,interval):
            index_o[i:min(i+interval,SX)]=np.sum((YApp[Dist[0,2]+i:Dist[0,2]+\
                    min(i+interval,SX),J]*ZApp[Dist[0,2]+i:Dist[0,2]+min(i+\
                       interval,SX),K]),dtype='bool',axis=1);
        #te=time.time()
        #print('        Extracted in',te-t0, 'seconds')
        return(index_o);
        
    if(RAM_constraint==2):
        #print('        RAM constraint 2, extracting ...')
        #t0=time.time()
        interval=np.int(max_ram/max(s2y,s2z)/2)#,np.int(max_ram/16));
                                                #Error why the second element?
        YApp=np.memmap(YApply, dtype='bool', mode='r', shape=(s1,s2y))
        ZApp=np.memmap(ZApply, dtype='bool', mode='r', shape=(s1,s2z))
        for i in range(0,SX,interval):
            index_o[i:min(i+interval,SX)]=np.sum((YApp[Dist[0,2]+i:Dist[0,2]+\
                    min(i+interval,SX),J]*ZApp[Dist[0,2]+i:Dist[0,2]+min(i+\
                       interval,SX),K]),dtype='bool',axis=1);
        #te=time.time()
        #print('        Extracted in',te-t0, 'seconds')
        return(index_o);
def Neighbouring(XInterval,YApply,ZApply,ID_Iin):
    global s1,s2y,s2z,RAM_constraint#in1 is the index in the lower level
    s1=YApply.shape[0]
    index_out=np.zeros((s1,),dtype=bool)    	
    Dist=Distribute(ID_Iin,XInterval);
    S=Dist.shape[0];
    for i in range(0,S):
        J=ID_Iin[Dist[i,0]:(Dist[i,1]+1),1];
        K=ID_Iin[Dist[i,0]:(Dist[i,1]+1),2];
        index_o=extract(YApply,ZApply,np.array([Dist[i,:]]),J,K,s2y,s2z);
        index_out[Dist[i,2]:(Dist[i,3]+1)]=index_out[Dist[i,2]:\
                       (Dist[i,3]+1)]+index_o;
             #ERRORi can apend this inside the extract function
    return(index_out)
    
#%%
def initialize(MainPts):
    Gi_Lv=keepLv(MainPts,min(MainPts[:,3]).astype(int));
    LvPts=MainPts[Gi_Lv,:];
    [XInterval,YApply,ZApply,ID_IRef]=Decompose(LvPts,LvPts) #s2y and s2z are the shape[1] 
                                                    #Y_Apply and Z_Apply                                              
    index_in=np.zeros((LvPts.shape[0],),dtype=bool);index_in[0]=True;
    Li_1=np.ones((LvPts.shape[0],),dtype=bool);
    Li_splash=Neighbouring(XInterval,YApply,ZApply,ID_IRef[index_in[Li_1],:]);    
    Gi_splash=np.zeros((MainPts.shape[0],),dtype=bool);
    Gi_splash[Gi_Lv]=Li_splash;
    index_in=Gi_splash[Gi_Lv]
    index_passed=np.zeros_like(index_in)
    nei=0;
    while(np.sum(index_in,dtype=bool)):
        nei=nei+1;
        index_passed=index_passed+index_in
        Li_splash=Neighbouring(XInterval,YApply,ZApply,ID_IRef[index_in[Li_1],:]);
        Gi_splash[Gi_Lv]=Gi_splash[Gi_Lv]+Li_splash;
        index_in=Gi_splash[Gi_Lv]*~(index_passed)
    #print('First Level neighboured,',nei,'times')
    return(Gi_splash)

def initialize_cavity(MainPts,level):

    Gi_Lv=keepLv(MainPts,level);
    LvPts=MainPts[Gi_Lv,:];
    [XInterval,YApply,ZApply,ID_IRef]=Decompose(LvPts,LvPts) #s2y and s2z are the shape[1] 
                                                    #Y_Apply and Z_Apply                                              
    index_in=np.zeros((LvPts.shape[0],),dtype=bool);index_in[0]=True;
    Li_1=np.ones((LvPts.shape[0],),dtype=bool);
    Li_splash=Neighbouring(XInterval,YApply,ZApply,ID_IRef[index_in[Li_1],:]);    
    Gi_splash=np.zeros((MainPts.shape[0],),dtype=bool);
    Gi_splash[Gi_Lv]=Li_splash;
    index_in=Gi_splash[Gi_Lv]
    index_passed=np.zeros_like(index_in)
    nei=0;
    while(np.sum(index_in,dtype=bool)):
        nei=nei+1;
        index_passed=index_passed+index_in
        Li_splash=Neighbouring(XInterval,YApply,ZApply,ID_IRef[index_in[Li_1],:]);
        Gi_splash[Gi_Lv]=Gi_splash[Gi_Lv]+Li_splash;
        index_in=Gi_splash[Gi_Lv]*~(index_passed)
    #print('First Level neighboured,',nei,'times')
    return(Gi_splash)
#%% Enrichement Function    
def enrichment(MainPts,Gi_splash,level1,level2):
    Gi_Lv=keepLv(MainPts,level1,level2);
    index_in=Gi_splash[Gi_Lv];
    LvPts=MainPts[Gi_Lv,:];
    Li_1=keepLv(LvPts,level1);
    #Li_2=reshape(keepLv(LvPts,np.array([level2])));
    Pts_L1=LvPts[Li_1,:]
    LvPts2=MainPts[~Gi_splash*Gi_Lv,:]
    if(LvPts2.shape[0]==0):
        return(Gi_splash)
    if(Pts_L1.shape[0]==0):
        return(Gi_splash)
    clv=2**(-min(min(LvPts2[:,3]),Pts_L1[0,3]))
    condition1=Pts_L1[:,0]>=(min(LvPts2[:,0])-clv)
    condition2=Pts_L1[:,0]<=(max(LvPts2[:,0])+clv)
    condition3=Pts_L1[:,1]>=(min(LvPts2[:,1])-clv)
    condition4=Pts_L1[:,1]<=(max(LvPts2[:,1])+clv)
    condition5=Pts_L1[:,2]>=(min(LvPts2[:,2])-clv)
    condition6=Pts_L1[:,2]<=(max(LvPts2[:,2])+clv)
    total_condition=condition1*condition2*condition3*condition4*condition5*condition6
    Li_1[Li_1]=total_condition
    Pts_L1=LvPts[Li_1,:]
    if(Pts_L1.shape[0]==0):
        return(Gi_splash)
    [XInterval,YApply,ZApply,ID_IRef]=Decompose(LvPts2,Pts_L1)
    if(type(ZApply)==np.ndarray):
        ram_consumed=(np.size(YApply)+np.size(ZApply))//(1024**3)
    nei=0;
    t1=time.time()
    index_passed=np.zeros_like(index_in)
    index_out=~Gi_splash*Gi_Lv
    while(np.sum(index_in[Li_1],dtype=bool)):
        nei=nei+1;
        index_passed=index_passed+index_in
        Li_splash=Neighbouring(XInterval,YApply,ZApply,ID_IRef[index_in[Li_1],:]);
        Gi_splash[index_out]=Gi_splash[index_out]+Li_splash;
        index_in=Gi_splash[Gi_Lv]*~(index_passed)
    del YApply,ZApply
    #print('  Levels',level1,level2,'processed ..',ram_consumed,'GiB were consumed, and' ,'neighboured,',nei,'times, in ', time.time()-t1, 'seconds')
    return(Gi_splash)
#%%Progrossive
def Progressive(MainPts,Gi_splash):
    for level in range(min(MainPts[:,3]).astype(int),max(MainPts[:,3]).astype(int)):
        Gi_splash=enrichment(MainPts,Gi_splash,level,level+1)    
    return(Gi_splash)
#%% Regressive
def Regressive(MainPts,Gi_splash):
    for level in range(max(MainPts[:,3]).astype(int),min(MainPts[:,3]).astype(int),-1):
        #what i can do here is to use min(MainPts[~Gi_splash,3]) so i wouldn't go into if conditions
        Gi_splash=enrichment(MainPts,Gi_splash,level,level-1)
    return(Gi_splash)
#%% LAPS
def LAPS(MainPts,Gi_splash,Gi_splash2):
    #print(' New Lap')
    Gi_splash=Regressive(MainPts,Gi_splash)
    Gi_splash3=np.zeros_like(Gi_splash);Gi_splash3[:]=Gi_splash[:]
    if(~np.sum(Gi_splash2^Gi_splash3,dtype=bool)):
        return(Gi_splash)
    Gi_splash=Progressive(MainPts,Gi_splash)
    Gi_splash2=np.zeros_like(Gi_splash);Gi_splash2[:]=Gi_splash[:]
    if(~np.sum(Gi_splash2^Gi_splash3,dtype=bool)):
        return(Gi_splash)
    Gi_splash=LAPS(MainPts,Gi_splash,Gi_splash2)
    return(Gi_splash)
