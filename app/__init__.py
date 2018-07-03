from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

def create_app(config_name):

    app = Flask(__name__)


        # app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name]


    # Registering the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    configure(app)

    return app
