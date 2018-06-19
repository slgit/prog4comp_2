import sys

def bisection(f, x_L, x_R, eps):
    f_L = f(x_L)
    if f_L*f(x_R) > 0:
        print("""Error! Function does not have opposite 
                 signs at interval endpoints!""")
        sys.exit(1)
    x_M = (x_L + x_R)/2.0
    f_M = f(x_M)
    iteration_counter = 1

    while abs(f_M) > eps:
        if f_L*f_M > 0:   # i.e. same sign
            x_L = x_M
            f_L = f_M
        else:
            x_R = x_M
        x_M = (x_L + x_R)/2
        f_M = f(x_M)
        iteration_counter = iteration_counter + 1
    return x_M, iteration_counter

if __name__ == '__main__':
    def f(x):
        return x**2 - 9
    
    a = 0;   b = 1000
    
    solution, no_iterations = bisection(f, a, b, eps=1.0e-6)
    
    print('Number of function calls: {:d}'.format(1 + 2*no_iterations))
    print('A solution is: {:f}'.format(solution))
