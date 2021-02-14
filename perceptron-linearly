import numpy as np


arr = 5*np.random.random(280)-5
arr = arr.reshape(40,7)

counter = 0

total_error = 0
while counter < 20:
    arr[2*counter, 4] = 2
    arr[(2*counter)+1, 4] = -2
    arr[(counter, 5)] = 1 ##bias
    arr[(counter+20, 5)] = 1 ##bias
    arr[(2*counter), 6] = 1
    arr[(2*counter)+1, 6] = -1
    counter += 1

training_vector = arr[:25]
test_vector = arr[25:]

epoch = 60

for i in range (epoch):
    learning_rate = 0.5
    w = np.ones(150)
    w = w.reshape(25, 6)
    s1 = []
    s2 = []
    error_rate = 0
    true = 0
    false = 0
    counter2 = 0
    counter3 = 0
    true_n = 0
    false_n =0

    if(i<=20):
        print("------------------------------------------------")
        w = (i/4)*np.ones(150)
        w = w.reshape(25, 6)
        print("w weight = ",w[1])
        print("learning rate",learning_rate)
    elif(20<i<=40):
        print("------------------------------------------------")
        learning_rate = (i-20)*0.05
        print("learning rate:",learning_rate)
        print("w weight = ",w[1])
    elif(40<i<=60):
        print("------------------------------------------------")
        np.random.shuffle(training_vector)
        print("shuffle")

    for counter2 in range(0,500):
        a = w[(counter2) % 25] * training_vector[(counter2)%25,:6]
        a = a.sum()
        if(a > 0):
            y = 1;
        elif(a <= 0):
            y = -1;
        b = list(range(6))
        for i in range(0, 6):
            b[i] = (learning_rate / 2) * (training_vector[counter2%25,6]-y)
        w[(counter2+1)%25] = w[(counter2) % 25] + b * training_vector[(counter2 % 25),:6]

        if (training_vector[(counter2%25,6)] == y):
            true_n = true_n + 1
        else:
            false_n = false_n + 1
            true_n = 0

        if true_n > 25:
            break

    b = 0
    for counter3 in range(0, 15):
        control_variable = w[24,:5] * test_vector[counter3,:5]
        control_variable = control_variable.sum()
        if(control_variable > 0):
            s1.append(test_vector[counter3])
            y = 1
        elif(control_variable <= 0):
            s2.append(test_vector[counter3])
            y = -1
        if(y == test_vector[counter3,6]):
            true = true +1
        else:
            false = false +1

    error_rate += (false/(true+false))
    print("error rate %", error_rate*100)
    total_error += error_rate
    print("total steps", counter2)

    s1_np = np.array(s1)
    s2_np = np.array(s2)


print("******************************************************")
print("total error rate")
print("%", (total_error/60)*100)
