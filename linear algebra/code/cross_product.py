import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


def main():

    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    crsprd = np.cross(v1, v2)
    a, b, c = crsprd
    limit = max(np.linalg.norm(v1), np.linalg.norm(v2), np.linalg.norm(crsprd))

    range_x = np.linspace(-limit, limit, 10)
    range_y = np.linspace(-limit, limit, 10)

    X, Y = np.meshgrid(range_x, range_y)
    Z = -(a * X + b * Y) / c


    def graph():
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.quiver(0,0,0, v1[0], v1[1], v1[2], color='red')
        ax.quiver(0,0,0, v2[0], v2[1], v2[2], color='blue')
        ax.quiver(0, 0, 0, crsprd[0], crsprd[1], crsprd[2], color='green')
        ax.plot_surface(X, Y, Z, color='grey', alpha=0.3, rstride=1, cstride=1)

        print(limit)
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_zlim(-limit, limit)

        ax.set_box_aspect([1,1,1]) 
        plt.show()
    graph()




main()
