import numpy as np 
import matplotlib.pyplot as plt


def main():

    vecteur1 = np.array([1, 3])
    vecteur2 = np.array([2, 3])

    def norme_2D(vect):
        norme = (vect[0] ** 2 + vect[1] ** 2) ** (1/2)
        return norme

    nrm_v1 = norme_2D(vecteur1)
    nrm_v2 = norme_2D(vecteur2)
    normes = [nrm_v1, nrm_v2]

    def produit_scalaire(vect1, vect2, nrm):
        prod_final = vect1 @ vect2 
        ombre_long = prod_final / nrm
        if nrm == nrm_v1:
            direction = vect1 / nrm
        else :
            direction = vect2 / nrm

        print(ombre_long)
        ombre = direction * ombre_long
        return prod_final, ombre

    rtr_prd_scl1 = produit_scalaire(vecteur1, vecteur2, nrm_v1)
    ombre1 = rtr_prd_scl1[1]
    rtr_prd_scl2 = produit_scalaire(vecteur1, vecteur2, nrm_v2)
    ombre2 = rtr_prd_scl2[1]

    
    n = 21
    x = np.linspace(-10, 10, n)
    y = np.linspace(-10, 10, n)
    X, Y = np.meshgrid(x, y)

    points1 = np.vstack([X.flatten(), Y.flatten()])

    def graph():

        plt.figure(figsize=(8, 8))
        w = 0.01
        params = dict(angles='xy', scale_units='xy', width=w, scale=1)
        plt.quiver(0, 0, vecteur1[0], vecteur1[1], color='blue', **params)
        plt.quiver(0, 0, vecteur2[0], vecteur2[1], color='red', **params)
        w2 = 0.005
        params2 = dict(angles='xy', scale_units='xy', width=w2, scale=1)
        plt.quiver(0, 0, ombre1[0], ombre1[1], color='red', **params2)
        plt.quiver(0, 0, ombre2[0], ombre2[1], color='blue', **params2)

        plt.scatter(0, 0, color='black', s=100, zorder=5, label='Origine')
        
        plt.plot([vecteur2[0], ombre1[0]], [vecteur2[1], ombre1[1]], color='red', linestyle='--', alpha=0.5)
        plt.plot([vecteur1[0], ombre2[0]], [vecteur1[1], ombre2[1]], color='blue', linestyle='--', alpha=0.5)


        plt.title(f"Produit scalaire = {rtr_prd_scl1[0]:.2f}")
        

    
        for i in range (n):
            plt.plot(X[i, :], Y[i, :], color='grey', alpha=0.5, lw=1.5)
            plt.plot(X[:, i], Y[:, i], color='grey', alpha=0.5, lw=1.5)

        limit = max(normes) + 3
        plt.xlim(-limit, limit)
        plt.ylim(-limit, limit)

        plt.show()

    graph()

main()



