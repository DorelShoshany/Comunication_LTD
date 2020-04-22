from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity, set_access_cookies, \
    jwt_required, unset_jwt_cookies, unset_access_cookies, fresh_jwt_required

from controllers.AuthorizationController import AuthorizationController
from controllers.PackagesController import PackagesController
from controllers.PackagesSectorController import PackagesSectorController
from controllers.RegistrationController import RegistrationController
from controllers.SectorController import SectorController

from application import app, jwt
from flask import render_template, request, Response, json, jsonify, make_response, redirect


@app.route("/api/packages" , methods=["GET"])
@jwt_required
def api_get_packages_to_buy():
    user_id = get_jwt_identity()
    print(user_id)
    #packagesSectorController = PackagesSectorController()
    #res = packagesSectorController.get_all_packages_to_buy_by_sector_id(user_id)
    return "dorel" , 200#jsonify(res), 200


@app.route("/api/register", methods=['POST'])
def api_register():
    registrationController = RegistrationController()
    if registrationController.Register(request) == True:
        return jsonify(message="user created successfully. "), 201
    else:
        return jsonify(message="user created failed. "), 400


#TODO: only user as admin
@app.route("/api/addSector", methods=['POST'])
def add_sector():
    sectorController = SectorController()
    sectorController.createSector(request)
    return jsonify(message="sector created successfully. "), 201


#TODO: only user as admin
@app.route("/api/addPackage", methods=['POST'])
def add_package():
    packagesController = PackagesController()
    packagesController.createPackages(request)
    return jsonify(message="package created successfully. "), 201

#TODO: only user as admin
@app.route("/api/addPackagesSector", methods=['POST'])
def addPackagesSector():
    packagesSectorController = PackagesSectorController()
    packagesSectorController.createPackagesSector(request)
    return jsonify(message="Packages for Sector created successfully. "), 201

@app.route("/api/login", methods=['POST'])
def api_login():
    authorizationController = AuthorizationController()
    user = authorizationController.Login(request)
    if user:
        #at = create_access_token(identity=user.email)
        return assign_access_refresh_tokens(user , app.config['BASE_URL'] + '/yourPurchases') #jsonify(message="Login succeed!", access_token=at)
    else:
        return jsonify(message="Login failed!, bad email or password"), 401


@app.route("/api/yourPurchases")
@fresh_jwt_required
def api_your_purchases():
    return render_template("yourPurchases.html")



# tokens func:
def assign_access_refresh_tokens(user_id, url):
    access_token = create_access_token(identity=str(user_id))
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