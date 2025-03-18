from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from config import client_secret, client_id
import json

# Microsoft OAuth Credentials
credentials = (client_id, client_secret)
scopes = ['Mail.ReadWrite', 'Mail.Send', 'email']

# Simple in-memory database for OAuth flows
class MyDB:
    def __init__(self):
        self.storage = {}

    def store_flow(self, flow):
        self.storage['flow'] = flow

    def get_flow(self):
        return self.storage.get('flow')

my_db = MyDB()

def serialize(flow):
    return json.dumps(flow)

def deserialize(flow_str):
    return json.loads(flow_str)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=True)
    active = db.Column(db.Boolean, default=True, nullable=True)
    pass_word = db.Column(db.String(200), nullable=False)
    privilages_ = db.Column(db.String(20), default='user')
    email_ = db.Column(db.String(100), nullable=True)
    usertokenid = db.Column(db.String(100), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    phoneN_ = db.Column(db.String(200), nullable=True)
    address = db.Column(db.String(200), nullable=True)
    enroll_status = db.Column(db.String(200), nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.pass_word = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pass_word, password)

class TermWithdrawalRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    reason = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('Profile', backref='withdrawal_requests')

    @property
    def request_type(self):
        return "Term Withdrawal"

    @property
    def details(self):
        return f"Reason: {self.reason}"
