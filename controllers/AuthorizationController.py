
from flask_jwt_extended import create_access_token, create_refresh_token

from services.DAL import DAL, UserProvider
from services.PasswordVerifier import verify_user_password


class AuthorizationController():
    def Login(self, request):
        if request.is_json:
            email = request.json['email']
            enteredPassword = request.json['password']
        else:
            email = request.form['email']
            enteredPassword = request.form['password']
        user = UserProvider.get_user_from_db_by_email(email)
        if verify_user_password(user, enteredPassword):
            return user
        else:
            return None


