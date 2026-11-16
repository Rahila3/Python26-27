import turtle
bob=turtle.Turtle()
bob.speed(6)
bob.shape("arrow")
screen=turtle.Screen()
screen.bgcolor("red")
screen.tracer(0)
for times in range(3) :
    bob.circle(50)
    bob.forward(times * 5)
    bob.left(120)
    bob.penup()
    bob.goto(200, 100)
    bob.pendown()
    bob.width(1)

for number in range(40):
    bob.forward(number * 4)
    bob.left(120)
    bob.penup()
    bob.goto(0,-200)
    bob.pendown()
    bob.width(1)
def flower1(x, y, size, c1,c2) :
    bob.color("brown")
    bob.pensize(5)
    bob.right(90)
    bob.forward(30)
    jump(x,y)
bob.circle (number * 5 + 10)
for times in range (70) :
    bob.circle (times * 5)
    bob. forward (times * 5)
    bob.left (120)
