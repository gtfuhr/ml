from sympy import Limit, Symbol, S
n = Symbol('n')
print(Limit((1+1/n)**n, n, S.Infinity).doit())



p = Symbol('p', positive=True)
r = Symbol('r', positive=True)
t = Symbol('t', positive=True)
# Finding the expression for A
Limit(p*(1+r/n)**(n*t), n, S.Infinity).doit()