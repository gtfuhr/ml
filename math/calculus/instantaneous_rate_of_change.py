from sympy import Symbol, Limit
t = Symbol('t')
St = 5*t**2 + 2*t + 8
t1 = Symbol('t1')
delta_t = Symbol('delta_t')
St1 = St.subs({t: t1})
St1_delta = St.subs({t: t1 + delta_t})
print(St1_delta)