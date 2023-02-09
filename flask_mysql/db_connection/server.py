from flask import Flask, render_template, redirect, request
# import the class from friend.py
from friend import Friend
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/friends/<int:friend_id>")
def show(friend_id):
    one_friend = Friend.get_one(friend_id)
    return render_template("show.html", friend = one_friend)

@app.route('/friends/create', methods = ['post'])
def create_friend():
    Friend.save(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)