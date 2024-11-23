from flask import Blueprint, request, jsonify
from app.services.employee_service import EmployeeService

bp = Blueprint('employees', __name__, url_prefix='/api/employees')

@bp.route('/', methods=['GET'])
def get_employees():
    return jsonify(EmployeeService.get_all_employees())

@bp.route('/<int:id>', methods=['GET'])
def get_employee(id):
    return jsonify(EmployeeService.get_employee_by_id(id))