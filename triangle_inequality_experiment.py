import random

def check_triangle_inequality():
    a, b, c = sorted([random.randint(1,20) for _ in range(3)])
    return a + b > c

results = sum(check_triangle_inequality() for _ in range(10000))
print(f"Valid triangles in 10,000 trials: {results}")
