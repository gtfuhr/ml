from sympy import FiniteSet, pi
def time_period(length):
    g = 9.8
    T = 2*pi*(length/g)**0.5
    return T
if __name__ == '__main__':
    L = FiniteSet(15, 18, 21, 22.5, 25)
    for l in L:
        t = time_period(l/100)
        print('Length: {0} cm Time Period: {1:.3f} s'. format(float(l), float(t)))