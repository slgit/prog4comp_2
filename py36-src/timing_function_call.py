import timeit
import numpy as np

def add(a, b):
    return a + b

x = np.zeros(1000)
y = np.zeros(1000)

# ...use the function add
t = timeit.Timer('for i in range(len(x)): x[i] = add(i, i+1)', \
                 setup='from __main__ import add, x')
x_time = t.timeit(10000)     # Time 10000 runs of the whole loop
print('Time, function call: {:g} seconds'.format(x_time))

# ...no use of function add
t = timeit.Timer('for i in range(len(y)): y[i] = i + (i+1)', \
                 setup='from __main__ import y')
y_time = t.timeit(10000)     # Time 10000 runs of the whole loop
print('Time: {:g} seconds'.format(y_time))
