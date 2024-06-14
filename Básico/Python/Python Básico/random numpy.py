import time

import numpy as np
import matplotlib.pyplot as plt

a = '----------------------------------'
print(np.random.random(5))
print(a)

print(np.random.normal(0, 1, (2, 3)))
print(a)

x = np.random.randint(1, 7, (10, 3))
print(x)
print(a)

print(np.sum(x, axis=0))   #se for 0 soma na vertical e se for 1 soma na horizontal
print(a)

y = np.sum(x, axis=1)
print(y)
print(a)
print(np.mean(np.random.normal(1,2,3)))
print(a)

comecotempo = time.time()
X = np.random.randint(1, 7, (1000000, 100))
Y = np.sum(X, axis=1)
plt.hist(Y)
plt.show()
finaltempo = time.time()
print(finaltempo - comecotempo)

print(np.random.random((5,2,3)))
