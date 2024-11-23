from flask import Blueprint, request, jsonify
from app.services.customer_service import CustomerService

bp = Blueprint('customers', __name__, url_prefix='/api/customers')

@bp.route('/', methods=['GET'])
def get_customers():
    return jsonify(CustomerService.get_all_customers())

@bp.route('/<int:id>', methods=['GET'])
def get_customer(id):
    return jsonify(CustomerService.get_customer_by_id(id))
