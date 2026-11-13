# Geometric Pattern Generator

A web app that turns a few parameters into a geometric drawing. Pick a shape, a size, a number of repetitions, a rotation angle and a color. The server draws the pattern with Python's Turtle graphics, converts it to an image and shows it in the browser, along with a history of everything generated in the session.

Built during my exchange semester abroad as a 5 ECTS project, written entirely in English.

## Features

- **Five pattern families**: polygon, star, spiral, circle and a recursive **Koch fractal**.
- **Parameters**: number of sides (polygons), size, repetitions, rotation angle (slider) and color.
- **Mystery Pattern** button: picks a random family and random parameters.
- **History** panel listing every generated pattern with its parameters.
- **Guard rails**: the sides field only appears for polygons, and fractals are capped at 7 levels to keep rendering fast.
- **Loading state** while the server draws, and a responsive layout with a separate landing page.
- **Self-cleaning**: generated images are deleted when the server shuts down.

## How it works

```
Browser form ──POST──► Flask (app.py) ──subprocess──► pattern.py (Turtle)
                                                           │
                        PNG in static/ ◄── Pillow ◄── canvas → PostScript
```

1. `app.py` reads the form, or draws random values for a mystery pattern, and runs `pattern.py` as a separate process with the parameters as arguments.
2. `pattern.py` draws with Turtle, exports the canvas as PostScript, converts it to PNG with Pillow and gives it a unique file name.
3. Flask redirects to the result page and adds the image and its parameters to the history, served as JSON at `/history`.

Running the drawing in its own process keeps Turtle's window and global state out of the web server.

## Run it locally

Requirements:
- Python 3 with Tk (Turtle needs it);
- Ghostscript, which Pillow uses to read the PostScript export (`brew install ghostscript` on macOS).

```bash
git clone https://github.com/matrixlnrs/patterns-generator
cd patterns-generator
pip install -r requirements.txt
python3 app.py
```

Then open http://127.0.0.1:5000/.

## Project layout

```
app.py              Flask routes: landing page, generator, history API, cleanup on exit
pattern.py          Turtle drawing functions and the PNG export
templates/          landing page and generator page (Jinja2)
static/             styles, front-end script (form logic, loader, history modal)
```

## Tech

Python · Flask · Turtle graphics · Pillow · HTML/CSS · JavaScript
