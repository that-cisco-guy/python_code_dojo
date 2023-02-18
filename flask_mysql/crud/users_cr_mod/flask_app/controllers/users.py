from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def read():
    users = User.read_users()
    return render_template('read.html', users = users)

@app.route('/new_user')
def new_user():
    return render_template('create.html')

@app.route('/create_user', methods = ['POST'])
def create_user():
    User.create_user(request.form)
    return redirect('/')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    data = {
        'id':id
    }
    User.delete_user(data)
    return redirect('/')

@app.route('/show_user/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("user.html",user=User.show_user(data))

@app.route('/edit_user/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.show_user(data))

@app.route('/update_user',methods=['POST'])
def update():
    User.update_user(request.form)
    return redirect('/')