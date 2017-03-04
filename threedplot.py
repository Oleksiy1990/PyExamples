import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(-5, 5, 0.2)
Y = np.arange(-5, 5, 0.2)
X, Y = np.meshgrid(X, Y) #apparently this is not necessary 
omega = 3
Z = np.exp(-2*X**2/omega**2 - 2*Y**2/(omega-2)**2)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
#print(Z)
#plt.imshow(Z)
#fig.savefig("testfig.png")
plt.show()


#fig = plt.figure()
	#ax = fig.add_subplot(111, projection='3d')
	#XX = np.arange(-5, 5, 0.2)
	#YY = np.arange(-5, 5, 0.2)
	#X, Y = np.meshgrid(XX, YY,sparse=False)
	#Z = residual_2D(p_fit2D,X,Y,data=None, eps=None)
	#surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,\
    #                   linewidth=0, antialiased=False)
	#plt.show()
