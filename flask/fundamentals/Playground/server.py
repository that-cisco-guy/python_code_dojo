from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def level1():
    return render_template('index.html', x = 3, color = 'blue')

@app.route('/play/<int:x>')
def level2(x):
    return render_template('index.html', x = x, color = 'blue' )

@app.route('/play/<int:x>/<string:color>')
def level3(x,color):
    return render_template('index.html', x = x, color = color )

if __name__=="__main__":
    app.run(debug=True)