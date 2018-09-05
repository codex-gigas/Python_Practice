import turtle
brad = turtle.Turtle()
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

def forward(turtle, distance):
    speed = turtle.speed()
    for _ in range(0, distance, speed):
        turtle.forward(speed)
        yield 0
"""def func1(turtle):
    for _ in range(4):
        turtle.right(45)
        yield from forward(turtle, 40)
        turtle.left(45)
        yield from forward(turtle, 30)
        turtle.left(45)
        yield from forward(turtle, 40)
        turtle.right(45)
        yield from forward(turtle, 30)

func1()"""
        
def A(turtle):
    draw_art()
    brad.left(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.right(90)
    brad.forward(50)
    brad.left(90)
    brad.forward(50)
def B(turtle):
    print("\t")
    draw_art()
    brad.left(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(80)
    brad.right(90)
    brad.forward(50)
    brad.right(90)
    brad.forward(42)
    brad.left(90)
    brad.forward(4)
    brad.left(90)
    brad.forward(42)
    brad.right(90)
    brad.forward(50)
    brad.right(90)
    brad.forward(90)
    brad.right(90)
    brad.forward(5)
A(turtle)
B(turtle)

