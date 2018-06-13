import random
import numpy as np
import matplotlib.pyplot as plt

N = 1000                   # number of steps
d = 1                      # step length (e.g., in meter)
x = np.zeros(N+1)          # x coordinates 
y = np.zeros(N+1)          # y coordinates
x[0] = 0;  y[0] = 0        # set initial position

for i in range(0, N, 1):
    r = random.random()         # random number in [0,1)
    if 0 <= r < 0.25:           # move north
        y[i+1] = y[i] + d
        x[i+1] = x[i]
    elif 0.25 <= r < 0.5:       # move east
        x[i+1] = x[i] + d
        y[i+1] = y[i]
    elif 0.5 <= r < 0.75:       # move south
        y[i+1] = y[i] - d
        x[i+1] = x[i]
    else:                       # move west
        x[i+1] = x[i] - d
        y[i+1] = y[i]

# plot path (mark start and stop with blue o and *, respectively)
plt.plot(x, y, 'r--', x[0], y[0], 'bo', x[-1], y[-1], 'b*')
plt.xlabel('x');  plt.ylabel('y')
plt.show()
