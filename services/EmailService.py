from flask_mail import Message
from application import mail
from config import Config

def send(email, body, header=None):
    if header is None:
        header = Config.TITLE_MSG_EMAIL_DEFAULT
    msg = Message(header, recipients=[email])
    msg.body = body
    mail.send(msg)