import hashlib
import os


from config import Config
# Will generate salt , hash with salt and append salt in the end of the password
# we can select some encryption that saves each password as hash of x characters and append the salt after it

length_of_the_salt = Config.LENGTH_OF_THE_SALT


def hash_salt(password, salt):
    if salt is None:
        salt = generate_new_salt()
    #password_bytes = bytes(password, encoding='utf-8')
    #salt_bytes = bytes(password, encoding='utf-8')
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Store them as:
    storage = salt + key
    return storage


def generate_new_salt():
    return os.urandom(32)

