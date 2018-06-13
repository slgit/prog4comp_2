"""As the basic SIR1.py, but including loss of immunity."""

import numpy as np
import matplotlib.pyplot as plt

# Time unit: 1 h
#beta = 10./(40*8*24)
#beta = 0.00033            # ca. beta/4, i.e. reduced compared to SIR1.py
beta = 0.00043
gamma = 3./(15*24)
dt = 0.1             # 6 min
D = 300              # Simulate for D days
N_t = int(D*24/dt)   # Corresponding no of hours
#nu = 1./(24*50)      # Average loss of immunity: 50 days
nu = 1./(24*90)      # Average loss of immunity: 90 days

t = np.linspace(0, N_t*dt, N_t+1)
S = np.zeros(N_t+1)
I = np.zeros(N_t+1)
R = np.zeros(N_t+1)

# Initial condition
S[0] = 50
I[0] = 1
R[0] = 0

# Step equations forward in time
for n in range(N_t):
    S[n+1] = S[n] - dt*beta*S[n]*I[n] + dt*nu*R[n]
    I[n+1] = I[n] + dt*beta*S[n]*I[n] - dt*gamma*I[n]
    R[n+1] = R[n] + dt*gamma*I[n] - dt*nu*R[n]

fig = plt.figure()
l1, l2, l3 = plt.plot(t, S, t, I, t, R)
fig.legend((l1, l2, l3), ('S', 'I', 'R'), 'upper right')
plt.xlabel('hours')
plt.savefig('tmp.pdf'); plt.savefig('tmp.png')
plt.show()