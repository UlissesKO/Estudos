import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(0, 1, 40)
y = x**2
y2 = x **1.5

plt.loglog(y, y2, "rd-", label="First") #pediu pra usar azul(b) circulos(o) e linha(-)
plt.loglog(x, y, "bo-", label="Second") #pediu pra usar azul(b) circulos(o) e linha(-)
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5, 10.5, -5, 110]) #xmin, xmax, ymin, ymax
plt.legend(loc="upper left")
plt.savefig("myplto.pdf")
