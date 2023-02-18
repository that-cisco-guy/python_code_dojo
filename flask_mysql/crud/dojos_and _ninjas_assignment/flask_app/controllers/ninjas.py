from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    ninjas = Ninja.all_ninjas()
    return render_template('all_ninjas.html', ninjas = ninjas)

@app.route('/new_ninja')
def new_ninja():
    return render_template('/new_ninja.html')

@app.route('/create_ninja', methods = ['POST'])
def create_ninja():
    Ninja.add_ninja(request.form)
    return redirect('/ninjas')