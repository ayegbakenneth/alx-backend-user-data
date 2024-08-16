#!/usr/bin/env python3
""" File  executable path """

from auth import Auth
from flask import Flask, jsonify, request
""" Module importation path """


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """ a users function that implements
    the POST /users route."""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port="5000")
