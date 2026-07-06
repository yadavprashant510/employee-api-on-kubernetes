from flask import Flask, request

from app.errors import register_error_handlers
from app.health import health_bp
from app.logger import get_logger
from app.routes import employee_bp
from app.middleware import register_middlewares

logger = get_logger(__name__)


def create_app():
    app = Flask(__name__)

    register_middlewares(app)
    app.register_blueprint(employee_bp)
    app.register_blueprint(health_bp)
    register_error_handlers(app)

    @app.before_request
    def log_request():
        logger.info("%s %s", request.method, request.path)

    return app
