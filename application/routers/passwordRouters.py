import datetime
from application.routers import authorizationController
from application import app
from flask import request, json
from services.jwtServices import *

roles = Config.ROLE


@app.route("/api/changePassword", methods=["POST"])
@change_password_role_required
def api_change_password():
    user_id = get_user_id_from_identity(get_jwt_identity())
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
    authorizationResult = authorizationController.password_recovery(request)
    if authorizationResult.isSuccess:
        return json.dumps({"msg": "email send successfully"}), 200
    else:
        return jsonify(authorizationResult.Message), 404