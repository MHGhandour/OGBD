
# Functions
#from tempfile import mkdtemp
#import os.path as path
import numpy as np

def LetLev(MainPts,arr):
        s=MainPts.shape[0];
        idx=np.zeros((s,),dtype=bool);
        for i in range(0,arr.shape[0]):
            idx =idx + MainPts[:,4]==arr[i]
        return(idx);
    
def SortRows(a,i):
	from operator import itemgetter #, attrgetter
	a=np.array(sorted(a, key=itemgetter(i)));
	return(a);

def LetPlainOnly(MainPts):
        j=MainPts[:,3]==0
        b=np.where(j==True);
        MainPts=np.delete(MainPts,b,axis=0);
        return MainPts;
        
def RANGE(Pts,Col):
        s=Pts.shape[0];
        R=np.empty((s,2));
        R[:]=np.nan
        i=0;
        while(np.isnan(R[-1,1])):
          j=np.array(np.where(np.logical_and(Pts[:,Col]==Pts[i,Col],Pts[:,4]==\
          Pts[:,4])))[0,-1];
          I=np.array(np.where(Pts[:,Col]>=Pts[i,Col]-1.5*2**-Pts[0,4]))[0,0];
          J=np.array(np.where(Pts[:,Col]<=Pts[i,Col]+1.5*2**-Pts[0,4]))[0,-1];
          R[i:j+1,:]=np.ones((j-i+1,1))*[I,J];
          i=j+1;
        R=R.astype(int)
        return(R);

def Organize(Pts,level):
    MainPts=LetPlainOnly(Pts);
    MainPts[:,4]=0*MainPts[:,4]+1*MainPts[:,5]+2*MainPts[:,6]+3*MainPts[:,7]+\
    4*MainPts[:,8]+5*MainPts[:,9]+6*MainPts[:,10]+7*MainPts[:,11]+8*MainPts[:,12];
    MainPts=np.delete(MainPts,range(5,13),axis=1)
    MainPts[:,0:3]=(MainPts[:,[0,1,2]]/(2**(-MainPts[:,[4]])*[[1,1,1]]))*2;
    MainPts[:,0:3]=MainPts[:,0:3].astype(int);
    MainPts[:,0:3]=MainPts[:,0:3].astype(float)/2;
    MainPts[:,0:3]=MainPts[:,0:3]*(2**(-MainPts[:,[4]])*[1,1,1])
    MainPts=SortRows(MainPts,2);
    MainPts=SortRows(MainPts,1);
    MainPts=SortRows(MainPts,0);
    index1=MainPts[:,4]==level;
    Pts=MainPts[index1,0:5];
    return(MainPts,Pts);

def RSHP(arr):
    s=arr.shape[0]
    arr=arr.reshape(s,1)
    return(arr);
 
#%% Phases Function
def XIntervalId(XPts):
	i=0;s=XPts.shape[0];m=0;
	XInterval=XPts[[i],:];X=np.zeros((s,1),dtype=int);X[i,0]=m;
	for i in range(1,s):
	    if(np.logical_or(XPts[i,0]!=XPts[i-1,0],XPts[i,1]!=XPts[i-1,1])):
	      m=m+1;
	      XInterval=np.append(XInterval,XPts[[i],:],axis=0);
	    X[i,0]=m;
	return(X,XInterval);

def YZIntervalId(YZPts):
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


def Fill(Id_ref,s1,s2,axe,fILE):
    max_ram=40*1024*1024;
    Apply = np.memmap(fILE, dtype='bool', mode='w+', shape=(s1,s2))
    Apply[:]=False;
    for i in range(0,s2):
         Apply[Id_ref[0,i]:Id_ref[1,i]+1,i]=np.ones((1,Id_ref[1,i]-\
         Id_ref[0,i]+1),dtype=bool);
#    interval=np.int(max_ram/s1);
    Apply=Apply[axe,:];
#    for i in range(0,s2,interval):
#        Apply[i:i+interval,:]=Apply[axe[i:i+interval],:];
    return();


def Idlize(XInterval,YInterval,ZInterval,Ids):
 s1=Ids[-1,0]+1;s1=np.int(s1);
 [X,XInterval]=XIntervalId(XInterval);
 [Y,Id_ref]=YZIntervalId(YInterval);Y=Y[Ids[:,1],:];
 Id_ref=np.transpose(Id_ref[:,1:3]);
 #fILE = path.join('/media/mhg/64BCAE6C40E79E46/tmp/', 'Yapply.dat')
 s2y=Id_ref.shape[1]; 
 Fill(Id_ref,s1,s2y,Ids[:,1],'Yapply.dat');
 [Z,Id_ref]=YZIntervalId(ZInterval);Z=Z[Ids[:,2],:];
 Id_ref=np.transpose(Id_ref[:,1:3]);
 #fILE = path.join('/media/mhg/64BCAE6C40E79E46/tmp/', 'Zapply.dat')
 s2z=Id_ref.shape[1]; 
 Fill(Id_ref,s1,s2z,Ids[:,2],'Zapply.dat');
 Ref_Pts=np.transpose(np.array([X,Y,Z]))
 Ref_Pts=Ref_Pts.reshape(Ref_Pts.shape[1],Ref_Pts.shape[2])
 return(XInterval,Ref_Pts,s1,s2y,s2z);
 
