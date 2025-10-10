import math

num_sides = 6
side_length = 100

perimeter = num_sides * side_length

area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))

print("Perimeter", perimeter)
print("Area", round(area, 2))