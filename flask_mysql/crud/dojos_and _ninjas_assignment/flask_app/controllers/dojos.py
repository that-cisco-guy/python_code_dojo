from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def dojos():
    dojos = Dojo.all_dojos()
    return render_template('all_dojos.html', dojos = dojos)

@app.route('/create_dojo', methods = ['POST'])
def create_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/')