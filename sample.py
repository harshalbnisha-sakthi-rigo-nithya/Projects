"""# ...existing code...
import turtle

# create screen
turtle.setup(800, 400)
screen = turtle.Screen()
screen.title("Write AQUA")
screen.bgcolor("white")

# create pen to write text
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("blue")
pen.goto(0, 0)
pen.write("AQUA", align="center", font=("Arial", 96, "bold"))

turtle.done()
# ...existing code..."""
import turtle
# create screen
turtle.setup(800, 400)
screen = turtle.Screen()
screen.title("Write FLAMMA")
screen.bgcolor("white")
# create pen to write text
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("red")
pen.goto(0, 0)
pen.write("FLAMMA", align="center", font=("Ariel", 96, "bold"))
turtle.done()