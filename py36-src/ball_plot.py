import numpy as np
import matplotlib.pyplot as plt

v0 = 5
g = 9.81
t = np.linspace(0, 1, 1001)

y = v0*t - 0.5*g*t**2

plt.plot(t, y)         # plots all y coordinates vs. all t coordinates
plt.xlabel('t (s)')    # places the text t (s) on x-axis
plt.ylabel('y (m)')    # places the text y (m) on y-axis
plt.show()             # displays the figure
