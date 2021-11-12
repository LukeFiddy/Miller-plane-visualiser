
import numpy as np
import matplotlib.pyplot as plt


miller_index = np.array([2, 4, 3])
coord = 1/(miller_index+0.00001)
print(coord)
points = [[coord[0], 0, 0], [0, coord[1], 0], [0, 0, coord[2]]]

px, py, pz = points
x0, y0, z0 = px
x1, y1, z1 = py
x2, y2, z2 = pz

x = [x0, x1, x2]
y = [y0, y1, y2]
z = [z0, z1, z2]


sidexy0 = np.arange(px[0], py[0], 0.01)
sideyz0 = np.arange(py[0], pz[0], 0.01)
sidezx0 = np.arange(pz[0], px[0], 0.01)

sidexy1 = np.arange(px[1], py[1], 0.01)
sideyz1 = np.arange(py[1], pz[1], 0.01)
sidezx1 = np.arange(pz[1], px[1], 0.01)

sidexy2 = np.arange(px[2], py[2], 0.01)
sideyz2 = np.arange(py[2], pz[2], 0.01)
sidezx2 = np.arange(pz[2], px[2], 0.01)


if x0 > 1:
    xx = sidezx0[99]
    xy = sidezx1[99]
    xz = sidezx2[99]

elif x0 != 0:
    xx = sidezx0[-1]
    xy = 0
    xz = 0

if y1 > 1:
    yx = sidexy0[99]
    yy = sidexy1[99]
    yz = sidexy2[99]
elif y1 != 0:
    yx = 0
    yy = sidexy1[-1]
    yz = 0

if z2 > 1:
    zx = sideyz0[99]
    zy = sideyz1[99]
    zz = sideyz2[99]
elif z2 != 0:
    zx = 0
    zy = 0
    zz = sideyz2[-1]


x = [xx, xy, xz]
y = [yx, yy, yz]
z = [zx, zy, zz]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(x, y, z, color='r')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)


plt.show()
