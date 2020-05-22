import ast
import datetime
from functools import wraps
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity, set_access_cookies, \
    jwt_required, unset_jwt_cookies, unset_access_cookies, fresh_jwt_required, verify_jwt_in_request, get_jwt_claims

from config import Config
from controllers.AuthorizationController import AuthorizationController
from controllers.PackagesController import PackagesController
from controllers.PackagesSectorController import *

from controllers.RegistrationController import RegistrationController
from controllers.SectorController import SectorController
from application import app, jwt
from flask import render_template, request, Response, json, jsonify, make_response, redirect, session

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


@app.route("/api/changePassword", methods=["POST"])
@change_password_role_required
def api_change_password():
    user_id = get_user_id_from_identity(get_jwt_identity())
    authorizationController = AuthorizationController()
    authorizationResult = authorizationController.change_password(request, user_id)
    if authorizationResult.isSuccess:
        # remove access_token_password form the browser:
        resp = jsonify({'Password changed successfully': True})
        resp.set_cookie('access_token_password', "", expires=0)
        set_access_cookies(resp, "")
        return resp, 200
    else:
        return jsonify(authorizationResult.Message), 401


@app.route("/api/passwordRecovery", methods=["POST"])
def api_password_recovery():
    authorizationController = AuthorizationController()
    user, authorizationResult = authorizationController.verify_password_and_token(request)
    if authorizationResult.isSuccess and user is not None:
        expires = datetime.timedelta(days=Config.TIME_EXPIRES_ACCESS_TOKENS_ROLE_BASIC)
        access_token = create_access_token(identity=json.dumps({"user": user.id, roles: Config.ROLE_CHANGE_PASSWORD}),
                                           expires_delta=expires)
        resp = jsonify({'passwordRecovery': True})
        resp.set_cookie('access_token_password', access_token)
        set_access_cookies(resp, access_token)
        return resp, 200
    else:
        return jsonify(authorizationResult.Message), 404


@app.route("/api/forgotYourPassword", methods=["POST"])
def api_forgot_your_password():
    authorizationController = AuthorizationController()
    authorizationResult = authorizationController.password_recovery(request)
    if authorizationResult.isSuccess:
        return json.dumps({"msg": "email send successfully"}), 200
    else:
        return jsonify(authorizationResult.Message), 404


def get_user_id_from_identity(jwt_identity):
    dict_identity = ast.literal_eval(jwt_identity)
    return dict_identity['user']


@app.route("/api/packagesOfferings", methods=["GET"])
@jwt_required
@basic_role_required
def api_get_packages_to_buy():
    user_id = get_user_id_from_identity(get_jwt_identity())
    packagesSectorController = PackagesSectorController()
    res = packagesSectorController.get_all_packages_to_buy_by_sector_id(user_id)
    return json.dumps(res), 200


@app.route("/api/buypackage", methods=["POST"])
@jwt_required
@basic_role_required
def api_buy_package():
    user_id = get_user_id_from_identity(get_jwt_identity())
    packagesSectorController = PackagesSectorController()
    if packagesSectorController.add_purchase_to_user(user_id=user_id, request=request):
        return jsonify("Buy package success. "), 200
    else:
        return jsonify("Buy package failed. "), 400


@app.route("/api/yourPackages", methods=["GET"])
@jwt_required
@basic_role_required
def api_your_packages():
    user_id = get_user_id_from_identity(get_jwt_identity())
    packagesSectorController = PackagesSectorController()
    res = packagesSectorController.get_all_packages_that_user_purchases(user_id)
    return json.dumps(res), 200


@app.route("/api/register", methods=['POST'])
def api_register():
    registrationController = RegistrationController()
    res = registrationController.register(request)
    if res.isSuccess:
        return jsonify(res.Message), 201
    else:
        resp = jsonify(res.Message)
        return resp, 400


