from math import factorial
from numpy import exp, linspace
import matplotlib.pyplot as plt

def f(x):
    """f(x) and its all its derivatives of higher order"""
    return exp(x)

def T(x, c, N):
    """Builds the T.s. approxim. for f(x) = exp(x) with N + 1 terms"""
    sum = 0
    for n in range(N+1):
        # Note that f(c)=f'(c)=f''(c)..., when f(x) = exp(x)
        sum += (f(c)/factorial(n))*(x-c)**n
    return sum

a = -3; b = 3; maxNoOfTerms = 4
c = input('Give the parameter c: ')
xPoints = linspace(a, b, 100)

for i in range(maxNoOfTerms):
    Tapprox = T(xPoints, c, i)
    plt.plot(xPoints, f(xPoints), 'r', xPoints, Tapprox, '--')
    plt.axis([-4.0, 4.0, -2, 15])
    plt.hold('on')
plt.hold('off')
plt.show()
