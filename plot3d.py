# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np

# data = np.loadtxt('alphagamma.txt')

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# x, y = data[:, 0], data[:, 1]
# hist, xedges, yedges = np.histogram2d(x, y, bins=4)

# elements = (len(xedges) - 1) * (len(yedges) - 1)
# xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)

# xpos = xpos.flatten()
# ypos = ypos.flatten()
# zpos = data[:, 2].flatten()
# dx = 0.5 * np.ones_like(zpos)
# dy = dx.copy()
# dz = hist.flatten()

# ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

# plt.show()

# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np

# data = np.loadtxt('alphagamma.txt')
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(data[:, 0], data[:, 1], data[:, 2])

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# plt.show()


# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import matplotlib.pyplot as plt
# import numpy as np

# data = np.loadtxt('alphagamma.txt')

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = data[:, 0]*10
# Y = data[:, 1]*10
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = data[:, 2]/10.0
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# ax.set_zlim(-1.01, 1.01)

# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# fig.colorbar(surf, shrink=0.5, aspect=5)

# plt.show()




from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('alphagamma.txt')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# x, y = np.random.rand(2, 100) * 4
x, y = data[:, 0]*10, data[:, 1]*10
hist, xedges, yedges = np.histogram2d(x, y, bins=10)

elements = (len(xedges) - 1) * (len(yedges) - 1)
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)

xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(elements)
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = data[:,2]






ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

ax.set_xlabel('alpha')
ax.set_ylabel('gamma')
ax.set_zlabel('success rate')

xxx = [0,1,2,3,4,5,6,7,8,9,1]
labels = ['0','.1','.2','.3','.4','.5','.6','.7','.8','.9','1']
plt.xticks(xxx, labels)
plt.yticks(xxx, labels)


print xpos
print ypos
print zpos

print dx
print dy
print dz
plt.show()