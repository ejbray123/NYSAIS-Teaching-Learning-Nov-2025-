import matplotlib.pyplot as plt
import numpy as np

n = 7  # sides
angles = np.linspace(0, 2*np.pi, n+1)
x = np.cos(angles)
y = np.sin(angles)

plt.plot(x, y, 'o-', label=f'{n}-gon')
plt.axis('equal')
plt.legend()
plt.show()

print(f"Sum of interior angles = {(n-2)*180}°")
print(f"Each interior angle (regular) = {((n-2)*180)/n}°")
