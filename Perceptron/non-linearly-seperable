import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math
data_list = [[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1],[-1,-1],[-1,0],[-1,1],
             [-3,3],[-3,1],[-3,0],[-3,-1],[-3,-3],[-1,3],[-1,-3],
             [0,3],[0,-3],[1,3],[1,-3],[3,3],[3,1],[3,0],[3,-1],
             [3,-3],[-2,3],[-3,2],[-3,-2],[-2,-3],[2,3],[3,2],[3,-2],[2,-3]]

arr = np.array(data_list)

fi1 = []
fi2 = []
fi3 = []
fi_total= []

counter = 0
counter2 = 0
yd = np.ones(33)
s1 = []
s2 = []
learning_rate =1
w= np.ones(132)
w = w.reshape(33,4)
true_number =0
false_number = 0
while counter < 33:
    if 8< counter:
        yd[counter] = -1
    a= arr[counter, 0]
    b= arr[counter, 1]


    fi1.append(a)
    fi2.append(b)
    fi3.append((a**2 + b**2))
    c = a**2 + b**2
    fi_total.append([a,b,c,1]) #4 -> bias term
    counter += 1

fi_total = np.array(fi_total)
while counter2 < 500:
    a = w[(counter2) % 33] * fi_total[(counter2)%33]
    a = a.sum()
    if(a > 0):
        y  = 1;
    elif(a <= 0):
        y = -1;
    b = list(range(4))
    while c < 4:
        b[c] = (learning_rate / 2) * (yd[counter2%33]-y)
        c = c + 1
    c = 0

    w[(counter2+1)%33] = w[(counter2) % 33] + b * fi_total[(counter2 % 33)]

    if (yd[counter2%33] == y):
        true_number = true_number + 1
    else:
        false_number = false_number + 1
        true_number = 0

    if true_number > 33:
        break

    counter2 = counter2 + 1


print("epoch number:", counter2)


xdata = np.array(fi1[:9])
ydata = np.array(fi2[:9])
zdata = xdata**2 + ydata**2

xdata2 = np.array(fi1[9:])
ydata2 = np.array(fi2[9:])
zdata2 = xdata2**2 + ydata2**2


fig = plt.figure()
plt.plot(xdata,ydata,"blue",ls = " ",marker = "X")
plt.plot(xdata2,ydata2,"red",ls = " ",marker = "X")


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
(x, y) = np.meshgrid(np.linspace(-3, 3, 33),
                     np.linspace(-3, 3, 33))

z = -(w[(counter2)%33,0]*x+w[(counter2)%33,1]*y+w[(counter2)%33,3])/w[(counter2)%33,2]
ax.plot_surface(x, y, z, cmap='inferno')
ax.view_init(0, 45)
ax.scatter(xdata,ydata, zs=zdata, zdir='0',c='blue')
ax.scatter(xdata2,ydata2, zs=zdata2, zdir='0', c='red')
plt.show()
