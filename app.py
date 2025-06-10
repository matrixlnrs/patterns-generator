from flask import Flask, render_template, request, redirect, url_for
import subprocess
import random

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('landing'))

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'mystery':
            nb_sides = random.choice([0] + list(range(3, 10)))
            nb_reps = random.randint(10, 50)
            size = random.choice([2, 3, 4])  # Small, Medium, Large
            rot = random.randint(5, 180)
            color = random.choice(['red', 'blue', 'green', 'black', 'orange', 'purple'])
        else:
            nb_sides = request.form.get('sides', type=int)
            nb_reps = request.form.get('reps', type=int)
            size = request.form.get('size', type=int)
            rot = request.form.get('rot', type=int)
            color = request.form.get('color', type=str)

        try:
            subprocess.run([
                'python3', 'pattern.py',
                str(nb_sides), str(nb_reps), str(size), str(rot), color
            ], check=True)
            return render_template('index.html', image_generated=True)
        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html', image_generated=False)

if __name__ == '__main__':
    app.run(debug=True)