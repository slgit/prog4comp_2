import numpy as np
import matplotlib.pyplot as plt

a = 0.0;  b = 3.0                     # time interval
N = 30                                # number of time steps
dt = (b - a)/N                        # time step (s)
V = np.zeros(N+1)                     # numerically computed volume (L)
V[0] = 1                              # inital volume

for i in range(0, N, 1):
    V[i+1] = V[i] + dt*V[i]           # ...r is V now

time_exact = np.linspace(a, b, 1000)  
V_exact = np.exp(time_exact)          # make exact solution (for plotting)
time = np.linspace(0, 3, N+1)
plt.plot(time, V, 'bo-', time_exact, V_exact, 'r')
plt.title('Case 2')
plt.legend(['numerical','exact'], loc='upper left')
plt.xlabel('t (s)')
plt.ylabel('V (L)')
plt.show()