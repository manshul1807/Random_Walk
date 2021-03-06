# Project : Plot the random walk in 1D

# Steps
# 1. Find the Equation
# 2. Code the equation via function
# 3. Plot it

# Importing libraries
import matplotlib.pyplot as plt
import random

# Inputting initial values and error handling

while True:
    try:
        start = int(input('Enter the starting number: '))
        break
    except ValueError:
        print('Enter a valid integer')

while True:
    try:

        step = int(input('Enter the number of steps : '))
        break
    except ValueError:
        print('Enter a valid integer')

# create a list of all the points
l = [start]
for i in range(step):
    k = random.choice([-1, 1])
    start += k
    l.append(start)

# plot the walk
plt.plot(l)
plt.title('1 D Random Walk')
plt.show()
