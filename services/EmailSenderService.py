from flask_mail import Message
from application import mail
from config import Config


def send_password_recovery(email):
    msg = Message(Config.TITLE_MSG_EMAIL, recipients=[email])
    msg.body = "testing"
    mail.send(msg)