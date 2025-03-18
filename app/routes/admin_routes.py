from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Profile, TermWithdrawalRequest, db

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/admin')
def admin():
    profiles = Profile.query.all()
    return render_template('adminpage.html', profiles=profiles)

@admin_routes.route('/active/<int:id>')
def activate(id):
    profile = Profile.query.get(id)
    if profile is None:
        return redirect('/ap')
    profile.active = not profile.active
    db.session.commit()
    return redirect('/ap')

@admin_routes.route('/ap')
def ap():
    profiles = Profile.query.all()
    return render_template('adminpage.html', profiles=profiles)

@admin_routes.route('/priv/<int:id>')
def change_privileges(id):
    data = Profile.query.get(id)
    if data is None:
        return redirect('/ap')
    if data.privilages_ == "user":
        data.privilages_ = "admin"
    else:
        data.privilages_ = "user"
    db.session.commit()
    return redirect('/ap')

@admin_routes.route('/delete/<int:id>')
def erase(id):
    data = Profile.query.get(id)
    if data:
        db.session.delete(data)
        db.session.commit()
    return redirect('/ap')
