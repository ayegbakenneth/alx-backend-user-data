#!/usr/bin/env python3
""" File  executable path """

from flask import Flask, jasonify
""" Module importation path """


app = Flask(__name__)


@app.route("/", method=["GET"])
def home():
    return jasonify({"message": "Bienvenue"})


if __name__ = ("__main__"):
    app.run(host="0.0.0.0", port="5000")
