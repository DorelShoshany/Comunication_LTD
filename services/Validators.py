import re

from config import Config
from services import PasswordEncryption
from services.DAL import SectorProivder, DAL


def sector_id_is_valid(sectorId):
    return SectorProivder.get_sector_by_id(sectorId)


def user_is_valid(user):
    return valid_email(user.email)


def valid_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.search(regex, email)


def password_is_valid(password):
    if len(password) != Config.LENGTH_OF_THE_PASSWORD:
        return False
    elif re.search('[0-9]', password) is None:
        return False # print("Make sure your password has a number in it")
    elif re.search('[A-Z]', password) is None:
        return False # print("Make sure your password has a capital letter in it")
    else:
        return True


