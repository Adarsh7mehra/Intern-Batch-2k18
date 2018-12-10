import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,3*np.pi,33)

sin = np.sin(x)
cos = np.cos(x)


plt.plot(x,sin,'bo:',linewidth=3)
plt.plot(x,cos,'gs-.',linewidth=2)


plt.show()
