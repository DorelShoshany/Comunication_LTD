
from config import Config
from models.AuthorizationResult import AuthorizationResult
from services import  UserTokenEncryptinoService, PasswordEncryption
from services.AuthorizationService import start_login_process, was_password_used_in_the_last_given_occurrences, \
    start_password_recovery_process, start_verify_password_and_token, start_change_password
from services.Validators import password_is_valid, form_is_full, valid_email


class AuthorizationController():

    def login(self, request):
        login_form = request.json if request.is_json else request.form
        login_dict = dict(login_form)
        login_fields = ['email','password']
        login_res= form_is_full(login_dict, login_fields)
        if login_res.isSuccess:
            return start_login_process(login_dict['email'], login_dict['password'])
        else:
            return None,login_res

    # POST: This will generate a token and send to the user email in order
    def password_recovery(self, request):
        forget_password_form = request.json if request.is_json else request.form
        forget_password_dict = dict(forget_password_form)
        forget_password_form_fields = ["email"]
        forget_password_form_res = form_is_full(forget_password_dict, forget_password_form_fields)
        if forget_password_form_res.isSuccess:
            return start_password_recovery_process(forget_password_dict.get("email"))
        else:
            return forget_password_form_res

    def verify_password_and_token(self, request):
        verify_password_recovery_form = request.json if request.is_json else request.form
        verify_password_recovery_form_fields = ["email",'token']
        verify_password_recovery_dict = dict(verify_password_recovery_form)
        verify_form_res = form_is_full(verify_password_recovery_dict, verify_password_recovery_form_fields)
        if verify_form_res.isSuccess:
            return start_verify_password_and_token(verify_password_recovery_dict)
        else:
            return None, verify_form_res

    def change_password(self, request, user_id):
        change_password_form = request.json if request.is_json else request.form
        change_password_form_fields = ['password']
        change_password_dict = dict(change_password_form)
        change_password_form_res = form_is_full(change_password_dict, change_password_form_fields)
        if change_password_form_res.isSuccess:
            return start_change_password(user_id, change_password_dict)
        else:
            return change_password_form_res





