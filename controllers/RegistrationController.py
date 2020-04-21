from entities.User import User
from services import PasswordEncryptor
from services.DAL import DAL
from services.Validators import user_is_valid, password_is_valid, sector_id_is_valid


class RegistrationController():
    def Register(self, request):
        if request.is_json:
            firstName = request.json['firstName']
            lastName = request.json['lastName']
            email = request.json['email']
            password = request.json['password']
            sectorId = request.json['sectorId']
        else:
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            email = request.form['email']
            password = request.form['password']
            sectorId = request.form['sectorId']
        user = User(firstName=firstName, lastName=lastName, email=email, password=password, sectorId=sectorId)
        if user_is_valid(user) and password_is_valid(user.password) and sector_id_is_valid(user.sectorId):
            password_encrypt = PasswordEncryptor.hash_salt(password=password, salt=None)
            user.password=password_encrypt
            return DAL.save_new_user_to_db(user)
        else:
            return False