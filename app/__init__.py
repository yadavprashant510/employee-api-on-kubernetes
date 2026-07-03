from flask import Flask

from app.health import health_bp
from app.routes import employee_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(employee_bp)
    app.register_blueprint(health_bp)

    return app
