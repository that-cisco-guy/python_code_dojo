from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug = True)