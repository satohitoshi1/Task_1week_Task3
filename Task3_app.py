from flask import Flask
from flask import render_template
import Task3_images

app = Flask(__name__)


@app.route("/")
def click():
    return render_template("index.html")


@app.route("/img")
def display():
    Task3_images.random_color_make()
    return render_template("images.html")


app.run(debug=True)
