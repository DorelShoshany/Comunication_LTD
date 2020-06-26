from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity, set_access_cookies, \
    jwt_required, unset_jwt_cookies, unset_access_cookies, fresh_jwt_required, verify_jwt_in_request, get_jwt_claims
from config import Config
from application import  jwt
import ast
from functools import wraps

roles = Config.ROLE


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    if Config.ROLE_CHANGE_PASSWORD in identity:
        return {roles: Config.ROLE_CHANGE_PASSWORD}
    else:
        return {roles: Config.ROLE_BASIC}


def change_password_role_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims[roles] != Config.ROLE_CHANGE_PASSWORD:
            return jsonify(Config.MSG_FOR_ROLE_REQUIRED), 403
        else:
            return fn(*args, **kwargs)

    return wrapper


def basic_role_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims[roles] == Config.ROLE_CHANGE_PASSWORD:
            return jsonify(Config.MSG_FOR_ROLE_REQUIRED), 403
        else:
            return fn(*args, **kwargs)

    return wrapper


def get_user_id_from_identity(jwt_identity):
    dict_identity = ast.literal_eval(jwt_identity)
    return dict_identity['user']


