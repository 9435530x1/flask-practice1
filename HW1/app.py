from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile")
def profile():
    my_hobbies = ["음악감상", "독서", "게임"]
    return render_template("profile.html", hobbies=my_hobbies)

@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)
