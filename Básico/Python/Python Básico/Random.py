import random
import matplotlib.pyplot as plt
import numpy as np
import time

#rand = []

#for a in range(1000000):
#    rand.append(random.choice(range(1,7)))

#plt.hist(rand, bins= np.linspace(0.5, 6.5, 7))
#plt.show()
tempocomeco = time.time()
rand2 = []
for rep in (range(1000000)):
    rand1 = []
    for b in range(10):
        x = random.choice(range(1, 7))
        rand1.append(x)
        y = sum(rand1)
    rand2.append(y)

plt.hist(rand2, bins=np.linspace(10, 60))
plt.show()

tempofinal = time.time()
print(tempofinal - tempocomeco)