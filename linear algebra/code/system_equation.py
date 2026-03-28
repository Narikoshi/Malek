import numpy as np
import matplotlib.pyplot as plt


def main():
    def parser(var):
        var = var.replace("x","").replace("y","").replace("z","").replace("+","").replace("=","")
        x, y, z = var.split()   
        ligne = np.array([float(x), float(y)])

        print(x, y, z)
        return ligne, float(z)

    
    équa1 = input("entrez la première équation : ")
    équa2 = input("entrez la deuxième équation : ")
    ligne1, z1 = parser(équa1)
    ligne2, z2 = parser(équa2)

    matrice = np.array([
        ligne1,
        ligne2
    ])
    
    
    matrice_inv = np.linalg.inv(matrice)

    vecteurf = np.array([z1, z2])

    résolution = matrice_inv @ vecteurf

    n = 21
    x = np.linspace(-10, 10, n)
    y = np.linspace(-10, 10, n)
    X, Y = np.meshgrid(x, y)
        
    points = np.vstack([X.flatten(), Y.flatten()])
    points_transfo = matrice_inv @ points
    
    xFinal = points_transfo[0].reshape(n, n)
    yFinal = points_transfo[1].reshape(n, n)
    vecteurf_trans = matrice_inv @ vecteurf
    
    
    det = np.linalg.det(matrice)

    if det == 0 :
        print("pas de solution unique")
        return
    else:
        print("")


    print(matrice)
    print(vecteurf)
    print(résolution)

    def graph():
        plt.figure(figsize=(8,8))
        w = 0.005
        params = dict(angles='xy', scale_units='xy', width=w, scale=1)
        plt.quiver(0,0, vecteurf[0], vecteurf[1], color='green', **params)      
        plt.quiver(0,0, vecteurf_trans[0], vecteurf_trans[1], color='red', **params)
        

        for i in range(n):
            plt.plot(X[i, :], Y[i, :], color='grey', alpha=0.5, lw=1.5)
            plt.plot(X[:, i], Y[:, i], color='grey', alpha=0.5, lw=1.5)

        for i in range(n):
            plt.plot(xFinal[i, :], yFinal[i, :], color='blue', alpha=0.6, lw=1.5)
            plt.plot(xFinal[:, i], yFinal[:, i], color='blue', alpha=0.6, lw=1.5)


        limit =  max(np.linalg.norm(vecteurf), np.linalg.norm(vecteurf_trans))
        epsilon = 9e-11
        plt.xlim(-limit - epsilon, limit + epsilon)
        plt.ylim(-limit - epsilon, limit + epsilon)
        plt.axhline(0, color='black', lw=2)
        plt.axvline(0, color='black', lw=2)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()





    graph()

main()


