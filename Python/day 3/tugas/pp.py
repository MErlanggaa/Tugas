import turtle
import math

# Set up Turtle
screen = turtle.Screen()
screen.bgcolor("white")
logo_turtle = turtle.Turtle()
logo_turtle.speed(1)
logo_turtle.pensize(2)

# Function to draw a filled circle with a border
def draw_filled_circle(radius, fill_color, border_color):
    logo_turtle.penup()
    logo_turtle.goto(0, -radius)
    logo_turtle.pendown()
    logo_turtle.fillcolor(fill_color)
    logo_turtle.begin_fill()
    logo_turtle.circle(radius)
    logo_turtle.end_fill()
    logo_turtle.pencolor(border_color)
    logo_turtle.circle(radius)

# Function to draw text along a curve
def draw_text_along_curve(text, radius):
    angle_per_char = 8  # Adjust this angle for text spacing
    angle = -90  # Start at the top
    for char in text:
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        logo_turtle.penup()
        logo_turtle.goto(x, y - radius * 0.2)  # Adjust vertical position
        logo_turtle.setheading(angle - 90)  # Rotate the text
        logo_turtle.pendown()
        logo_turtle.pencolor("black")  # Text color is black
        logo_turtle.write(char, align="center", font=("Arial", 12, "bold"))
        angle -= angle_per_char

# Function to draw a hand (index finger and thumb) with red fill and white line art
def draw_hand():
    logo_turtle.penup()
    logo_turtle.goto(30, -80)
    logo_turtle.setheading(45)
    logo_turtle.pendown()
    logo_turtle.fillcolor("red")
    logo_turtle.begin_fill()
    for _ in range(2):
        logo_turtle.forward(50)
        logo_turtle.right(90)
        logo_turtle.forward(15)
        logo_turtle.right(90)
    logo_turtle.end_fill()
    logo_turtle.pencolor("white")
    for _ in range(2):
        logo_turtle.forward(50)
        logo_turtle.right(90)
        logo_turtle.forward(15)
        logo_turtle.right(90)

# Draw the white circle (outer circle)
draw_filled_circle(100, "white", "black")

# Draw the blue circle (inner circle) with a black border
draw_filled_circle(80, "blue", "black")

# Draw text along the curve in black inside the white circle
draw_text_along_curve("Sekolah Menengah Kejuruan Prestasi Prima", 90)

# Draw the hand (index finger and thumb) inside the blue circle
draw_hand()

# Close the Turtle graphics window on click
screen.exitonclick()
