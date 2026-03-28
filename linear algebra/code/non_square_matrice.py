import numpy as np
import matplotlib.pyplot as plt


def main():
    i = -2
    j = 2

    v1 = np.array([i, j])


    transfo = ([
        [1, 1]
    ])

    n = 21
    x = np.linspace(-10, 10, n)
    y = np.linspace(-10, 10, n)
    X, Y = np.meshgrid(x, y)
    points = np.vstack([X.flatten(), Y.flatten()])

    points_transfo = transfo @ points    
    xFinal = points_transfo[0].reshape(n, n)
    yFinal = points_transfo[0].reshape(n, n)

    v10 = transfo @ v1
    vscale = v10.flatten()

    def graph():

        plt.figure(figsize=(8, 8))



        w = 0.01
        params = dict(angles='xy', scale_units='xy', width=w, scale=1)
        plt.quiver(0,0, vscale, vscale, color='red', zorder=5, **params)
        plt.quiver(0,0, i, i, color='green', zorder=7, **params)
        plt.quiver(0,0, j, j, zorder=6, color='grey', **params)

        for k in range(n):
            plt.plot(X[k, :], Y[k, :], color='grey', alpha=0.5, lw=1.5)
            plt.plot(X[:, k], Y[:, k], color='grey', alpha=0.5, lw=1.5)

        for k in range(n):
            plt.plot(xFinal[k, :], yFinal[k, :], color='blue', alpha=0.6, lw=1.5)
            plt.plot(xFinal[:, k], yFinal[:, k], color='blue', alpha=0.6, lw=1.5)



        plt.axhline(0, color='black', lw=2)
        plt.axvline(0, color='black', lw=2)
        n1 = n / 3
        plt.axis('equal')
        plt.xlim(-n1, n1)
        plt.ylim(-n1, n1)



        plt.gca().set_aspect('equal', adjustable='box')
        plt.draw()
        plt.show()
    
    graph()


main()



