

from flask_mail import Message

from services.DAL import DAL, UserProvider
from services.PasswordVerifier import verify_user_password


class AuthorizationController():

    def login(self, request):
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

    # POST: This will generate a token and send to the user email in order
    def start_password_recovery(self, request):
        if request.is_json:
            email = request.json['email']
        else:
            email = request.form['email']
        #TODO: find if the user is exist in the DB -> if he is -> send emaiil
        msg = Message("Hello", recipients=[email])
        msg.body = "testing"
        return msg



