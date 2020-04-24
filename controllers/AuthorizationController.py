from config import Config
from services import EmailService, UserTokenEncryptinoService, PasswordEncryption
from services.DAL import UserProvider, DAL
from services.PasswordVerifier import verify_user_password
from services.Validators import password_is_copy_of_history


class AuthorizationController():

    def login(self, request):
        if request.is_json:
            email = request.json['email']
            enteredPassword = request.json['password']
        else:
            email = request.form['email']
            enteredPassword = request.form['password']
        user = UserProvider.get_user_from_db_by_email(email)
        # TODO: return user is not exist and  verify
        if verify_user_password(user, enteredPassword):
            return user
        else:
            return None

    # POST: This will generate a token and send to the user email in order
    def start_password_recovery(self, request):
        if request.is_json:
            email = request.json['email']
        else:
            email = request.form['email']
        user = UserProvider.get_user_from_db_by_email(email)
        if user is None:
            return False, Config.USER_NOT_FOUND
        else:
            header = Config.TITLE_MSG_EMAIL_PASSWORD_RECOVERY
            body = UserTokenEncryptinoService.hash_email_with_date(email)
            EmailService.send(email=email, body=body, header=header)
            return True, Config.USER_FOUND


    def verify_password_recovery(self, request):
        if request.is_json:
            email = request.json['email']
            entered_token = request.json['token']
        else:
            email = request.form['email']
            entered_token = request.form['token']
        user = UserProvider.get_user_from_db_by_email(email)
        if user:
            if UserTokenEncryptinoService.verify_hash_email_with_date(email, entered_token):
                return user, Config.VERIFY_HASH_EMAIL_WITH_DATE_SUCCESS
            else:
                return None, Config.VERIFY_HASH_EMAIL_WITH_DATE_FAILED
        return None, Config.USER_FOUND

    def change_password(self, request, user_id):
        if request.is_json:
            enteredPassword = request.json['password']
        else:
            enteredPassword = request.form['password']
        user = UserProvider.get_user_from_db_by_id(user_id)
        if password_is_copy_of_history(user, enteredPassword):
            return False, Config.PASSWORD_IS_COPY_OF_HISTORY
        else:
            password_encrypt = PasswordEncryption.hash_salt(password=enteredPassword, salt=None)
            user.password = password_encrypt
            if DAL.save_new_user_to_db(user) and DAL.save_user_password_history_to_db(user):
                return True, Config.PASSWORD_CHANGE_SUCCESS
            else:
                return False, Config.PASSWORD_CHANGE_FAILED



