'''
Plot the graph of an input expression
'''
from sympy import sympify, solve, Symbol
from sympy.plotting import plot
def plot_expression(expr):
    y = Symbol('y')
    solutions = solve(expr, y)
    expr_y = solutions[0]
    plot(expr_y)
if __name__=='__main__':
    expr = input("Enter your expression in terms of x and y: ")
    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        plot_expression(expr)