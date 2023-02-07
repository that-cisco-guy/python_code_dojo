from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'banana'

@app.route('/')
def index():
    if 'visit' not in session:
        session['visit'] = 0
    else:
        session['visit'] += 1
    return render_template('index.html')

@app.route('/add_two')
def add_two():
    session['visit'] += 1
    return redirect('/')

@app.route('/destroy_session')
def detroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)