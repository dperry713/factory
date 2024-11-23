from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService

bp = Blueprint('products', __name__, url_prefix='/api/products')

@bp.route('/', methods=['GET'])
def get_products():
    return jsonify(ProductService.get_all_products())

@bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    return jsonify(ProductService.get_product_by_id(id))