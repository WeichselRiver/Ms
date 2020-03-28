from flask import Flask, url_for, render_template
from app import app


Marken = [
    {'Gebiet': 'Berlin',
     'Jahrgang' : 1948,
     'Satz': 'II. Kontrollrat mit schwarzem Aufdruck',
     'MichNr' : 1,
     'Falz': 0,
     'Postfrisch': 0,
     'Gestempelt': 0
     },
    {'Gebiet': 'Berlin',
     'Jahrgang' : 1948,
     'Satz': 'II. Kontrollrat mit schwarzem Aufdruck',
     'MichNr' : 2,
     'Falz': 0,
     'Postfrisch': 0,
     'Gestempelt': 2
     }
    ]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/Brommel")
def brommel():
    return render_template('brommel.html')

@app.route("/Altdeutschland")
def altdeutschland():
    return render_template('altdeutschland.html')
    
@app.route("/Berlin")
def berlin():
    return render_template('berlin.html', Marken = Marken)

# my routes
    