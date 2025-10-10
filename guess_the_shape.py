import turtle

t = turtle.Turtle()
t.speed(0)

# Not a regular pattern — irregular angles & sides
sides = [109, 96, 103, 131, 85]
angles = [52, 94, 59, 89, 65]

for i in range(5):
    t.forward(sides[i])
    t.left(angles[i])

turtle.done()
