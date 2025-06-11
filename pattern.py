import turtle
from PIL import Image
import os
import sys

# Get command-line arguments
pattern_type = sys.argv[1]
nb_sides = int(sys.argv[2])
nb_reps = int(sys.argv[3])
size_input = int(sys.argv[4])
rot = int(sys.argv[5])
color = sys.argv[6]

# Convert size input to pixels
size = {1: 50, 2: 125, 3: 200}.get(size_input, 100)

# Setup turtle
t = turtle.Turtle()
t.hideturtle()
t.color(color)
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("white")

# Drawing functions
def draw_polygon(size, sides):
    """Draw a regular polygon with given size and number of sides."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.left(angle)

def draw_spiral(size, repetitions, angle, increment):
    """Draw a spiral by incrementally increasing the length of each segment."""
    length = size
    for _ in range(repetitions):
        t.forward(length)
        t.left(angle)
        length += increment

def draw_star(size, repetitions, rot_angle):
    """Draw multiple 5-pointed stars, rotated by a specified angle each time."""
    for _ in range(repetitions):
        for _ in range(5):
            t.forward(size)
            t.right(144)
        t.left(rot_angle)

def draw_fractal(length, level):
    """Recursively draw a Koch fractal curve."""
    if level == 0:
        t.forward(length)
    else:
        draw_fractal(length / 3, level - 1)
        t.left(60)
        draw_fractal(length / 3, level - 1)
        t.right(120)
        draw_fractal(length / 3, level - 1)
        t.left(60)
        draw_fractal(length / 3, level - 1)

# Draw the selected pattern
if pattern_type == "spiral":
    draw_spiral(size, nb_reps, rot, increment=5)
elif pattern_type == "polygon":
    for _ in range(nb_reps):
        draw_polygon(size, nb_sides)
        t.left(rot)
elif pattern_type == "star":
    draw_star(size, nb_reps, rot)
elif pattern_type == "fractal":
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    draw_fractal(size, nb_reps)

# Save the drawing as PNG
canvas = turtle.getcanvas()
canvas.postscript(file="pattern.eps")
turtle.bye()

img = Image.open("pattern.eps")
img.save("static/pattern.png", "PNG")
os.remove("pattern.eps")