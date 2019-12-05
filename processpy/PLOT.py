def plt3d(Pts):
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import Axes3D
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	ax.scatter(Pts[:,0],Pts[:,1],Pts[:,2],s=10,marker=".")
	plt.show()
def plt3dmulti(arr):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()    
    ax = fig.add_subplot(111,projection='3d')

    for i in range(1,len(arr)):   
        Pts=arr[i];
        ax.scatter(Pts[:,0],Pts[:,1],Pts[:,2],s=10,marker=".")
    plt.show()    
def CheckRange(X):
	import matplotlib.pyplot as mplot
	s=X.shape[0];
	mplot.plot(X[:,0],'b',X[:,1],'r',range(0,s),'g')
	mplot.show()
def pltdrops(X):
    import matplotlib.pyplot as mplot
    mplot.scatter(X[:,0],X[:,1],marker='o',s=50*X[:,2])
    mplot.show();
    
def pltsizealpha(X):
    import matplotlib.pyplot as mplot
    mplot.scatter(X[:,0],X[:,1],marker='o',s=1)
    mplot.show();
