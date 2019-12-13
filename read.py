import numpy as np


ram=np.loadtxt(open('RAM').readlines(),dtype=float)
ram=int(ram*128*1024*1024*1024)
for i in np.loadtxt(open('Steps').readlines(),dtype=int)[:-1]:
    f=open("step-"+str(i)+".txt","r");
    a=f.readlines(ram);
    data=np.loadtxt(a);
    while True:
    	print('    A matrix with the dimension of '+ str(data.shape[0])+ 'x'+\
           str(data.shape[1])+' floats have been read')
    	a=f.readlines(ram);
    	if not a:
    		break;
    	data=np.append(data,np.loadtxt(a),axis=0)
    
    #empty_levels=np.zeros_like(data[:,[0]])
#    while True:   
#        Oil=input('do you have an oil layer? (y/n)    ')
#        if( (Oil=='y') | (Oil=='Y')):
#            Oil=1
#            break;
#        if( (Oil=='n') | (Oil=='N')):
#            Oil=0
#            break;
#        Oil=input('Wrong input! do you have an oil layer? (y/n)    ')
#    
#    if (Oil==0):
#        data_final=np.append(data[:,[0,2,1,0,3,4]],data[:,6:],axis=1)
#        
#    if (Oil==1):
#        data_final=np.append(data[:,[0,2,1,0,3,4,5]],data[:,6:],axis=1)
        
    data_final=np.append(data[:,[0,2,1,0,3,4]],data[:,6:],axis=1)    
    data_final[:,3]=0 #This is to be used later for levels
    np.save('data-'+str(i)+'.npy',data_final);
