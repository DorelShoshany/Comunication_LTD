from application.routers import packagesSectorController, packagesController
from application import app
from flask import request, json
from services.jwtServices import *

roles = Config.ROLE


@app.route("/api/packagesOfferings", methods=["GET"])
@jwt_required
@basic_role_required
def api_get_packages_to_buy():
    user_id = get_user_id_from_identity(get_jwt_identity())
    res = packagesSectorController.get_all_packages_to_buy_by_sector_id(user_id)
    return json.dumps(res), 200


@app.route("/api/buypackage", methods=["POST"])
@jwt_required
@basic_role_required
def api_buy_package():
    user_id = get_user_id_from_identity(get_jwt_identity())
    if packagesSectorController.add_purchase_to_user(user_id=user_id, request=request):
        return jsonify("Buy package success. "), 200
    else:
        return jsonify("Buy package failed. "), 400


@app.route("/api/yourPackages", methods=["GET"])
@jwt_required
@basic_role_required
def api_your_packages():
    user_id = get_user_id_from_identity(get_jwt_identity())
    res = packagesSectorController.get_all_packages_that_user_purchases(user_id)
    return json.dumps(res), 200


# TODO: only user as admin
@app.route("/api/addPackagesSector", methods=['POST'])
def addPackagesSector():
    res = packagesSectorController.create_packages_sector(request)
    if res:
        return jsonify("Packages for Sector created successfully. "), 200
    else:
        return jsonify("Packages for Sector failed to create . "), 400


# TODO: only user as admin
@app.route("/api/addPackage", methods=['POST'])
def add_package():
    res = packagesController.create_packages(request)
    if res:
        return jsonify("Package created successfully. "), 201
    else:
        return jsonify("Package created failed. "), 400