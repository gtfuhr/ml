from sympy import Derivative, Symbol

x = Symbol('x')
f = (x**3 + x**2 + x)*(x**2+x)
print("First Example")
print("Derivative of {0}".format(str(f)))
print("Derivative:")
print(Derivative(f, x).doit())

print("Use the following derivative calculator:")

'''
Derivative calculator
'''
from sympy import sympify, pprint
from sympy.core.sympify import SympifyError

def derivative(f, var):
    var = Symbol(var)
    d = Derivative(f, var).doit()
    pprint(d)

if __name__=='__main__':
    f = input('Enter a function: ')
    var = input('Enter the variable to differentiate with respect to: ')
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid input')
    else:
        derivative(f, var)