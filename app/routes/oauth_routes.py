from flask import Blueprint, render_template, request, redirect, url_for, session
from ..models import Profile, db

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/userhompage')
def user_home():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth_routes.login'))
    user = Profile.query.get(user_id)
    return render_template('userhompage.html', user=user)

@user_routes.route('/settings', methods=['GET', 'POST'])
def settings():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth_routes.login'))
    user = Profile.query.get(user_id)
    if request.method == 'POST':
        new_email = request.form.get("email")
        if new_email:
            user.email_ = new_email
            db.session.commit()
        return redirect(url_for('user_routes.settings'))
    return render_template('settings.html', user=user)

@user_routes.route('/reports')
def reports():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth_routes.login'))
    user = Profile.query.get(user_id)
    return render_template('reports.html', user=user)
