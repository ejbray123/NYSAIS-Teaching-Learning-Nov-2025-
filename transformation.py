import matplotlib.pyplot as plt
import numpy as np

# Original triangle
triangle = np.array([[0,0], [4,0], [2,3], [0,0]])

# Rotation matrix (about origin)
theta = np.radians(45)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
rotated = triangle.dot(R)

# Plot
plt.plot(triangle[:,0], triangle[:,1], 'b-', label='Original')
plt.plot(rotated[:,0], rotated[:,1], 'r--', label='Rotated 45°')
plt.axis('equal')
plt.legend()
plt.show()
