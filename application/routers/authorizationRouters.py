import datetime
from application.routers import *
from application import app
from flask import request, json
from services.jwtServices import *

roles = Config.ROLE


@app.route("/api/register", methods=['POST'])
def api_register():
    res = registrationController.register_new_user(request)
    if res.isSuccess:
        return jsonify(res.Message), 201
    else:
        resp = jsonify(res.Message)
        return resp, 400


@app.route("/api/login", methods=['POST'])
def login():
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


@app.route('/api/logout', methods=['GET'])
@jwt_required
@basic_role_required
def logout():
    resp = jsonify({'logout': True})
    # Remove the access_token form the browser
    resp.set_cookie('access_token', "", expires=0)
    set_access_cookies(resp, "")
    return resp, 200