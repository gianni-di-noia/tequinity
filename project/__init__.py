from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads

# init SQLAlchemy so we can use itlater in our models
db = SQLAlchemy()
receipts = UploadSet("receipts", IMAGES)


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "9OLWxND4o83j4K4iuopO"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["UPLOADED_RECEIPTS_DEST"] = "/tmp/receipts"

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    configure_uploads(app, (receipts,))
    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
