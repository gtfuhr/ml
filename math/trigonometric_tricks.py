from sympy import Symbol, sin
theta = Symbol('theta')

sin(theta) + sin(theta)

from sympy import solve

u = Symbol('u')
t = Symbol('t')
g = Symbol('g')
theta = Symbol('theta')
print(solve(u*sin(theta)-g*t, t))

# The expression for t , as we learned earlier, turns out to be u*sin(theta)/g ,
# and it illustrates how the solve() function can be used to find solutions to
# equations containing mathematical functions as well.

# Excerpt got from the book Doing Math with Python

