from flask import Flask, render_template, \
    request, redirect, url_for

app = Flask(__name__)

@app.route('/')    #przekierowanie na strone 
def strona_glowna():
    return render_template("strona_glowna.html") #render zwraca strony, wszystko z html w katalogu template musi byc

@app.route('/granicefunkcji/twierdzenia')  # Nowa trasa dla strony z twierdzeniami dla granic ciagow
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

# if __name__ == '__main__':
#     app.run(debug=True)