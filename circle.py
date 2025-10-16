import matplotlib.pyplot as plt
import numpy as np

circle = plt.Circle((0,0), 5, fill=False)
fig, ax = plt.subplots()
ax.add_artist(circle)

# Tangent line at (5,0)
x = np.linspace(-6, 6, 100)
y = [0]*len(x)
plt.plot(x, y, 'r--')
plt.plot(5, 0, 'bo')

plt.axis('equal')
plt.grid(True)
plt.show()
