import turtle

# Ask user for pattern type
pattern = int(input("What pattern do you want to draw?\n 1. Polygon \n 2. Circle \n 3. Spiral \n"))

# Number of sides for polygon
nb_sides = 0
if pattern == 1:
    nb_sides = int(input("How many sides do you want for the polygon? \n"))

nb_reps = int(input("How many repetitions do you want? \n"))
size = int(input("What size do you want the pattern to be? \n"))
rot = int(input("What rotation angle do you want? \n"))
color = input("What color do you want? (e.g. red, blue, black...) \n")

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

# Circle pattern
def draw_circles(size, repetitions, angle):
    for _ in range(repetitions):
        t.circle(size)
        t.left(angle)

# Spiral pattern
def draw_spiral(size, repetitions, angle, increment):
    length = size
    for _ in range(repetitions):
        t.forward(length)
        t.left(angle)
        length += increment

# Main drawing
if pattern == 1:
    for _ in range(nb_reps):
        draw_polygon(size, nb_sides)
        t.left(rot)
elif pattern == 2:
    draw_circles(size, nb_reps, rot)
elif pattern == 3:
    draw_spiral(size, nb_reps, rot, increment=5)
else:
    print("Invalid pattern choice.")

turtle.done()