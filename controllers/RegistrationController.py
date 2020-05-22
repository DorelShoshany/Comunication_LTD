import os

from entities.User import User
from models.AuthorizationResult import AuthorizationResult

from services import PasswordEncryption
from services.DAL import DAL
from services.Validators import user_is_valid, password_is_valid, sector_id_is_valid, form_is_full


class RegistrationController():

    def register(self, request):
        register_form = request.json if request.is_json else request.form
        register_dict = dict(register_form)
        form_register_fields = ["firstName", 'lastName', 'email', 'password', 'sectorId']
        form_valid_res = form_is_full(register_dict, form_register_fields)

        if form_valid_res.isSuccess:
            firstName = register_dict["firstName"]
            lastName = register_dict['lastName']
            email = register_dict['email']
            password = register_dict['password']
            sectorId = register_dict['sectorId']

            user = User(firstName=firstName, lastName=lastName, email=email, password=password, sectorId=sectorId)

            if user_is_valid(user).isSuccess:
                if password_is_valid(user.password).isSuccess:
                    if sector_id_is_valid(user.sectorId).isSuccess:
                        password_encrypt = PasswordEncryption.hash_salt(password=password, salt=None)
                        user.password = password_encrypt
                        if DAL.save_new_user_to_db(user) and DAL.save_user_password_history_to_db(user):
                            return AuthorizationResult(isSuccess=True, Message="User created successfully. ")
                    else:
                        return sector_id_is_valid(user.sectorId)
                else:
                    return password_is_valid(user.password)
            else:
                return AuthorizationResult(isSuccess=False, Message="User created failed. ")
        else:
            return form_valid_res