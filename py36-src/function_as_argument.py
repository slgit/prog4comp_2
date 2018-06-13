def f(x):
    return x

def g(x):
    return x**2

def sum_function_values(f, start, stop):
    """Sum up function values for integer arguments as 
    f(start) + f(start+1) + f(start+2) + ... + f(stop)"""
    S = 0
    for i in range(start, stop+1, 1):
        S = S + f(i)
    return S

print('Sum with f becomes {:g}'.format(sum_function_values(f, 1, 3)))
print('Sum with g becomes {:g}'.format(sum_function_values(g, 1, 3)))

