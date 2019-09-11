# Finding the limit of 1/x in the infinity

from sympy import Limit, Symbol, S, sin
x = Symbol('x')
Limit(1/x, x, S.Infinity)

l = Limit(1/x, x, S.Infinity)

var = input("For what variable do you want to solve the limit? (maybe x..)\n")

tendence = input("X tends for what? For infinity type infinity, for minus infinity type -infinity\n")

if(tendence == "infinity"):
    tendence = S.Infinity

elif(tendence == "-infinity"):
    tendence = S.Infinity*-1

# Using Limit to solve, guess what? Limits!
limit_equation = input("Insert the equation that you want to calculate:\n")

lim = Limit(limit_equation, var, tendence)

print(lim.doit(hints=True))
