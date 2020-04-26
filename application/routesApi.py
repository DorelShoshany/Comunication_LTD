import ast
import datetime
from functools import wraps
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity, set_access_cookies, \
    jwt_required, unset_jwt_cookies, unset_access_cookies, fresh_jwt_required, verify_jwt_in_request, get_jwt_claims

from config import Config
from controllers.AuthorizationController import AuthorizationController
from controllers.PackagesController import PackagesController
from controllers.PackagesSectorController import PackagesSectorController
from controllers.RegistrationController import RegistrationController
from controllers.SectorController import SectorController
from application import app, jwt
from flask import render_template, request, Response, json, jsonify, make_response, redirect

#TODO: change all 404,200 to enum

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
        #print(claims)
        #print(type(claims))
        #print(claims['roles'] == Config.ROLE_CHANGE_PASSWORD)
        if claims[roles] != Config.ROLE_CHANGE_PASSWORD:
            return jsonify(msg="can't continue without login!"), 403
        else:
            return fn(*args, **kwargs)
    return wrapper

def basic_role_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        #print(claims)
        #print(type(claims))
        #print(claims['roles'] == Config.ROLE_CHANGE_PASSWORD)
        if claims[roles] == Config.ROLE_CHANGE_PASSWORD:
            return jsonify(msg="can't continue without login!"), 403
        else:
            return fn(*args, **kwargs)
    return wrapper


@app.route("/api/changePassword", methods=["POST"])
@change_password_role_required
def api_changePassword():
    dict_identity = ast.literal_eval(get_jwt_identity())
    user_id = dict_identity['user']
    authorizationController = AuthorizationController()
    authorizationResult = authorizationController.change_password(request, user_id)
    if authorizationResult.isSuccess:
        return make_response(redirect(app.config['BASE_URL'] + '/', 302))
    else:
        return jsonify(message=authorizationResult.Message), 401


@app.route("/api/passwordRecovery", methods=["POST"])
def api_passwordRecovery():
    authorizationController = AuthorizationController()
    user, authorizationResult = authorizationController.verify_password_recovery(request)
    if authorizationResult.isSuccess:
        return assign_access_refresh_tokens(json.dumps({"user" : user.id , roles: Config.ROLE_CHANGE_PASSWORD}),
                                            app.config['BASE_URL'] + '/changePassword')
    else:
        return jsonify(message=authorizationResult.Message), 404


@app.route("/api/forgotYourPassword", methods=["POST"])
def api_forgot_your_password():
    authorizationController = AuthorizationController()
    authorizationResult = authorizationController.password_recovery(request)
    if authorizationResult.isSuccess:
        return make_response(redirect(app.config['BASE_URL'] + '/passwordRecovery', 302))
    else:
        return jsonify(message=authorizationResult.Message), 404


@app.route("/api/packagesOfferings", methods=["GET"])
@jwt_required
@basic_role_required
def api_get_packages_to_buy():
    user_id = get_jwt_identity()
    packagesSectorController = PackagesSectorController()
    res = packagesSectorController.get_all_packages_to_buy_by_sector_id(user_id)
    return jsonify(res), 200


@app.route("/api/register", methods=['POST'])
def api_register():
    registrationController = RegistrationController()
    if registrationController.Register(request):
        return jsonify(message="User created successfully. "), 201
    else:
        return jsonify(message="User created failed. "), 400


#TODO: only user as admin
@app.route("/api/addSector", methods=['POST'])
def add_sector():
    sectorController = SectorController()
    sectorController.createSector(request)
    return jsonify(message="Sector created successfully. "), 201


#TODO: only user as admin
@app.route("/api/addPackage", methods=['POST'])
def add_package():
    packagesController = PackagesController()
    packagesController.createPackages(request)
    return jsonify(message="Package created successfully. "), 201

#TODO: only user as admin
@app.route("/api/addPackagesSector", methods=['POST'])
def addPackagesSector():
    packagesSectorController = PackagesSectorController()
    packagesSectorController.createPackagesSector(request)
    return jsonify(message="Packages for Sector created successfully. "), 201


@app.route("/api/login", methods=['POST'])
def api_login():
    authorizationController = AuthorizationController()
    user, authorizationResult = authorizationController.login(request)
    if authorizationResult.isSuccess:
        return assign_access_refresh_tokens(json.dumps({"user" : user.id , roles: Config.ROLE_BASIC})
                                            , app.config['BASE_URL'] + '/yourPackages')
    else:
        return jsonify(message=authorizationResult.Message), 404


@app.route("/api/yourPackages")
@jwt_required
@basic_role_required
def api_yourPackages():
    return "yourPackages", 200 #render_template("yourPackages.html")


# tokens func:
def assign_access_refresh_tokens(user, url):
    expires = datetime.timedelta(days=Config.DAYS_EXPIRES_ACCESS_TOKENS_ROLE_BASIC)
    access_token = create_access_token(identity=user,expires_delta=expires)
    resp = make_response(redirect(url, 302))
    set_access_cookies(resp, access_token)
    return resp


@jwt.expired_token_loader
def my_expired_token_callback(expired_token):
    token_type = expired_token['type']
    #return jsonify({
     #   'status': 401,
      #  'sub_status': 42,
       # 'msg': 'The {} token has expired'.format(token_type)
    #}), 401
    return redirect(app.config['BASE_URL'] + '/login', 302)

@app.route('/token/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh():
    # Refreshing expired Access token
    user_id = get_jwt_identity()
    access_token = create_access_token(identity=str(user_id))
    resp = make_response(redirect(app.config['BASE_URL'] + '/', 302))
    set_access_cookies(resp, access_token)
    return resp


@app.route('/logout', methods=['GET'])
@jwt_required
@basic_role_required
def logout():
    # Revoke Fresh/Non-fresh Access and Refresh tokens
    return unset_jwt(), 302


def unset_jwt():
    resp = make_response(redirect(app.config['BASE_URL'] + '/', 302))
    unset_jwt_cookies(resp)
    return resp


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    # No auth header
    return redirect(app.config['BASE_URL'] + '/login', 302)


@jwt.invalid_token_loader
def invalid_token_callback(callback):
    # Invalid Fresh/Non-Fresh Access token in auth header
    resp = make_response(redirect(app.config['BASE_URL'] + '/signup'))
    unset_jwt_cookies(resp)
    return resp, 302


@jwt.expired_token_loader
def expired_token_callback(callback):
    # Expired auth header
    resp = make_response(redirect(app.config['BASE_URL'] + '/token/refresh'))
    unset_access_cookies(resp)
    return resp, 302


