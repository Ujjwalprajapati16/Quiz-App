from flask import Flask, flash, redirect, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required
import os
from sqlalchemy import MetaData,func

load_dotenv()

metadata = MetaData(
    naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
    }
)

db=SQLAlchemy(metadata=metadata)

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    
    # set up file upload folder
    app.config['UPLOAD_FOLDER'] = 'static/uploads/'
    
    # change databse what we use
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    
    app.secret_key = os.getenv('SECRET_KEY')
    
    db.init_app(app)
    migrate = Migrate(app, db)
    bcrypt = Bcrypt(app) # for hasing the password
    
    # login manager
    login_manager = LoginManager(app)
    login_manager.init_app(app)
    
    # models
    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @login_manager.unauthorized_handler
    def unauthorized():
        flash('You need to login first.', 'warning')
        return redirect(url_for('login'))

    # routes
    from routes.auth_routes import auth_routes
    from routes.questions_routes import questions_routes
    
    auth_routes(app, db, bcrypt)
    questions_routes(app, db)
    
    return app