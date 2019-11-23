import os

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
