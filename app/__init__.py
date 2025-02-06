from flask import Flask
from .db import db
from flask_swagger_ui import get_swaggerui_blueprint

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swagger_bp = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Flask API"
        }
    )
    app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)
    return app