import numpy as np
import matplotlib.pyplot as plt

def parser(fonction):
  fonction = fonction.replace("[", "").replace("]", "").replace(",", "")
  x, y, z = fonction.split()
  fonction = np.array([int(x), int(y), int(z)])
  print(fonction)
  return fonction



entre1 = input("composantes du vecteur 1 : ")
v1 = parser(entre1)
entre2 = input("composantes du vecteur 2 : ")
v2 = parser(entre2)

coefficients = np.linspace(-10, 10, 20)
A, B = np.meshgrid(coefficients, coefficients)
X = A * v1[0] + B * v2[0]
Y = A * v1[1] + B * v2[1]
Z = A * v1[2] + B * v2[2]


fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

plan = ax.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis')

ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='red', label='v1', linewidth=3)
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='blue', label='v2', linewidth=3)


ax.set_xlabel('Axe X')
ax.set_ylabel('Axe Y')
ax.set_zlabel('Axe Z')
ax.set_title("Visualisation du Span de deux vecteurs")
ax.legend()


limit =   15
ax.set_xlim([-limit, limit])
ax.set_ylim([-limit, limit])
ax.set_zlim([-limit, limit])

plt.show()
