from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

# Landing page
@app.route('/')
def home():
    return redirect(url_for('landing'))

@app.route('/landing')
def landing():
    return render_template('landing.html')

# Pattern generator form and logic
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
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