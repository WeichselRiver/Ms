from flask import Flask, url_for, render_template, request, redirect
from app import app, Todo, db


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


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        task_content = request.form['content']
        BackMichNr = request.form['MichNr']
        new_task = Todo(content=task_content, MichNr = BackMichNr)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('home.html', tasks=tasks)


@app.route("/Brommel")
def brommel():
    return render_template('brommel.html')

@app.route("/Altdeutschland")
def altdeutschland():
    return render_template('altdeutschland.html')
    
@app.route("/Berlin")
def berlin():
    return render_template('berlin.html', Marken = Marken)

# my routes 2
    