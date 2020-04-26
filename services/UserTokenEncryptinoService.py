import hashlib
from datetime import date


def hash_email_with_date(email):
    # encoding email + today date using encode()
    # then sending to SHA1()
    #TODO: change the time to be part of the parmars for this function
    hash_object = hashlib.sha1(bytes(email + str(date.today()), encoding='utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def verify_hash_email_with_date(email, entered_token):
    return hash_email_with_date(email) == entered_token