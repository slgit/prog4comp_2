def y(v0, t):
    g = 9.81                  # Acceleration of gravity
    return v0*t - 0.5*g*t**2

v0 = 5                   # Initial velocity

time = 0.6               # Just pick one point in time
print(y(v0, time))
time = 0.9               # Pick another point in time
print(y(v0, time))
