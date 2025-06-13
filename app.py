from flask import Flask, render_template, request, redirect, url_for
import subprocess
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'mystery':
            # Random parameters for mystery
            pattern_type = random.choice(['spiral', 'polygon', 'star', 'fractal'])
            nb_sides = random.randint(3, 8) if pattern_type == 'polygon' else 0
            nb_reps = random.randint(5, 50)
            size = random.choice([1, 2, 3])
            rot = random.randint(5, 180)
            color = random.choice(['red', 'blue', 'green', 'black', 'orange', 'purple'])
        else:
            # User parameters
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
            # Redirect after generation to avoid forced POST reload
            return redirect(url_for('index', generated=1))

        except Exception as e:
            return render_template('index.html', error=str(e))

    # If GET, or redirect after success display with generated image if needed
    generated = request.args.get('generated', default=0, type=int)
    return render_template('index.html', image_generated=bool(generated))

if __name__ == '__main__':
    app.run(debug=True)