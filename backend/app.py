import os
from flask import Flask
from controller.user import app_user
from controller.blog import app_blog
from controller.disk import app_disk
from flask_cors import *
from model.extensions import mail


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config['MAIL_SERVER'] = 'smtp.qq.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USERNAME'] = '3588034273@qq.com'
    app.config['MAIL_PASSWORD'] = 'wmxbvgdcdqiqchhj'
    app.config['MAIL_DEFAULT_SENDER'] = '3588034273@qq.com'
    mail.init_app(app)
    app.register_blueprint(app_user)
    app.register_blueprint(app_blog)
    app.register_blueprint(app_disk)
    CORS(app, supports_credentials=True)
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app