#!/usr/bin/env python3
""" File executable path """

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
        user = User(email=email, hashed_password=hashed_password)
        self._db.add_user(user)
        return user
