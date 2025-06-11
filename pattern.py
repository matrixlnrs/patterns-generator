import turtle
from PIL import Image
import os
import sys

# Retrieve arguments
pattern_type = sys.argv[1]
nb_sides = int(sys.argv[2])
nb_reps = int(sys.argv[3])
size_input = int(sys.argv[4])
rot = int(sys.argv[5])
color = sys.argv[6]

size = {1: 50, 2: 125, 3: 200}.get(size_input, 100)

# Initialize turtle graphics
t = turtle.Turtle()
t.hideturtle()
t.color(color)
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("white")

# Drawing functions

# Draw a polygon with a certain number of sides
def draw_polygon(size, sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.left(angle)

# Draw a spiral by increasing the length of each segment incrementally
def draw_spiral(size, repetitions, angle, increment):
    length = size
    for _ in range(repetitions):
        t.forward(length)
        t.left(angle)
        length += increment

# Draw multiple 5-pointed stars
def draw_star(size, repetitions, rot_angle):
    for _ in range(repetitions):
        for _ in range(5):
            t.forward(size)
            t.right(144)  # Star angle
        t.left(rot_angle)

# Draw recursively a Koch fractal curve at the given recursion level
def draw_fractal(length, level):
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

# Draw circles
def draw_circles(size, repetitions, rot_angle):
    for _ in range(repetitions):
        t.circle(size)
        t.left(rot_angle)

# Execute the appropriate drawing function based on pattern_type
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
elif pattern_type == "circle":
    draw_circles(size, nb_reps, rot)

# Save the turtle drawing as a PNG file
canvas = turtle.getcanvas()
canvas.postscript(file="pattern.eps")
turtle.bye()  # Close the turtle graphics window

# Convert EPS file to PNG and save it in the static directory
img = Image.open("pattern.eps")
img.save("static/pattern.png", "PNG")
os.remove("pattern.eps")  # Clean up the temporary EPS file