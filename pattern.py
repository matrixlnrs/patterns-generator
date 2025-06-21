import turtle
from PIL import Image
import os
import sys

# retrieve command-line arguments
pattern_type = sys.argv[1]
nb_sides = int(sys.argv[2])
nb_reps = int(sys.argv[3])
size_input = int(sys.argv[4])
rot = int(sys.argv[5])
color = sys.argv[6]

# convert size input to pixel values
if size_input == 1:
    size = 50
elif size_input == 2:
    size = 125
elif size_input == 3:
    size = 200
else:
    size = 100

# setup turtle environment
t = turtle.Turtle()
t.hideturtle()
t.color(color)
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("white")

# drawing functions

# draw a polygon with given number of sides
def draw_polygon(size, sides):
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.left(angle)

# draw a spiral by increasing the length of segment
def draw_spiral(size, repetitions, angle, increase):
    length = size
    for i in range(repetitions):
        t.forward(length)
        t.left(angle)
        length += increase

# draw multiple 5-pointed stars
def draw_star(size, repetitions, rot_angle):
    for i in range(repetitions):
        for i in range(5):
            t.forward(size)
            t.right(144)
        t.left(rot_angle)

# draw recursively a Koch fractal curve.
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

# draw a circle
def draw_circle(radius, repetitions, rot_angle):
    for i in range(repetitions):
        t.circle(radius)
        t.left(rot_angle)

# draw selected pattern
if pattern_type == "spiral":
    draw_spiral(size, nb_reps, rot, increase=5)
elif pattern_type == "polygon":
    for i in range(nb_reps):
        draw_polygon(size, nb_sides)
        t.left(rot)
elif pattern_type == "star":
    draw_star(size, nb_reps, rot)
elif pattern_type == "fractal":
    screen.tracer(0, 0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    for i in range(nb_reps):
        draw_fractal(size, nb_reps)
        t.right(120)
    screen.update()
elif pattern_type == "circle":
    draw_circle(size, nb_reps, rot)

# save the drawing as PNG file
canvas = turtle.getcanvas()
canvas.postscript(file="pattern.eps")
turtle.bye()

# convert EPS file to PNG and save in 'static' folder
img = Image.open("pattern.eps")
img.save("static/pattern.png", "PNG")
os.remove("pattern.eps")