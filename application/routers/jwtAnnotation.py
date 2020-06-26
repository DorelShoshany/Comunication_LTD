import datetime
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity, set_access_cookies\
    , unset_jwt_cookies, unset_access_cookies
from config import Config
from application import app, jwt
from flask import jsonify, make_response, redirect
roles = Config.ROLE


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


def unset_jwt():
    resp = make_response(redirect(app.config['BASE_URL'] + '/', 302))
    unset_jwt_cookies(resp)
    return resp


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    # No auth header
    return jsonify(Config.MSG_FOR_ROLE_REQUIRED), 400  # redirect(app.config['BASE_URL'] + '/login', 302)


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
