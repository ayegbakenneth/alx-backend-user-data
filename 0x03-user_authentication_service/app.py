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
    """POST /sessions
    Return:
        - JSON payload of the form containing login info.
    """
    # Get user credentials from form data
    email, password = request.form.get("email"), request.form.get("password")
    # Check if the user's credentials are valid
    if not AUTH.valid_login(email, password):
        abort(401)
    # Create a new session for the user
    session_id = AUTH.create_session(email)
    # Construct a response with a JSON payload
    response = jsonify({"email": email, "message": "logged in"})
    # Set a cookie with the session ID on the response
    response.set_cookie("session_id", session_id)
    # Return the response
    return response


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", port="5000")
