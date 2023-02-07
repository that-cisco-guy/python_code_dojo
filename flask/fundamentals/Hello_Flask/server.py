from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          
def index():
    return render_template('index.html')  

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<string:name>/<int:num>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name, num):
    return render_template('hello.html', name = name, num = num)

@app.route('/lists')
def render_lists():

    student_info = [
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Michael', 'age' : 35 },
        {'name' : 'Mark', 'age' : 25 },
        {'name' : 'KB', 'age' : 27 },

    ]
    return render_template('lists.html', random_numbers = [3, 1, 5, ], students = student_info)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
# import statements, maybe some other routes
    



