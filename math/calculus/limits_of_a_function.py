# Finding the limit of 1/x in the infinity

from sympy import Limit, Symbol, S, sin
x = Symbol('x')
Limit(1/x, x, S.Infinity)

l = Limit(1/x, x, S.Infinity)
# Using Limit to solve, guess what? Limits!
print(l.doit())

print(Limit(1/x, x, 0, dir='-').doit())

print(Limit(sin(x)/x, x, 0).doit())