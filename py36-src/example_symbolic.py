import sympy as sym

x, y = sym.symbols('x y')

print(2*x + 3*x - y)                      # Algebraic computation
print(sym.diff(x**2, x))                  # Differentiates x**2 wrt. x
print(sym.integrate(sym.cos(x), x))       # Integrates cos(x) wrt. x
print(sym.simplify((x**2 + x**3)/x**2))   # Simplifies expression
print(sym.limit(sym.sin(x)/x, x, 0))      # lim of sin(x)/x as x->0
print(sym.solve(5*x - 15, x))             # Solves 5*x = 15
