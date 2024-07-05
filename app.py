from flask import Flask, render_template

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