# TODO: only user as admin
@app.route("/api/addSector", methods=['POST'])
def add_sector():
    sectorController = SectorController()
    res = sectorController.create_sector(request)
    if res:
        return jsonify(message="Sector created successfully. "), 201
    else:
        return jsonify(message="Sector created failed"), 201


@app.route("/api/getSectors", methods=['GET'])
def get_sectors():
    sectorController = SectorController()
    sectors = sectorController.get_all_sectors()
    return jsonify(sectors), 200


# TODO: only user as admin
@app.route("/api/addPackage", methods=['POST'])
def add_package():
    packagesController = PackagesController()
    res = packagesController.create_packages(request)
    if res:
        return jsonify("Package created successfully. "), 201
    else:
        return jsonify("Package created failed. "), 400


# TODO: only user as admin
@app.route("/api/addPackagesSector", methods=['POST'])
def addPackagesSector():
    packagesSectorController = PackagesSectorController()
    res = packagesSectorController.create_packages_sector(request)
    if res:
        return jsonify("Packages for Sector created successfully. "), 200
    else:
        return jsonify("Packages for Sector failed to create . "), 400


@app.route("/api/login", methods=['POST'])
def login():
    authorizationController = AuthorizationController()
    user, authorizationResult = authorizationController.login(request)
    if authorizationResult.isSuccess:
        # resp = assign_access_refresh_tokens(json.dumps({"user" : user.id , roles: Config.ROLE_BASIC})
        #                                  , app.config['BASE_URL'] + '/yourPackages')
        expires = datetime.timedelta(days=Config.TIME_EXPIRES_ACCESS_TOKENS_ROLE_BASIC)
        access_token = create_access_token(identity=json.dumps({"user": user.id, roles: Config.ROLE_BASIC}),
                                           expires_delta=expires)
        resp = jsonify({'login': True})
        resp.set_cookie('access_token', access_token, expires)
        set_access_cookies(resp, access_token)
        return resp, 200
    else:
        return jsonify(authorizationResult.Message), 404


# tokens func:


def assign_access_refresh_tokens(user, url):
    expires = datetime.timedelta(days=Config.TIME_EXPIRES_ACCESS_TOKENS_ROLE_BASIC)
    access_token = create_access_token(identity=user, expires_delta=expires)
    resp = make_response(redirect(url, 302))
    set_access_cookies(resp, access_token)
    return resp


@jwt.expired_token_loader
def my_expired_token_callback(expired_token):
    token_type = expired_token['type']
    return jsonify({
       'status': 401,
      'sub_status': 42,
     'msg': 'The {} token has expired'.format(token_type)
     }), 401
    #return redirect(app.config['BASE_URL'] + '/login', 302)


@app.route('/token/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh():
    # Refreshing expired Access token
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=str(user_id))
    resp = make_response(redirect(app.config['BASE_URL'] + '/', 302))
    set_access_cookies(resp, access_token)
    return resp


@app.route('/api/logout', methods=['GET'])
@jwt_required
@basic_role_required
def logout():
    resp = jsonify({'logout': True})
    # Remove the access_token form the browser
    resp.set_cookie('access_token', "", expires=0)
    set_access_cookies(resp, "")
    return resp, 200


def unset_jwt():
    resp = make_response(redirect(app.config['BASE_URL'] + '/', 302))
    unset_jwt_cookies(resp)
    return resp


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    # No auth header
    return jsonify("unauthorized_callback"), 400  # redirect(app.config['BASE_URL'] + '/login', 302)


@jwt.invalid_token_loader
def invalid_token_callback(callback):
    # Invalid Fresh/Non-Fresh Access token in auth header
    resp = jsonify({Config.MSG_FOR_ROLE_REQUIRED: True})
    unset_jwt_cookies(resp)
    return resp, 302


@jwt.expired_token_loader
def expired_token_callback(callback):
    # Expired auth header
    resp = jsonify({Config.MSG_FOR_ROLE_REQUIRED: True})
    # resp = make_response(redirect(app.config['BASE_URL'] + '/token/refresh'))
    unset_access_cookies(resp)
    return resp, 302
