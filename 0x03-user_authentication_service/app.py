#!/usr/bin/env python3
""" File  executable path """

import logging
from auth import Auth
from flask import Flask, jsonify, request, redirect, abort, make_response
""" Module importation path """


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """ a users function that implements
    the POST /users route."""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ A login function to respond
    to the POST /sessions route."""
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify{"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port="5000")
