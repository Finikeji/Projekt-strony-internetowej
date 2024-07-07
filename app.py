from flask import Flask, render_template, request, send_file
import matplotlib
matplotlib.use('Agg')  # Ustawienie backendu na 'Agg' przed importowaniem pyplot
import matplotlib.pyplot as plt
import io
import sympy as sp
import numpy as np

app = Flask(__name__)

@app.route('/')
def strona_glowna():
    return render_template("strona_glowna.html")

@app.route('/granicefunkcji/twierdzenia')
def twierdzenia():
    return render_template("twierdzenia_funkcje.html")

@app.route('/granicefunkcji/wzorywlasnosci')
def wzorywlasnosci():
    return render_template("wzorywlasnosci_funkcje.html")

@app.route('/granicefunkcji/przyklady')
def przyklady_funkcje():
    return render_template("przyklady_funkcje.html")

@app.route('/graniceciagow/twierdzenia')
def twierdzenia_ciagi():
    return render_template("twierdzenia_ciagi.html")

@app.route('/graniceciagow/wzorywlasnosci')
def wzorywlasnosci_ciagi():
    return render_template("wzorywlasnosci_ciagi.html")

@app.route('/graniceciagow/przyklady')
def przyklady_ciagi():
    return render_template("przyklady_ciagi.html")

@app.route('/graniceciagow/rysuj', methods=['GET', 'POST'])
def rysuj_granice():
    if request.method == 'POST':
        granica_str = request.form['granica']
        punkt_str = request.form['punkt']
        try:
            x = sp.symbols('x')
            granica_expr = sp.sympify(granica_str)
            punkt = sp.sympify(punkt_str)

            # Generowanie wykresu
            x_vals = np.linspace(float(punkt)-10, float(punkt)+10, 400)
            y_vals = [granica_expr.subs(x, val) for val in x_vals]

            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, label=f'y = {granica_str}')
            ax.axvline(x=float(punkt), color='r', linestyle='--', label=f'x = {punkt_str}')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend()
            ax.grid(True)

            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plt.close(fig)
            return send_file(img, mimetype='image/png')
        except Exception as e:
            return f"Błąd: {str(e)}"
    return render_template('formularz_granica.html')

if __name__ == '__main__':
    app.run(debug=True)
