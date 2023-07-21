from pisigma import pisigma
import numpy as np
import matplotlib.pyplot as plt

# identity function
I = lambda x: x

x_values = np.linspace(1, np.inf)
y_values = [pisigma(n, 1, I) for n in x_values]

plt.plot(x_values, y_values)
plt.xlabel('n')
plt.ylabel('pi/sigma')
plt.show()

