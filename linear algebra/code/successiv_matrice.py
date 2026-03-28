import numpy as np
import matplotlib.pyplot as plt


v1 = np.array([4, 6])
n = 21
v1_base = np.array([1, 0])
v2_base = np.array([0, 1])

transformation = np.array([
    [1, 0.4],
    [0.2, 0.5]
])

transformation2 = np.array([
    [1, 0],
    [1, 2]
])

transformation3 = transformation @ transformation2

transformation4 = transformation2 @ transformation

x = np.linspace(-10, 10, n)
y = np.linspace(-10, 10, n)
X, Y = np.meshgrid(x, y)

points1 = np.vstack([X.flatten(), Y.flatten()])



fig, axs = plt.subplots(2, 2, figsize=(10, 10))


w = 0.01
params = dict(angles='xy', scale_units='xy', width=w, scale=1)

for ax in axs.flat:
    for i in range(n):
        ax.plot(X[i, :], Y[i, :], color='grey', alpha=0.5, lw=1.5)
        ax.plot(X[:, i], Y[:, i], color='grey', alpha=0.5, lw=1.5)
    ax.axhline(0, color='black', lw=2)
    ax.axvline(0, color='black', lw=2)
    ax.quiver(0, 0, v1_base[0], v1_base[1], color='red', **params)
    ax.quiver(0, 0, v2_base[0], v2_base[1], color='red', **params)
    n1 = n / 15
    ax.set_xlim(-n1, n1)
    ax.set_ylim(-n1, n1)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, alpha=0.3)


def graph(transfo, axs):
    points1_transfo = transfo @ points1
    xFinal = points1_transfo[0].reshape(n, n)
    yFinal = points1_transfo[1].reshape(n, n)   
    v1_trans = transfo @ v1_base
    v2_trans = transfo @ v2_base

    for i in range(n):
            axs.plot(xFinal[i, :], yFinal[i, :], color='blue', alpha=0.6, lw=1.5)
            axs.plot(xFinal[:, i], yFinal[:, i], color='blue', alpha=0.6, lw=1.5)    

    axs.quiver(0, 0, v1_trans[0], v1_trans[1], color='green', **params)
    axs.quiver(0, 0, v2_trans[0], v2_trans[1], color='green', **params)


graph(transformation, axs[0,0])
graph(transformation2, axs[0,1])
graph(transformation3, axs[1,0])
graph(transformation4, axs[1,1])

plt.draw()
plt.show()
