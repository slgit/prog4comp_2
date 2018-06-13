def naive_Newton(f, dfdx, x, eps):
    while abs(f(x)) > eps:
        x = x - (f(x))/dfdx(x)
        print(x)
    return x

def f(x):
    return x**2 - 9

def dfdx(x):
    return 2*x

print(naive_Newton(f, dfdx, 1000, 0.001))

# Another example...
from math import tanh

def g(x):
    return tanh(x)

def dgdx(x):
    return 1 - tanh(x)**2

#print(naive_Newton(f, dfdx, 1.08, 0.001))
#print(naive_Newton(f, dfdx, 1.09, 0.001))  # change x_0 slightly
