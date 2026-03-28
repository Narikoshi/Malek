import numpy as np
import matplotlib.pyplot as plt



def main():
    v1= np.array([1, 0])
    v2 = np.array([0, 1])
    

    i1 = 1
    i2 = 0
    j1 = 0
    j2 = 1

    transfo = np.array([
        [i1, j1],
        [i2, j2]
    ])

    det = i1*j2 - j1*i2
    print(det)
    
    n = 21
    x = np.linspace(-10, 10, n)
    y = np.linspace(-10, 10, n)
    X, Y = np.meshgrid(x, y)
    
    points = np.vstack([X.flatten(), Y.flatten()])

    points_transfo = transfo @ points
    
    xFinal = points_transfo[0].reshape(n, n)
    yFinal = points_transfo[1].reshape(n, n)
    v1_trans = transfo @ v1
    v2_trans = transfo @ v2


    def graph():
        plt.figure(figsize=(8,8))
        w = 0.005
        params = dict(angles='xy', scale_units='xy', width=w, scale=1)

        plt.quiver(0, 0, v1[0], v1[1], color='red', **params)
        plt.quiver(0, 0, v2[0], v2[1], color='red', **params)

        plt.quiver(0, 0, v1_trans[0], v1_trans[1], color='green', **params)
        plt.quiver(0, 0, v2_trans[0], v2_trans[1], color='green', **params)

        for i in range(n):
            plt.plot(X[i, :], Y[i, :], color='grey', alpha=0.5, lw=1.5)
            plt.plot(X[:, i], Y[:, i], color='grey', alpha=0.5, lw=1.5)

        for i in range(n):
            plt.plot(xFinal[i, :], yFinal[i, :], color='blue', alpha=0.6, lw=1.5)
            plt.plot(xFinal[:, i], yFinal[:, i], color='blue', alpha=0.6, lw=1.5)

        def aff_Det():
            sommet = ([
                [0, 1, 1, 0], 
                [0, 0, 1, 1]
            ])

            coins_transformes = transfo @ sommet

            xf = coins_transformes[0]
            yf = coins_transformes[1]

            plt.fill(xf, yf, color='green', alpha=0.3)

            centre_x = np.mean(xf)
            centre_y = np.mean(yf)
            
            plt.text(centre_x, centre_y, f"det={det:.2f}", 
                    fontsize=10, fontweight='bold', ha='center', va='center',
                    bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

        aff_Det()



        plt.axhline(0, color='black', lw=2)
        plt.axvline(0, color='black', lw=2)
        limit = n / 2
        plt.xlim(-limit, limit)
        plt.ylim(-limit, limit)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
        

        
    graph()


main()
