import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(36):
    t.color(colors[i % 6])
    for j in range(5):
        t.forward(100)
        t.right(144)
    t.right(10)

turtle.done()