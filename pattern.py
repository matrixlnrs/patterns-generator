import turtle
from PIL import Image
import os
import sys  # To receive arguments from the command line
import random

if len(sys.argv) == 2 and sys.argv[1] == "mystery":
    nb_sides = random.choice([0] + list(range(3, 10)))
    nb_reps = random.randint(10, 50)
    size_input = random.choice([1, 2, 3])
    rot = random.randint(10, 180)
    color = random.choice(["red", "blue", "green", "purple", "black", "orange", "cyan"])
else:
    nb_sides = int(sys.argv[1])
    nb_reps = int(sys.argv[2])
    size_input = int(sys.argv[3])
    rot = int(sys.argv[4])
    color = sys.argv[5]

# Ask for parameters
nb_sides = int(sys.argv[1])
nb_reps = int(sys.argv[2])
size_input = int(sys.argv[3])
rot = int(sys.argv[4])
color = sys.argv[5]

# Convert size into pixels
if size_input == 1:
    size = 50
elif size_input == 2:
    size = 125
elif size_input == 3:
    size = 200
else:
    size = 100

# Setup turtle
t = turtle.Turtle()
t.hideturtle()
t.color(color)
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("white")

# Polygon pattern drawing
def draw_polygon(size, sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.left(angle)

# Spiral pattern drawing
def draw_spiral(size, repetitions, angle, increment):
    length = size
    for _ in range(repetitions):
        t.forward(length)
        t.left(angle)
        length += increment

# Main drawing
if nb_sides == 0:
    draw_spiral(size, nb_reps, rot, increment=5)
else:
    for _ in range(nb_reps):
        draw_polygon(size, nb_sides)
        t.left(rot)

# Save image as EPS
canvas = turtle.getcanvas()
canvas.postscript(file="pattern.eps")
turtle.bye()

# Convert EPS to PNG
img = Image.open("pattern.eps")
img.save("static/pattern.png", "PNG")
os.remove("pattern.eps")    # Delete the EPS file to keep only the PNG