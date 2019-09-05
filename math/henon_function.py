'''
Draw a Henon Function
'''

import matplotlib.pyplot as plt

def transform(p):
    x, y = float(p[0]), float(p[1])
    new_x = y + 1 -1.4 * x*x
    new_y = 0.3 * x
    return new_x, new_y

def draw_henon(n):
    # We start with (0, 0)
    x = [0]
    y = [0]
    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x, y

if __name__ == '__main__':
    n = int(input('Enter the number of points in the Henon function: '))
    x, y = draw_henon(n)
    # Plot the points
    plt.plot(x, y, 'o')
    plt.title('Henon Function with {0} points'.format(n))
    plt.show()