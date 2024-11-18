import os
from flask_cors import CORS
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.utils import secure_filename
from functions import fetch
from PIL import Image
from datetime import datetime
import pytz

# Client Model
from Client import Client

# Set timezone
utc_time = datetime.now(pytz.timezone('UTC'))
est_time = utc_time.astimezone(pytz.timezone('US/Eastern'))

app = Flask(__name__)
CORS(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set the path for the images folder
app.config['IMAGES_FOLDER'] = 'static/images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        session.pop("requested", None)
        return render_template("index.html")
    
    else:
        # Check if the post request has the file part
        if 'img' not in request.files:
            return "No file part", 400

        img = request.files['img']
        
        if img.filename == '':
            return "No selected file", 400

        # Ensure the images folder exists
        if not os.path.exists(app.config['IMAGES_FOLDER']):
            os.makedirs(app.config['IMAGES_FOLDER'])
        
        # Save the image securely
        filename = secure_filename(img.filename)
        img_path = os.path.join(app.config['IMAGES_FOLDER'], filename)
        
        img.save(img_path)  # Save the uploaded image

        scan_type = request.form.get("button-group")
        if not scan_type:
            mssg = "Scan type not selected."
            return render_template("error.html", error=mssg)

        location = request.form.get("button-group2")
        if not location:
            mssg = "Location not specified."
            return render_template("error.html", error=mssg)
        
        # Get appropriate model
        model_path = os.path.join(f"./models/{location.lower()}.keras")
        label_path = os.path.join(f"./labels/{location.lower()}.txt")
        # Get client model prediction
        client = Client(model_path, label_path)
        prediction = client.predict(img)
        #Debug: print(img, prediction)
        description = fetch(prediction) # Fetch description based on prediction
        return render_template("index.html", description=description, image_filename=filename)

if __name__ == '__main__':
    app.run(debug=True)