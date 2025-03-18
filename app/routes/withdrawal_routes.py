from flask import Blueprint, render_template, request, redirect, url_for, session
from ..models import TermWithdrawalRequest, db, Profile

withdrawal_routes = Blueprint('withdrawal_routes', __name__)

@withdrawal_routes.route('/Termdroprequest', methods=['POST'])
def term_withdraw_request():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth_routes.login'))
    user = Profile.query.get(user_id)
    reason = request.form.get("reason")
    if not reason:
        return "No reason selected", 400
    new_request = TermWithdrawalRequest(user_id=user.id, reason=reason)
    db.session.add(new_request)
    db.session.commit()
    return redirect(url_for('user_routes.settings'))

@withdrawal_routes.route('/approvals')
def approvals():
    pending_requests = TermWithdrawalRequest.query.filter_by(status='pending').all()
    return render_template('admin_notifications.html', pending_requests=pending_requests)

@withdrawal_routes.route('/approve_request/<int:request_id>', methods=['POST'])
def approve_request(request_id):
    request = TermWithdrawalRequest.query.get(request_id)
    if request:
        request.status = 'approved'
        db.session.commit()
    return redirect(url_for('withdrawal_routes.notification'))

@withdrawal_routes.route('/reject_request/<int:request_id>', methods=['POST'])
def reject_request(request_id):
    request = TermWithdrawalRequest.query.get(request_id)
    if request:
        request.status = 'rejected'
        db.session.commit()
    return redirect(url_for('withdrawal_routes.notification'))
