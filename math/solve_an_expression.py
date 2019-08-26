from sympy import sympify, solve, Symbol
expr = input("Enter an expression to solve it:\n")
expr  = sympify(expr)
y = Symbol('y')

print(solve(expr,y))
