import turtle

t = turtle.Turtle()

n = int(input("number of sides? "))

angle = 360 / n

for i in range(n):
    t.fd(100)
    t.left(angle)