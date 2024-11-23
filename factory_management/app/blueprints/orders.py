from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService

bp = Blueprint('orders', __name__, url_prefix='/api/orders')

@bp.route('/', methods=['GET'])
def get_orders():
    return jsonify(OrderService.get_all_orders())

@bp.route('/<int:id>', methods=['GET'])
def get_order(id):
    return jsonify(OrderService.get_order_by_id(id))