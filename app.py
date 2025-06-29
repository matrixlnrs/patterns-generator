from flask import Flask, render_template, request, redirect, url_for, jsonify
import subprocess
import random
import os
import glob
import atexit

app = Flask(__name__)

# list to keep track of the generated patterns
history = []

# route for the landing page
@app.route('/')
def home():
    return render_template('landing.html')

# route for the main page where you can generate patterns
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'mystery':
            # if the user chose mystery randomly generate parameters
            pattern_type = random.choice(['spiral', 'polygon', 'star', 'circle'])
            nb_sides = random.randint(3, 8) if pattern_type == 'polygon' else 0
            nb_reps = random.randint(5, 50)
            size = random.choice([1, 2, 3])
            rot = random.randint(5, 180)
            color = random.choice(['Red', 'Blue', 'Green', 'Black', 'Orange', 'Purple'])
        else:
             # get parameters from the form input
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

            image_url = url_for('static', filename=generated_filename)

            history.append({
                'image_url': image_url,
                'params': f"{pattern_type} | sides={nb_sides} | reps={nb_reps} | size={size} | rot={rot} | color={color}"
            })

            return redirect(url_for('index', generated=1, image=generated_filename))

        except Exception as e:
            return render_template('index.html', error=str(e))

    image_filename = request.args.get('image', default=None, type=str)
    return render_template('index.html', image_generated=bool(image_filename), image_filename=image_filename)

# route to return history of generated patterns
@app.route('/history')
def get_history():
    return jsonify(history[::-1])

# function to clean up image files
def cleanup_generated_images():
    # delete all PNG except 'painting.png'
    for file in glob.glob("static/*.png"):
        if not file.endswith("painting.png"):
            os.remove(file)
    if os.path.exists("last_generated.txt"):
        os.remove("last_generated.txt")

# cleanup function to run on shutdiwn of the server
atexit.register(cleanup_generated_images)

if __name__ == '__main__':
    app.run(debug=True)