import turtle

# Function to draw a rectangle (persegi panjang)
def draw_rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

# Function to draw a triangle (segitiga)
def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# Function to draw a trapezium
def draw_trapezium(base1, base2, height):
    turtle.forward(base1)
    turtle.left(135)
    turtle.forward(height)
    turtle.left(45)
    turtle.forward(base2)
    turtle.left(45)  # Adjust the angle here
    turtle.forward(height)
    turtle.left(135)  # Adjust the angle here
    turtle.forward(base1)
    turtle.forward(base2)

# Function to draw a parallelogram (jajar genjang)
def draw_parallelogram(base, height):
    turtle.forward(base)
    turtle.left(60)
    turtle.forward(height)
    turtle.left(120)
    turtle.forward(base)
    turtle.left(60)
    turtle.forward(height)

# Function to draw a rhombus (belah ketupat)
def draw_rhombus(side_length):
    for _ in range(2):
        turtle.forward(side_length)
        turtle.left(60)
        turtle.forward(side_length)
        turtle.left(120)

# Set up the Turtle screen
turtle.speed(5)

# Draw the shapes
turtle.color("red")
draw_rectangle(100, 50)

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

turtle.color("yellow")
draw_triangle(100)

turtle.penup()
turtle.goto(-150, -100)
turtle.pendown()

turtle.color("green")
draw_trapezium(100, 200, 80)

turtle.penup()
turtle.goto(150, -100)
turtle.pendown()

turtle.color("purple")
draw_parallelogram(100, 50)

turtle.penup()
turtle.goto(-150, -200)
turtle.pendown()

turtle.color("orange")
draw_rhombus(70)

# Close the Turtle graphics window on click
turtle.exitonclick()
