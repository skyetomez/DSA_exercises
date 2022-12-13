import numpy as np

import matplotlib.pyplot as plt


t = np.linspace(1, 10, 100)

y1 = 8 * t
y2 = 4 * t * np.log10(t)
y3 = 2 * t * t
y4 = t * t * t
y5 = np.power(2, t)
plt.loglog(t, y1, label="8t")
plt.loglog(t, y2, label="4tlogt")
plt.loglog(t, y3, label="2t^2")
plt.loglog(t, y4, label="t^3")
plt.loglog(t, y5, label="2^t")
plt.title("log-log plot of R-3.1 functions.")
plt.legend()
plt.grid()
plt.show()
