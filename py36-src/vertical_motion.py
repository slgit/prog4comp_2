"""
Module for computing vertical motion
characteristics for a projectile.
"""
def y(v0, t):
    """
    Compute vertical position at time t, given the initial vertical
    velocity v0. Assume negligible air resistance.
    """
    g = 9.81
    return v0*t - 0.5*g*t**2

def time_of_flight(v0):
    """
    Compute time in the air, given the initial vertical
    velocity v0. Assume negligible air resistance.
    """
    g = 9.81
    return 2*v0/g

def max_height(v0):
    """
    Compute maximum height reached, given the initial vertical
    velocity v0. Assume negligible air resistance.
    """
    g = 9.81
    return v0**2/(2*g)

def application():
    import numpy as np
    import matplotlib.pyplot as plt
    import sys
    
    print("""This program computes vertical motion characteristics for a
    projectile. Given the intial vertical velocity, it computes height
    (as it develops with time), maximum height reached, as well as time
    of flight.""")
    
    try:
        v_initial = float(input('Give the initial velocity: '))
    except:
        print('You must give a valid number!')
        sys.exit(1)
    
    H = max_height(v_initial)
    T = time_of_flight(v_initial)
    print('Maximum height: {:g} m, \nTime of flight: {:g} s'.format(H, T))
    
    # compute and plot position as function of time
    dt = 0.001
    # just pick a "small" time step
    N = int(T/dt)
    # number of time steps
    t = np.linspace(0, N*dt, N+1)
    position = y(v_initial, t)
    # compute all positions (over T)
    plt.plot(t, position, 'b--')
    plt.xlabel('Time (s)')
    plt.ylabel('Vertical position (m)')
    plt.show()
    return

if __name__ == '__main__':
    application()