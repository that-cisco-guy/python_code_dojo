from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'banana'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_users', methods = ['POST'])
def submit_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True)