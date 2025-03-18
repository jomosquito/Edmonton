from flask import Blueprint, redirect, url_for, request
from O365 import Account
import json
from .. import my_db

oauth_routes = Blueprint('oauth_routes', __name__)

@oauth_routes.route('/stepone')
def auth_step_one():
    callback = url_for('oauth_routes.auth_step_two_callback', _external=True).replace("127.0.0.1", "localhost")
    account = Account(credentials)
    url, flow = account.con.get_authorization_url(requested_scopes=scopes, redirect_uri=callback)
    my_db.store_flow(serialize(flow))
    return redirect(url)

@oauth_routes.route('/steptwo')
def auth_step_two_callback():
    account = Account(credentials)
    my_saved_flow_str = my_db.get_flow()
    if not my_saved_flow_str:
        return "Flow state not found. Restart authentication.", 400
    my_saved_flow = deserialize(my_saved_flow_str)
    requested_url = request.url
    result = account.con.request_token(requested_url, flow=my_saved_flow)
    email, idtoken = open1()
    if result:
        profile = Profile.query.order_by(Profile.id.desc()).first()
        if profile:
            profile.email_ = email
            profile.usertokenid = idtoken
            db.session.commit()
        return redirect('/')
    return "Authentication failed", 400
