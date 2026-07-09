import time

from flask import Blueprint, jsonify

from app.config import Config

health_bp = Blueprint("health", __name__)


@health_bp.route("/health")
def health():

    if Config.SIMULATION_MODE == "health-fail":
        return jsonify({"status": "DOWN"}), 500

    if Config.SIMULATION_MODE == "slow-health":
        time.sleep(10)

    return jsonify({"status": "UP"})


@health_bp.route("/ready")
def ready():

    if Config.SIMULATION_MODE == "ready-fail":
        return jsonify({"status": "NOT READY"}), 500

    if Config.SIMULATION_MODE == "slow-ready":
        time.sleep(10)

    return jsonify({"status": "READY"})
