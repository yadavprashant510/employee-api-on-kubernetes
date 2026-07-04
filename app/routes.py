import math
import time

from flask import Blueprint, jsonify, request
import socket
from app.app import app_info
from app.logger import get_logger

employee_bp = Blueprint("employees", __name__)

logger = get_logger(__name__)

# Temporary in-memory database
employees = {1: {"id": 1, "name": "Prashant", "role": "DevOps Engineer"}}


@employee_bp.route("/")
def home():
    return jsonify({**app_info(), "api": "/api/v1", "status": "running", "hostname": socket.gethostname()})


@employee_bp.route("/api/v1/employees", methods=["GET"])
def get_employees():
    logger.info("Fetching all employees")
    return jsonify(list(employees.values()))


@employee_bp.route("/api/v1/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):

    employee = employees.get(employee_id)

    if not employee:
        return jsonify({"status": "error", "message": "Employee not found"}), 404

    return jsonify(employee)


@employee_bp.route("/api/v1/employees", methods=["POST"])
def create_employee():

    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "Request body is required"}), 400

    new_id = max(employees.keys(), default=0) + 1
    required = ["name", "role"]

    missing = [field for field in required if field not in data]

    if missing:
        return jsonify({"status": "error", "message": f"Missing fields: {', '.join(missing)}"}), 400

    employee = {"id": new_id, "name": data["name"], "role": data["role"]}

    employees[new_id] = employee

    logger.info("Employee created id=%s", new_id)

    return jsonify(employee), 201


@employee_bp.route("/api/v1/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):

    employee = employees.get(employee_id)

    if not employee:
        return jsonify({"status": "error", "message": "Employee not found"}), 404

    data = request.get_json()

    employee["name"] = data.get("name", employee["name"])
    employee["role"] = data.get("role", employee["role"])

    logger.info(f"Employee updated : {employee_id}")

    return jsonify(employee)


@employee_bp.route("/api/v1/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):

    if employee_id not in employees:
        return jsonify({"status": "error", "message": "Employee not found"}), 404

    employees.pop(employee_id)

    logger.info(f"Employee deleted : {employee_id}")

    return jsonify({"status": "success", "message": "Employee deleted"})

@employee_bp.route("/cpu")
def cpu_load():

    end = time.time() + 60

    while time.time() < end:
        math.sqrt(987654321)

    return {
        "status": "CPU test completed"
    }