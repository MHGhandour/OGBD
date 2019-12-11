import numpy as np


i=input('please insert the step number:    ')
ram=input('please insert the amount of RAM available, in GiB:    ')
ram=float(ram)
ram=int(ram*128*1024*1024*1024)
f=open("step-"+i+".txt","r");
a=f.readlines(ram);
data=np.loadtxt(a);
while True:
	print('    A matrix with the dimension of '+ str(data.shape[0])+ 'x'+str(data.shape[1])+' floats have been read')
	a=f.readlines(ram);
	if not a:
		break;
	data=np.append(data,np.loadtxt(a),axis=0)

while True:   
    Oil=input('do you have an oil layer? (y/n)    ')
    if( (Oil=='y') | (Oil=='Y')):
        Oil=1
        break;
    if( (Oil=='n') | (Oil=='N')):
        Oil=0
        break;
    Oil=input('Wrong input! do you have an oil layer? (y/n)    ')

if (Oil==0):
    data_final=np.append(data[:,[0,2,1,3,4]],data[:,6:],axis=1)
np.save('data-'+i+'.npy',data_final);
