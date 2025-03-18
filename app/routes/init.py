from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    
    db.init_app(app)
    
    from .routes.auth_routes import auth_routes
    from .routes.admin_routes import admin_routes
    from .routes.user_routes import user_routes
    from .routes.oauth_routes import oauth_routes
    from .routes.withdrawal_routes import withdrawal_routes
    
    app.register_blueprint(auth_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(oauth_routes)
    app.register_blueprint(withdrawal_routes)
    
    return app
