from flask import Flask, render_template, request, redirect, url_for
import subprocess
import random
import os
import glob
import atexit

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'mystery':
            # random parameters for mystery
            pattern_type = random.choice(['spiral', 'polygon', 'star', 'circle'])
            nb_sides = random.randint(3, 8) if pattern_type == 'polygon' else 0
            nb_reps = random.randint(5, 50)
            size = random.choice([1, 2, 3])
            rot = random.randint(5, 360)
            color = random.choice(['red', 'blue', 'green', 'black', 'orange', 'purple'])
        else:
            # user parameters
            pattern_type = request.form.get('pattern_type', type=str)
            nb_sides = request.form.get('sides', type=int) if pattern_type == 'polygon' else 0
            nb_reps = request.form.get('reps', type=int)
            size = request.form.get('size', type=int)
            rot = request.form.get('rot', type=int)
            color = request.form.get('color', type=str)

        try:
            subprocess.run(
                [
                    'python3', 'pattern.py',
                    pattern_type,
                    str(nb_sides),
                    str(nb_reps),
                    str(size),
                    str(rot),
                    color
                ],
                check=True
            )

            with open("last_generated.txt", "r") as f:
                generated_filename = f.read().strip()

            return redirect(url_for('index', generated=1, image=generated_filename))

        except Exception as e:
            return render_template('index.html', error=str(e))

    # GET request (or redirect after POST)
    image_filename = request.args.get('image', default=None, type=str)
    return render_template('index.html', image_generated=bool(image_filename), image_filename=image_filename)

# cleanup all generated images (except painting.png) on server shutdown
def cleanup_generated_images():
    for file in glob.glob("static/*.png"):
        if not file.endswith("painting.png"):
            os.remove(file)
    if os.path.exists("last_generated.txt"):
        os.remove("last_generated.txt")

atexit.register(cleanup_generated_images)

if __name__ == '__main__':
    app.run(debug=True)