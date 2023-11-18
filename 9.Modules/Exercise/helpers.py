from hashlib import sha256      # import hash module
from canvas import frame        # import frame


def clean_screen():             # clean screen after action
    frame.delete('all')


def get_password_hash(password):                    # encoding password
    hash_object = sha256(password.encode())         # most popular module for hashing

    return str(hash_object.hexdigest())             # return string key of the hash
