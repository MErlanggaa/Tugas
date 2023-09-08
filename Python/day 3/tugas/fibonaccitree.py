import turtle

def fibonacci_tree(t, branch_len, angle, level):
    if level > 0:
        t.forward(branch_len)
        t.right(angle)
        fibonacci_tree(t, branch_len - 15, angle, level - 1)
        t.left(2 * angle)
        fibonacci_tree(t, branch_len - 15, angle, level - 1)
        t.right(angle)
        t.backward(branch_len)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("green")
    
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    
    fibonacci_tree(t, 100, 30, 5)
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
