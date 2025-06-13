import turtle
from PIL import Image
import os
import sys

# Retrieve command-line arguments
pattern_type = sys.argv[1]
nb_sides = int(sys.argv[2])
nb_reps = int(sys.argv[3])
size_input = int(sys.argv[4])
rot = int(sys.argv[5])
color = sys.argv[6]

# Convert size input to pixel values
size = {1: 50, 2: 125, 3: 200}.get(size_input, 100)

# Setup turtle environment
t = turtle.Turtle()
t.hideturtle()
t.color(color)
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("white")

# Drawing functions

# Draw a polygon with given number of sides
def draw_polygon(size, sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.left(angle)

# Draw a spiral by incrementally increasing the length of each segment
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
            t.right(144)
        t.left(rot_angle)

# Draw recursively a Koch fractal curve.
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

# Draw a circle
def draw_circle(radius, repetitions, rot_angle):
    for _ in range(repetitions):
        t.circle(radius)
        t.left(rot_angle)

# Draw selected pattern
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
    draw_circle(size, nb_reps, rot)

# Save the drawing as PNG file
canvas = turtle.getcanvas()
canvas.postscript(file="pattern.eps")
turtle.bye()

# Convert EPS file to PNG and save in 'static' folder
img = Image.open("pattern.eps")
img.save("static/pattern.png", "PNG")
os.remove("pattern.eps")