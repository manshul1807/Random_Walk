# Project : Plot the random walk in 1D

# Steps
# 1. Find the Equation
# 2. Code the equation via function
# 3. Plot it in commandline
# 4. Plot it in GUI

# 1. The Quation of Simple Random 1 D Walk >> S0 = 0 and SN = sum(1,n) of Z

import matplotlib.pyplot as plt
import random

start = int(input('Enter the starting number: '))
step = int(input('Enter the number of steps : '))
l = [start]
for i in range(step):
    k = random.choice([-1, 1])
    start += k
    l.append(start)

plt.plot(l)
plt.show()
