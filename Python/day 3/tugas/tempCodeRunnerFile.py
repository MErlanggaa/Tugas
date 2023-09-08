import turtle as t
import math

def draw_circle(x, y, r, fill_color):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def draw_logo():
    draw_circle(0, -200, 230, "white")
    draw_circle(0, -200, 180, "blue")

def draw_hand():
    t.penup()
    t.goto(30, -80)
    t.setheading(45)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(50)
        t.right(90)
        t.forward(15)
        t.right(90)
    t.end_fill()
    t.pencolor("white")  # Mengatur warna garis putih
    t.forward(50)  # Garis putih pertama
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(50)  # Garis putih kedua
    t.right(90)
    t.forward(15)
    t.right(90)

def draw_text_along_curve(text, radius):
    angle_per_char = 8
    angle = -90
    for char in text:
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        t.penup()
        t.goto(x, y - radius * 0.2)
        t.setheading(angle - 90)
        t.pendown()
        t.pencolor("black")
        t.write(char, align="center", font=("Arial", 12, "bold"))
        angle -= angle_per_char

def main():
    t.speed(10)
    t.bgcolor("lightblue")
    t.screensize(800, 600)
    draw_logo()
    t.hideturtle()

    t.speed(10)
    tut = t.Screen()
    t.width(5)

    t.color("black")
    t.fillcolor("red")
    
    t.begin_fill()
    
    t.penup()
    t.goto(-50, -300)
    t.pendown()
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(55) 
    
    def draw(rad):
        t.penup()
        t.goto(-70, -280)
        t.pendown()
        for i in range(1):
            t.circle(rad, 113)
            t.circle(rad//2, 20)
    
    t.seth(-45)
    draw(88)

    t.setheading(-270)
    t.forward(60)  # kelingking
    t.circle(15, 180)
    t.forward(60)
    t.left(180)  # manis
    t.forward(60)
    t.circle(15, 180)
    t.forward(60)
    t.left(180)  # tengah
    t.forward(60)
    t.circle(15, 180)
    t.forward(60)
    t.left(180)  # telunjuk
    t.forward(140)
    t.circle(17, 180)
    t.forward(130)
    t.right(125)  # jempol
    t.forward(60)
    t.circle(20, 180)
    t.forward(64)
    t.right(50)
    t.forward(30)
    
    t.end_fill()
    
    t.hideturtle()
    t.done()

    # Set up Turtle
    screen = t.Screen()
    screen.bgcolor("white")
    logo_turtle = t.Turtle()
    logo_turtle.speed(1)
    logo_turtle.pensize(2)

    # Draw the white circle (outer circle)
    draw_circle(100, "white", "black")

    # Draw the blue circle (inner circle) with a black border
    draw_circle(80, "blue", "black")

    # Draw text along the curve in black inside the white circle
    draw_text_along_curve("Sekolah Menengah Kejuruan Prestasi Prima", 90)

    # Draw the hand (index finger and thumb) inside the blue circle with white lines
    draw_hand()

    # Close the Turtle graphics window on click
    screen.exitonclick()

if __name__ == "__main__":
    main()
