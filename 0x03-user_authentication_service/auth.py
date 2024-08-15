#!/usr/bin/env python3
""" File executable path """

import bcrypt
""" Module importation path """


def _hash_password(password: str) -> bytes:
    """ A method  that takes in a password
    string arguments and returns bytes. """
    encoded_password = password.encode('utf-8')
    salt = bcryt.gensalt()
    password_hashed = bcryt.hashpw(encoded_password, salt)
    return password_hashed
