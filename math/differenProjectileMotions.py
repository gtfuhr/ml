'''
Generate equally spaced floating point
values between two given values
'''
def frange(start,final,increment):

    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment

    return numbers

'''
Now we will draw the trajectory of the projectile motion
'''

from matplotlib import pyplot as plt
from math import radians, sin, cos

def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def draw_trajectory(u,theta):
    theta = radians(theta)
    g = 9.8

    # Time of the flight
    t_flight = 2 * u * sin(theta) / g

    # Find the time intervals
    intervals = frange(0, t_flight, 0.001)

    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*cos(theta)*t)
        y.append(u*sin(theta)*t - 0.5*g*t*t)
    draw_graph(x, y)

if __name__ == '__main__':
    for u in range(10,100,10):
        draw_trajectory(u, 45)
    plt.legend([str(u) for u in range(10,100,10)])
    plt.show()