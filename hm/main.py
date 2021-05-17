from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/main")
def main():
    return render_template("home.html")

@app.route("/")
def hi():
    return redirect(url_for("main"))

app.run(debug = True)