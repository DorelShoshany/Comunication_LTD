from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity, set_access_cookies, \
    jwt_required, unset_jwt_cookies, unset_access_cookies, fresh_jwt_required


from controllers.AuthorizationController import AuthorizationController
from controllers.PackagesController import PackagesController
from controllers.PackagesSectorController import PackagesSectorController
from controllers.RegistrationController import RegistrationController
from controllers.SectorController import SectorController

from application import app, jwt, mail
from flask import render_template, request, Response, json, jsonify, make_response, redirect

@app.route("/api/forgotYourPassword", methods=["POST"])
def api_forgot_your_password():
    authorizationController = AuthorizationController()
    msg = authorizationController.start_password_recovery(request)
    mail.send(msg)
    return "dorel" , 200


@app.route("/api/packagesOfferings" , methods=["GET"])
@jwt_required
def api_get_packages_to_buy():
    user_id = get_jwt_identity()
    packagesSectorController = PackagesSectorController()
    res = packagesSectorController.get_all_packages_to_buy_by_sector_id(user_id)
    return jsonify(res), 200


@app.route("/api/register", methods=['POST'])
def api_register():
    registrationController = RegistrationController()
    if registrationController.Register(request) == True:
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
    user = authorizationController.login(request)
    if user:
        return assign_access_refresh_tokens(user.id, app.config['BASE_URL'] + '/yourPackages') #jsonify(message="Login succeed!", access_token=at)
    else:
        return jsonify(message="Login failed!, bad email or password"), 401


@app.route("/api/yourPackages")
@jwt_required
def api_yourPackages():
    return "yourPackages",200 #render_template("yourPackages.html")


# tokens func:
def assign_access_refresh_tokens(user, url):
    access_token = create_access_token(identity=user)
    resp = make_response(redirect(url, 302))
    set_access_cookies(resp, access_token)
    return resp


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