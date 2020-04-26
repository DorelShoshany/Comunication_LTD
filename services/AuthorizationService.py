from datetime import datetime, timedelta
from config import Config
from models.AuthorizationResult import AuthorizationResult
from services import PasswordEncryption, UserTokenEncryptinoService, EmailService
from services.DAL import UserProvider, DAL
from services.PasswordVerifier import verify_user_password


def start_login_process(email, enteredPassword):
    user = UserProvider.get_user_from_db_by_email(email)
    if user:
        if hasattr(user, 'lockEndTime'):
            if user.lockEndTime != None and user.lockEndTime > datetime.now():
                return None,AuthorizationResult(isSuccess=False, Message=Config.USER_IS_LOCKED_UNTIL + str(user.lockEndTime))
        if verify_user_password(user, enteredPassword):
            user.invalidLoginAttempt = 0
        else:
            user.invalidLoginAttempt = user.invalidLoginAttempt + 1
            if user.invalidLoginAttempt >= Config.LOGIN_LIMIT_TRYING:
                user.lockEndTime = (datetime.now() + timedelta(minutes=15)) #.strftime("%B %d, %Y %I:%M%p")
                user.invalidLoginAttempt = 0
        DAL.save_new_user_to_db(user)
        return user, AuthorizationResult(isSuccess=verify_user_password(user, enteredPassword), Message="")
    else:
        return None, AuthorizationResult(isSuccess=False, Message=Config.USER_NOT_FOUND)


def was_password_used_in_the_last_given_occurrences(user, enteredPassword, occurrences):
    password_history = DAL.get_UserPasswordsHistory_by_user_id(user.id)
    n = occurrences
    if password_history.count() < occurrences:
        n = password_history.count()
    for i in range(-n, n-occurrences):
        salt_from_storage = password_history[i].password[:Config.LENGTH_OF_THE_SALT]  # 32 is the length of the salt
        key_from_storage = password_history[i].password[Config.LENGTH_OF_THE_SALT:]
        enteredPassword_hash_salt = PasswordEncryption.hash_salt(enteredPassword, salt_from_storage)
        if enteredPassword_hash_salt[Config.LENGTH_OF_THE_SALT:] == key_from_storage:
            return True
    return False


def start_password_recovery_process(email):
    user = UserProvider.get_user_from_db_by_email(email)
    if user:
        header = Config.TITLE_MSG_EMAIL_PASSWORD_RECOVERY
        body = UserTokenEncryptinoService.hash_email_with_date(email)
        EmailService.send(email=email, body=body, header=header)
        return AuthorizationResult(isSuccess=True, Message=Config.USER_FOUND)
    else:
        return AuthorizationResult(isSuccess=False, Message=Config.USER_NOT_FOUND)