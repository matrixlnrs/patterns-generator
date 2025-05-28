import turtle
from PIL import Image
import os

# Ask for parameters
nb_sides = int(input("How many sides do you want?\n(Use 0 for a spiral)\n"))
nb_reps = int(input("How many repetitions do you want? \n"))
size = int(input("What size do you want the pattern to be?\n 1. Small \n 2. Medium \n 3. Large \n"))
# User choice to actual size values
size_map = {
    1: 50,
    2: 125,
    3: 200
}
size = size_map.get(size, 50)
rot = int(input("What rotation angle do you want? \n"))
color = input("What color do you want? (red, blue, black...) \n")

# Setup turtle
t = turtle.Turtle()
t.color(color)
t.speed(0)

# Polygon pattern
def draw_polygon(size, sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.left(angle)

# Spiral pattern
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

# Convert EPS to PNG
img = Image.open("pattern.eps")
img.save("pattern.png", "PNG")

print("Pattern saved as 'pattern.png'")

# Delete the EPS file to keep only the PNG
os.remove("pattern.eps")

# Keep the turtle window open
turtle.done()