import os

from flask_cors import CORS
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from functions import fetch


from datetime import datetime
import pytz
utc_time = datetime.now(pytz.timezone('UTC'))
est_time = utc_time.astimezone(pytz.timezone('US/Eastern'))

app = Flask(__name__)
CORS(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="GET":
        session.pop("requested", None)
        return render_template("index.html")
    else:
        img = request.form.get("img")
        if not img:
            mssg = "Medical diagnosis image not uploaded."
            return render_template("error.html", error=mssg)

        scan_type = request.form.get("button-group")
        if not scan_type:
            mssg = "Scantype not selected."
            return render_template("error.html", error=mssg)
        else:
            print(f"Selected option: {scan_type}")

        location = request.form.get("button-group2")
        if not location:
            mssg = "Location not specified."
            return render_template("error.html", error=mssg)
        else:
            print(f"Selected option: {location}")
        
        return render_template("index.html")