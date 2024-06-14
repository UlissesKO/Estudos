import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=10)
plt.hist(x, bins=np.linspace(-5, 5, 21))

x1 = np.random.gamma(2,3,1000)
plt.hist(x1, bins=30, cumulative=True, histtype="step")

x2 = np.linspace(-5,5,201)
plt.hist(x2)
plt.show()
