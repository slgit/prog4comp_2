def naive_Newton(f, dfdx, x, eps):
    while abs(f(x)) > eps:
        x = x - float(f(x))/dfdx(x)
        print(x)
    return x

def app_sqrt():
    def f(x):
        return x**2 - 9    
    def dfdx(x):
        return 2*x    
    print(naive_Newton(f, dfdx, 1000, 0.001))

if __name__ == '__main__':
    app_sqrt()

