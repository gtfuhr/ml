import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

def initialize_image(x_p, y_p):
    image = []
    iteration = 0
    max_iteration = 100
    x = -2.5,1
    y = -1,1
    x_len = x[1] - x[0]
    y_len = y[1] - y[0]

    x_points = []
    ant = x[0]
    increment = x_len/x_p
    for i in range(x_p):
        x_points.append(ant)
        ant += increment

    y_points = []
    ant = y[0]
    increment = y_len/y_p
    for i in range(y_p):
        y_points.append(ant)
        ant += increment

    # plt.plot(x_points,y_points)
    # plt.show()
    # input()
    # all_points = x_points * y_points
    # print(len(all_points))
    
    # xi, yi = 0,0
    for i in range(y_p):
        image.append([])
        # TODO
            image[i].append(iteration)
    return image

def color_points():
    x_p = 40
    y_p = 40
    image = initialize_image(x_p, y_p)
    # for i in range(y_p):
    #     for j in range(x_p):
    #         image[i][j] = random.randint(0, 10)
    plt.imshow(image, origin='lower', extent=(0, 5, 0, 5),
            cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    color_points()