def Phases(Pts): 
    [s1, s2]=Pts.shape
    Pts=SortRows(Pts,2);
    Pts=SortRows(Pts,1);
    Pts=SortRows(Pts,0);
    #
    Pts=SortRows(Pts,0);
    Pts=np.append(Pts,np.transpose([range(0,s1)]),axis=1);
    XInterval=RANGE(Pts,0);
    #
    Pts=SortRows(Pts,1);
    Pts=np.append(Pts,np.transpose([range(0,s1)]),axis=1);
    YInterval=RANGE(Pts,1);
    #
    Pts=SortRows(Pts,2);
    Pts=np.append(Pts,np.transpose([range(0,s1)]),axis=1);
    ZInterval=RANGE(Pts,2);
    #
    Pts=SortRows(Pts,-1);
    Pts=SortRows(Pts,-2);
    Pts=SortRows(Pts,-3);
    #
    Ids=Pts[:,[-3,-2,-1]].astype(int);
    [XInterval,Ref_Pts,s1,s2y,s2z]=Idlize(XInterval,YInterval,ZInterval,Ids)
    return(Ids,XInterval,Ref_Pts,s1,s2y,s2z);








 #%%Alpha Function
def Decompose(Pts_in,XInterval):
	s=Pts_in.shape[0];
	#m=Pts_in[0,0];
	#M=Pts_in[-1,0];
	i=0;
	A=np.empty((1,4));A[:]=np.nan;A=A.astype(int);
	B=np.empty((1,4));B[:]=np.nan;B=B.astype(int);
	A[-1,0]=i; 
	A[-1,2]=XInterval[Pts_in[i,0],0];
	A[-1,3]=XInterval[Pts_in[i,0],1];
	for i in range(1,s):
		if(Pts_in[i,0]!=Pts_in[i-1,0]):
	        	A[-1,1]=i-1;
	        	A=np.append(A,B,axis=0)
	        	A[-1,0]=i;
	        	A[-1,2]=XInterval[Pts_in[i,0],0];
	        	A[-1,3]=XInterval[Pts_in[i,0],1];
	A[-1,1]=s-1; 
	return(A);

def summation(A,J,K,s1,s2y,s2z):
    SX=A[0,3]-A[0,2]+1;
    Y_Apply = np.memmap('Yapply.dat', dtype='bool', mode='r+', offset=A[0,2]*\
    s2y,shape=(SX,s2y))
    Z_Apply = np.memmap('Zapply.dat', dtype='bool', mode='r+', offset=A[0,2]*\
    s2z,shape=(SX,s2z))
    max_ram=20*1024*1024*1024;#I suppose i have only 40+GB to use
    interval=np.int(max_ram/max(s2y,s2z));
    #print('Summation rows number:',SX);
    index_o=np.zeros((SX,1),dtype='bool');
    #print('test')
    if(interval>SX):
        YApp=np.zeros((SX,s2y),dtype='bool');
        ZApp=np.zeros((SX,s2z),dtype='bool');       
        YApp[:]=Y_Apply[:]
        ZApp[:]=Z_Apply[:]
      #  try1=YApp[:,J];
      #  try2=ZApp[:,K];
        index_o[:,0]=np.sum((YApp[:,J]*ZApp[:,K]),axis=1)
    else:
        print('RAM constraints >>>')
        for i in range(0,SX,interval):
            YApp=np.zeros((min(SX-i,interval),s2y),dtype='bool');
            ZApp=np.zeros((min(SX-i,interval),s2z),dtype='bool');
            #print('summation step..');
            YApp[0:interval,:]=Y_Apply[i:i+interval,:];
            ZApp[0:interval,:]=Z_Apply[i:i+interval,:];
            index_o[i:i+interval,0]=np.sum((YApp[0:interval,J]+ZApp\
            [0:interval,K]),dtype='bool',axis=1);
    return(index_o);

def Alpha(XInterval,Ref_Pts,index1,s1,s2y,s2z):
	index2=np.zeros((index1.shape[0],1),dtype=bool); 
	index_in=index1*(~index2); 
	while(np.sum(index_in,axis=0,dtype='bool')):
         #a=None;# if it causes problem make a=None
         Pts_in=Ref_Pts[index_in[:,0],:];			
         index_out=np.zeros(index1.shape,dtype=bool);
         A=Decompose(Pts_in,XInterval);
         S=A.shape[0];
         for i in range(0,S):
             J=Pts_in[A[i,0]:(A[i,1]+1),1];
             K=Pts_in[A[i,0]:(A[i,1]+1),2];
             index_o=summation(np.array([A[i,:]]),J,K,s1,s2y,s2z);
             index_out[A[i,2]:(A[i,3]+1)]=index_out[A[i,2]:(A[i,3]+1)]+index_o;
         index1=index1+index_out;
         index2=index2+index_in; 
         index_in=index1*(~index2);
         #print(np.where((index1!=index2)>0));    
	return(index1)