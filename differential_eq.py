# Importing libraries
import matplotlib.pyplot as plt
import random


def recursion(x0, dict):
    global n
    l = 1.50
    x1 = x0*l*(1-x0)
    if n <= 50:
        #print(f'n is {n} and x1 is {x1}')
        dict[n] = x1
        n += 1
        return recursion(x1, dict)
    else:
        return


def check(x0):
    global n
    dict = {}
    recursion(x0, dict)
    return dict


x0 = 0.5
global n
n = 1
x = check(x0)
print(x)

lists = sorted(x.items())

print(lists)

alpha, beta = zip(*lists)

plt.plot(alpha, beta)

plt.show()
