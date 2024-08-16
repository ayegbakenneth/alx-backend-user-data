#!/usr/bin/env python3
""" File executable path """
from typing import Union
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
""" Module importation path """


def _hash_password(password: str) -> bytes:
    """ A method  that takes in a password
    string arguments and returns bytes. """
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(encoded_password, salt)
    return password_hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ A method that returns a user object
        after recieving the login credentials """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """ An Auth.valid_login method """
        user = self._db.find_user_by(email=email)
        if user:
            hashed_password = user._hashed_password
            entered_password = password.encode("utf-8")
            if bcrypt.checkpw(entered_password, hashed_password)
            return True

        return False
