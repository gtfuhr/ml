from sympy import Integral, Symbol, Derivative

x = Symbol('x')
k = Symbol('k')
print("Funcao original:")
print("k*x")
print("Integral da função:")
print(Integral(k*x, x).doit())
print("Derivada da integral da função:")
print(str(Derivative(Integral(k*x, x).doit(),[x,k]).doit()))

