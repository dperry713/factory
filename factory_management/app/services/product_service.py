from app.models import Product, db

class ProductService:
    @staticmethod
    def get_all_products():
        return [{'id': p.id, 'name': p.name, 'price': p.price, 'stock': p.stock} 
                for p in Product.query.all()]

    @staticmethod
    def get_product_by_id(id):
        product = Product.query.get_or_404(id)
        return {'id': product.id, 'name': product.name, 'price': product.price, 'stock': product.stock}
