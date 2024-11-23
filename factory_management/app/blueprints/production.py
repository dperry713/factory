from flask import Blueprint, request, jsonify
from app.services.production_service import ProductionService

bp = Blueprint('production', __name__, url_prefix='/api/production')

@bp.route('/', methods=['GET'])
def get_production_orders():
    return jsonify(ProductionService.get_all_production_orders())

@bp.route('/<int:id>', methods=['GET'])
def get_production_order(id):
    return jsonify(ProductionService.get_production_order_by_id(id))
