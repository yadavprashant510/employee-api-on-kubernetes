from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/health")
def health():
    return jsonify({"status": "UP"})


@health_bp.route("/ready")
def ready():
    return jsonify({"status": "READY"})
