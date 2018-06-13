def xy(v0x=2.0, v0y=5.0, t=0.6):
    """Computes horizontal and vertical positions at time t"""
    g = 9.81                              # acceleration of gravity
    return v0x*t, v0y*t - 0.5*g*t**2

x, y = xy()
print('Horizontal position: {:g} , Vertical position: {:g}'.format(x, y))

