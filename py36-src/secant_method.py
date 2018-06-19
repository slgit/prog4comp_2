import sys

def secant(f, x0, x1, eps):
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0
    while abs(f_x1) > eps and iteration_counter < 100:
        try:
            denominator = (f_x1 - f_x0)/(x1 - x0)
            x = x1 - f_x1/denominator
        except ZeroDivisionError:
            print('Error! - denominator zero for x = ', x)
            sys.exit(1)     # Abort with error
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter = iteration_counter + 1
    # Here, either a solution is found, or too many iterations
    if abs(f_x1) > eps:
        iteration_counter = -1
    return x, iteration_counter

if __name__ == '__main__':
    def f(x):
        return x**2 - 9
    
    x0 = 1000;   x1 = x0 - 1
    
    solution, no_iterations = secant(f, x0, x1, eps=1.0e-6)
    
    if no_iterations > 0:    # Solution found
        print('Number of function calls: {:d}'.format(2+no_iterations))
        print('A solution is: {:f}'.format(solution))
    else:
        print('Solution not found!')
