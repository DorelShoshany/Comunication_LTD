from entities.User import User
from services.DAL import DAL


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
        DAL.save_new_user_to_db(user)