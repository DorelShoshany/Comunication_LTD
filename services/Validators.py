import re

from config import Config
from models.AuthorizationResult import AuthorizationResult
from services.DAL import SectorProivder


def form_is_full(form, field):
    form_is_not_full_res = AuthorizationResult(isSuccess=False, Message="All form fields must be filled in")
    for x in (True if field in form.keys() else False for field in field):
        if x == False:
            return form_is_not_full_res
    if ""  in form.values():
        return form_is_not_full_res
    if '""'  in form.values():
        return form_is_not_full_res
    return AuthorizationResult(isSuccess=True, Message="All form fields are filled ")


def sector_id_is_valid(sectorId):
    if SectorProivder.get_sector_by_id(sectorId) is None:
        return AuthorizationResult(isSuccess=False, Message="Sector is not exist")
    return AuthorizationResult(isSuccess=True, Message="Sector is exist")


def user_is_valid(user):
    if valid_email(user.email):
        return AuthorizationResult(isSuccess=True, Message=Config.EMAIL_IS_VALID)
    else:
        return AuthorizationResult(isSuccess=False, Message=Config.EMAIL_IS_NOT_VALID)


def valid_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.search(regex, email)


def password_is_valid(password):
    if len(password) != Config.LENGTH_OF_THE_PASSWORD:
        return AuthorizationResult(isSuccess=False, Message="Password should be exactly "+str(Config.LENGTH_OF_THE_PASSWORD)+" characters")
    for value, msg in Config.PASSWORD_VALIDATION_STRUCTURE.items():
        if re.search(value, password) is None:
            return AuthorizationResult(isSuccess=False,
                                       Message=msg)
    if Config.DICTIONARY_ATTACK:
        if dictionary_attack(password):
            return AuthorizationResult(isSuccess=False,
                                       Message="Password is not safe! ")
    return AuthorizationResult(isSuccess=True,
                                   Message="Password is ok! ")


def dictionary_attack(password):
    with open(Config.DICTIONARY_ATTACK_FILE) as f:
        for line in f:
            # For Python3, use print(line)
            if password in line:
                f.close()
                return True
    f.close()
    return False
