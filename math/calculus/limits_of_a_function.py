# Finding the limit of 1/x in the infinity

from sympy import Limit, Symbol, S, sin
x = Symbol('x')
Limit(1/x, x, S.Infinity)

l = Limit(1/x, x, S.Infinity)
# Using Limit to solve, guess what? Limits!
# print(l.doit())

# print(Limit(1/x, x, 0, dir='-').doit())

# print(Limit(sin(x)/x, x, 0).doit())
lim = Limit((x**3 + 3*x**2 -x -3)/(x**3 + -x**2 +2), x, -1)
# print(help(lim))
print(lim.doit(hints=True))
