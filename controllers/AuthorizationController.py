from flask_jwt_extended import create_access_token

from services.DAL import DAL


class AuthorizationController():
    def Login(self, request):
        if request.is_json:
            email = request.json['email']
            password = request.json['password']
        else:
            email = request.form['email']
            password = request.form['password']
        user = DAL.get_user_from_db(email, password)
        if user:
            return create_access_token(identity=email)
        else:
            return None


