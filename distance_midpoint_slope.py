import matplotlib.pyplot as plt

A = (1, 2)
B = (6, 5)

# Compute distance, midpoint, slope
dist = ((B[0]-A[0])**2 + (B[1]-A[1])**2)**0.5
mid = ((A[0]+B[0])/2, (A[1]+B[1])/2)
slope = (B[1]-A[1])/(B[0]-A[0])

print(f"Distance = {dist:.2f}, Midpoint = {mid}, Slope = {slope:.2f}")

# Plot
plt.plot([A[0], B[0]], [A[1], B[1]], 'bo-')
plt.text(*A, 'A')
plt.text(*B, 'B')
plt.scatter(*mid, color='red')
plt.grid(True)
plt.axis('equal')
plt.show()
