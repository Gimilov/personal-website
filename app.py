from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/recommendations")
def recommendations():
    return render_template("recommendations.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/whygimilov")
def whygimilov():
    return render_template("whygimilov.html")