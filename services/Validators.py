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


def password_is_copy_of_history(user, enteredPassword):
    password_history = DAL.get_UserPasswordsHistory_by_user_id(user.id)
    n = Config.HISTORY_OF_THE_PASSWORDS
    if password_history.count() < Config.HISTORY_OF_THE_PASSWORDS:
        n = password_history.count()
    for i in range(-n, n-Config.HISTORY_OF_THE_PASSWORDS):
        salt_from_storage = password_history[i].password[:Config.LENGTH_OF_THE_SALT]  # 32 is the length of the salt
        key_from_storage = password_history[i].password[Config.LENGTH_OF_THE_SALT:]
        enteredPassword_hash_salt = PasswordEncryption.hash_salt(enteredPassword, salt_from_storage)
        if enteredPassword_hash_salt[Config.LENGTH_OF_THE_SALT:] == key_from_storage:
            return True
    return False