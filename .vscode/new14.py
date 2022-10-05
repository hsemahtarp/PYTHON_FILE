import turtle

turtle.screensize(canvwidth = 500, canvheight = 500, bg = "Yellow")
tr = turtle.Turtle()
tr.pensize(5)

for a in range(5):
    tr.color("light Green")
    tr.right(144)
    tr.forward(80)
turtle.done()

r = 2
for i in range(100):
    tr.color("sky blue")
    tr. circle(r + i, 50)
turtle.done()
