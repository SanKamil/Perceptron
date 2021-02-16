import numpy as np
import math
from math import e
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def foo_fi(v):
  y=1/(1+(e**(-1*v)))
  return y

def foo_derivative_fi(v):
  y=(1*e**(1*-v))/(((e**(1*-v))+1)**2)
  return y



x1_values = np.random.uniform(0.0, 1.0, 60)
x2_values = np.random.uniform(math.cos(0),math.cos(math.pi/2),60)

training_vector = []
test_vector = []
counter3 = 0

for i in range (0,60):
    if(i < 40):
        training_vector.append((x1_values[i],x2_values[i],1))
    elif(40<=i<60):
        test_vector.append((x1_values[i], x2_values[i],1))

test_vector = np.array(test_vector)
training_vector = np.array(training_vector)



for i in range (0,25):
    w = np.ones(120)
    w = w.reshape(40, 3)
    learning_rate = 0.9

    if(i<10):
        print("*********************************")
        print("weights changed")
        w = (((i+1)/2))*np.ones(120)
        w = w.reshape(40, 3)
        print("weights:", w[0])
    elif(10<=i<20):
        print("-------------------------------------")
        print("learning rate changed")
        learning_rate = learning_rate-((i-10)/10)
        print("learning rate:", learning_rate)
    elif(20 <= i):
        print("-------------------------------------")
        print("training set shuffled")
        np.random.shuffle(training_vector)
    error_store = []
    test_error_store = []
    counter = 0
    counter3 = 0
    error = np.ones(40)
    E = np.ones(40)
    while counter < 20000:
        v1 = (w[counter%40, 0]*training_vector[counter % 40, 0])
        v2 = (w[counter%40, 1]*training_vector[counter % 40, 1])
        v3 = (w[counter%40, 2]*training_vector[counter % 40, 2])
        v = v1+v2+v3
        fi = foo_fi(v)
        derivative_fi = foo_derivative_fi(v)
        yd = ((3*training_vector[counter%40,0])+(2 * training_vector[counter%40, 1]))/5.0

        error[counter%40] = 0.5 *((yd-fi)**2)

        w[(counter+1)%40] = w[counter%40] + learning_rate* (yd-fi) * derivative_fi * training_vector[counter % 40]

        if counter > 40 :
            result = error.sum()/40
            error_store.append((result,counter))
            if((result < 0.0002)):
                break
        counter = counter + 1
    print("epoch:", counter)
    print("last error in training:", result)

    while counter3 < 20:
        control_variable = w[(counter) % 40] * test_vector[counter3]
        control_variable = control_variable.sum()
        sonuc = foo_fi(control_variable)
        ydtest = ((3 * test_vector[counter3, 0]) + (2 * test_vector[counter3, 1]))/5.0
        test_error_store.append((abs(sonuc-ydtest)))

        counter3 += 1

    test_error_store = np.array(test_error_store)
    test_average_error = test_error_store.sum()
    print("average test error",test_average_error/20)





fig = plt.figure()
a,b = zip(*error_store)
plt.xlabel('epoch')
plt.ylabel('error')
plt.plot(b,a,"red")

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
(x, y) = np.meshgrid(np.linspace(0, 1, 40),
                     np.linspace(0, math.pi/2, 40))

z = 5*foo_fi(w[(counter)%40,0]*x+w[(counter)%40,1]*np.cos(y)+w[(counter)%40,2])
ax.plot_surface(x, y, z, color='r')
K = 3*x + 2*np.cos(y)
ax.plot_surface(x,y,K,color = 'bisque')
ax.view_init(0, 45)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(x, y, z, color='r')
ax.plot_surface(x,y,K,color = 'bisque')
ax.view_init(0, 90)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(x, y, z, color='r')
ax.plot_surface(x,y,K,color = 'bisque')
ax.view_init(0, 135)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(x, y, z, color='r')
ax.plot_surface(x,y,K,color='bisque')
ax.view_init(0, 180)
plt.show()

