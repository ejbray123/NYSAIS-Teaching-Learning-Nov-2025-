import turtle

radius = 100

leo = turtle.Turtle()
leo.speed(0)

for i in range(6):
    for j in range(2):
        leo.circle(radius, 60)
        leo.left(120)
    leo.left(60)

leo.circle(radius, 60)
leo.left(60)
leo.circle(radius)

