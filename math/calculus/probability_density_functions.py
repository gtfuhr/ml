from sympy import Symbol, exp, sqrt, pi, Integral

# Which is the probability of x grade staying between 11 and 12
# In a normal distribution of grades

x = Symbol('x')
p = exp(-(x - 10)**2/2)/sqrt(2*pi)
print(Integral(p, (x, 11, 12)).doit().evalf())