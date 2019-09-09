# app.py
import os, base64
from flask import Flask, render_template, request

# Load system variables with dotenv
from dotenv import load_dotenv
load_dotenv()

# Load endpoint

# Load keys

# Create vision_client

# Create face_client

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Load image or placeholder
    uri = get_image_uri(request)
    # Create a placeholder for messages
    messages = []

    # TODO: Add code to retrieve text from picture

    # TODO: Add code to translate text

    return render_template("index.html", image_uri=uri, messages=messages)

@app.route("/train", methods=["GET", "POST"])
def train():
    # Load image or placeholder
    image_uri = get_image_uri(request)
    # Create a placeholder for messages
    messages = []

    # TODO: Add code 

def get_image_uri(request):
    # Set a placeholder if no image is uploaded
    uri = "/static/placeholder.png"
    if request.method == "POST":
        image = request.files["file"]
        uri = "data:;base64," + base64.b64encode(image.read()).decode("utf-8")
    return uri
