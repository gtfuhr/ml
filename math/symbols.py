from sympy import Symbol, factor, expand, pprint, solve

x = Symbol('x')
y = Symbol('y')

print(x)
expr = x ** 2 - y ** 2
print(expr)
print(factor(expr))
print()

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
print(factor(expr))
print(expand(expr))

print("Now the last two expressions with pretty printing enabled")
print(pprint(factor(expr)))
print(pprint(expand(expr)))


# solving equations with solve
print("Solving quadratic equations")
x = Symbol('x')
expr = x**2 + 5*x + 4
print(pprint(expr))
print(solve(expr, dict=True));

print("\nSolving quadratic equations with complex numbers")
x = Symbol('x')
expr = x**2 + x + 1
print(pprint(expr))
print(solve(expr, dict=True))

print("Solving for one variable in term of others")

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
expr = a*x*x + b*x + c
print("Solving the following expression in term of x")
print(pprint(expr))
print(solve(expr, x, dict=True))


print("Solving a system of linear equations:")
x = Symbol('x')
y = Symbol('y')
print("Solving the following system")
expr1 = 2*x + 3*y - 6
expr2 = 3*x + 2*y - 12
print(pprint(expr1))
print(pprint(expr2))


print("Simpler way of plotting different functions")
from sympy import plot
x = Symbol('x')
plot(2 * x**2 + 6)