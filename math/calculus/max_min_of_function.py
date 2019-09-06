from sympy import Symbol, solve, Derivative
x = Symbol('x')
f = x**5 - 30*x**3 + 50*x
d1 = Derivative(f, x).doit()

critical_points = solve(d1)
print(critical_points)

A = critical_points[2]
B = critical_points[1]
C = critical_points[1]
D = critical_points[3]

'''
    Because all the critical points for this function lie within the considered
    interval, they are all relevant for our search for the global maximum and
    minimum of f(x). We may now apply the so-called second derivative test to
    narrow down which critical points could be global maxima or minima.
    First, we calculate the second-order derivative for the function f(x).
    Note that to do so, we enter 2 as the third argument:

    Excerpt from the book Doing Math with Python
'''

d2 = Derivative(f, x, 2).doit()


# The minimum of the following values will be the minima of the function
print(d2.subs({x:B}).evalf())
print(d2.subs({x:C}).evalf())
print(d2.subs({x:A}).evalf())
print(d2.subs({x:D}).evalf())


x_min = -5
x_max = 5
f.subs({x:A}).evalf()
f.subs({x:C}).evalf()
f.subs({x:x_min}).evalf()
f.subs({x:x_max}).evalf()