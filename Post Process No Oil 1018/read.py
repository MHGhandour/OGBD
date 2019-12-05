import numpy as np
f=open("text.txt","r");
a=f.readlines(1024*1024*1024);
G=np.loadtxt(a);
while True:
	print(G.shape)
	a=f.readlines(1024*1024*1024);
	if not a:
		break;
	G=np.append(G,np.loadtxt(a),axis=0)
np.save('data.npy',G);
