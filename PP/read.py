import numpy as np
f=open("/home/mhg/temp/text.txt","r");
a=f.readlines(1024*1024*1024);
G=np.loadtxt(a);
while True:
	print(G.shape)
	a=f.readlines(1024*1024*1024);
	if not a:
		break;
	G=np.append(G,np.loadtxt(a),axis=0)
G=G[:,[0,2,1,16,30,29,13,5,7,6,3,32,28]];
np.save('/home/mhg/temp/data.npy',G);
