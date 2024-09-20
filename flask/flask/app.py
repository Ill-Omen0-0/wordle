import os

from flask import Flask, flash, redirect, render_template, request, session
from tempfile import mkdtemp
import datetime

# Configure application
app = Flask(__name__, static_url_path='/static')

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/")
def home():
    return render_template("home.html")

if __name__=='__main__':
    app.run(debug=True)
