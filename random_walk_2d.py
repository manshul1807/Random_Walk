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
        x_start = int(input('Enter the x starting dimension: '))
        break
    except ValueError:
        print('Enter a valid integer')

while True:
    try:
        y_start = int(input('Enter the y starting dimension: '))
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

x_list = [x_start]
y_list = [y_start]
for i in range(step):
    (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
    x_start += dx
    y_start += dy
    x_list.append(x_start)
    y_list.append(y_start)

# plot the walk
plt.plot(x_list, y_list)
plt.title('2 D Random Walk')
plt.show()
