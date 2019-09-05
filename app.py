# app.py
import base64
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Display the uploaded image
        image = request.files["file"]
        uri = "data:;base64," + base64.b64encode(image.read()).decode("utf-8")

    else:
        # Display a placeholder image
        uri = "/static/placeholder.png"

    return render_template("index.html", image_uri=uri)
