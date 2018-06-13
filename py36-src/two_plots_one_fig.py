import numpy as np
import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)          # 2 rows, 1 column, plot number 1
v0 = 5
g = 9.81
t = np.linspace(0, 1, 11)
y = v0*t - 0.5*g*t**2
plt.plot(t, y, '*')
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.title('Ball moving vertically')

plt.subplot(2, 1, 2)          # 2 rows, 1 column, plot number 2
t = np.linspace(-2, 2, 100)   
f_values = t**2
g_values = np.exp(t)
plt.plot(t, f_values, 'r', t, g_values, 'b--')
plt.xlabel('t')
plt.ylabel('f and g')
plt.legend(['t**2', 'e**t'])
plt.title('Plotting of two functions (t**2 and e**t)')
plt.grid('on')
plt.axis([-3, 3, -1, 10])

plt.tight_layout()           # make subplots fit figure area
plt.show()
