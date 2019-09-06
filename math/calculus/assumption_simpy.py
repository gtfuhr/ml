from sympy import Symbol, sin
x = Symbol('x', positive=True)
if (x+5) > 0:
    print('Looks like x+5 is greater than 0')
else:
    print('Looks like x+5 is not greater than 0')
