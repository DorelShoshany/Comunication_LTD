from datetime import datetime, timedelta
from config import Config
from models.AuthorizationResult import AuthorizationResult
from services import PasswordEncryption, UserTokenEncryptinoService, EmailService
from services.DAL import UserProvider, DAL
from services.PasswordVerifier import verify_user_password
from services.Validators import valid_email, password_is_valid


def start_login_process(email, enteredPassword):
    user = UserProvider.get_user_from_db_by_email(email)
    if user:
        if verify_user_password(user, enteredPassword):
            user.invalidLoginAttempt = 0
            return user, AuthorizationResult(isSuccess=verify_user_password(user, enteredPassword), Message="User Login!")
        else:
            #if hasattr(user, 'lockEndTime'):
            if user.lockEndTime != None and user.lockEndTime > datetime.now():
                return None, AuthorizationResult(isSuccess=False,
                                                     Message=Config.USER_IS_LOCKED_UNTIL + str(user.lockEndTime))
            else:
                user.invalidLoginAttempt = user.invalidLoginAttempt + 1
                if user.invalidLoginAttempt >= Config.LOGIN_LIMIT_TRYING:
                    user.lockEndTime = (datetime.now() + timedelta(minutes=15))  # .strftime("%B %d, %Y %I:%M%p")
                    user.invalidLoginAttempt = 0
                DAL.save_new_user_to_db(user)
    return None, AuthorizationResult(isSuccess=False, Message=Config.BAD_USER_NAME_OR_PASSWORD)


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
    if valid_email(email):
        user = UserProvider.get_user_from_db_by_email(email)
        if user:
            header = Config.TITLE_MSG_EMAIL_PASSWORD_RECOVERY
            body = UserTokenEncryptinoService.hash_email_with_date(email)
            EmailService.send(email=email, body=body, header=header)
            return AuthorizationResult(isSuccess=True, Message=Config.USER_NOT_FOUND)
        else:
            return AuthorizationResult(isSuccess=False, Message=Config.USER_NOT_FOUND)
    else:
        return AuthorizationResult(isSuccess=False, Message=Config.EMAIL_IS_NOT_VALID)


def start_verify_password_and_token(verify_password_dict):
    email = verify_password_dict.get("email")
    entered_token = verify_password_dict.get("token")
    if valid_email(email):
        user = UserProvider.get_user_from_db_by_email(email)
        if user:
            if UserTokenEncryptinoService.verify_hash_email_with_date(email, entered_token):
                return user, AuthorizationResult(isSuccess=True, Message=Config.VERIFY_HASH_EMAIL_WITH_DATE_SUCCESS)
            else:
                return None, AuthorizationResult(isSuccess=False, Message=Config.VERIFY_HASH_EMAIL_WITH_DATE_FAILED)
        return None, AuthorizationResult(isSuccess=False, Message=Config.BAD_USER_NAME_OR_PASSWORD)
    else:
        return None, AuthorizationResult(isSuccess=False, Message=Config.EMAIL_IS_NOT_VALID)


def start_change_password(user_id,change_password_dict):
    enteredPassword = change_password_dict['password']
    user = UserProvider.get_user_from_db_by_id(user_id)
    occurrences = Config.HISTORY_OF_THE_PASSWORDS
    res_password_is_valid = password_is_valid(enteredPassword)
    if res_password_is_valid.isSuccess:
        print(was_password_used_in_the_last_given_occurrences(user, enteredPassword, occurrences))
        if was_password_used_in_the_last_given_occurrences(user, enteredPassword, occurrences):
            return AuthorizationResult(isSuccess=False, Message=Config.PASSWORD_WAS_USED_IN_THE_LAST_GIVEN_OCCURRENCES)
        else:
            password_encrypt = PasswordEncryption.hash_salt(password=enteredPassword, salt=None)
            user.password = password_encrypt
            if DAL.save_new_user_to_db(user) and DAL.save_user_password_history_to_db(user):
                return AuthorizationResult(isSuccess=True, Message=Config.PASSWORD_CHANGE_SUCCESS)
            else:
                return AuthorizationResult(isSuccess=False, Message=Config.PASSWORD_CHANGE_FAILED)
            # else:
            # return AuthorizationResult(isSuccess=False, Message=Config.PASSWORD_CHANGE_FAILED)
    else:
        return res_password_is_valid