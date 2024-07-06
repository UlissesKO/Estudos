import numpy as np
import matplotlib.pyplot as plt

X_0 = np.array([[0], [0]])
deltax = np.random.normal(0, 1, (2, 100))
X = np.concatenate((X_0,np.cumsum(deltax, axis=1)), axis=1)
#a soma vai ser assim:
#[1, 2, 4, 6, 10]
#[1, 3, 7, 13, 23] vai sempre somar o de baixo com o proximo da sequencia de cima
plt.plot(X[0], X[1], "go-")
plt.show()
