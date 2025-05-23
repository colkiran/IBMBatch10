# pip install flask (terminal)

from flask import Flask

app = Flask(__name__)       # __main__

@app.route("/")
def home():
    return "<h1> Hello World </h1>"

@app.route("/<usrname>")
def user(usrname):
    return f"<h2> Greetings Mr.{usrname}, Welcome to Flask Programming......"

if __name__ == '__main__':
    app.run(debug=True, use_reloader = True)

