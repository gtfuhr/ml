'''
Draw a sierpinski triangle
'''
import random
import matplotlib.pyplot as plt
def transformation_1(xn,yn):
    xn1 = 0.5*xn
    yn1 = 0.5*yn
    return xn1, yn1

def transformation_2(xn,yn):
    xn1 = 0.5*xn + 0.5
    yn1 = 0.5*yn + 0.5
    return xn1, yn1

def transformation_3(xn,yn):
    xn1 = 0.5*xn + 1
    yn1 = 0.5*yn
    return xn1, yn1

def get_index(probability):
    r = random.random()
    c_probability = 0
    sum_probability = []
    for p in probability:
        c_probability += p
        sum_probability.append(c_probability)
    for item, sp in enumerate(sum_probability):
        if r <= sp:
            return item
    return len(probability)-1

def transform(p):
    # List of transformation functions
    transformations = [transformation_1, transformation_2,
    transformation_3]
    
    probability = [1/3, 1/3, 1/3]
    # Pick a random transformation function and call it
    tindex = get_index(probability)
    
    t = transformations[tindex]
    x, y = t(p[0],p[1])
    return x, y

def draw_triangle(n):
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
    n = int(input('Enter the number of points in the Sierpinski Triangle: '))
    x, y = draw_triangle(n)
    # Plot the points
    plt.plot(x, y, 'o')
    plt.title('Sierpinski Triangle with {0} points'.format(n))
    plt.show()