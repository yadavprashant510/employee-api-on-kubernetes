import time

from flask import Blueprint, jsonify

from app.config import Config
from flasgger import swag_from

health_bp = Blueprint("health", __name__)


@health_bp.route("/health")
@swag_from(
    {
        "tags": ["Health"],
        "summary": "Application health check",
        "responses": {200: {"description": "Application is healthy"}},
    }
)
def health():
    """
    Health Check Endpoint
    ---
    responses:
      200:
        description: Application health status
        schema:
          type: object
          properties:
            status:
              type: string
              example: healthy
    """
    return {"status": "healthy"}


@health_bp.route("/ready")
def ready():

    if Config.SIMULATION_MODE == "ready-fail":
        return jsonify({"status": "NOT READY"}), 500

    if Config.SIMULATION_MODE == "slow-ready":
        time.sleep(10)

    return jsonify({"status": "READY"})
