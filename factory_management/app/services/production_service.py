from app.models import Production, db

class ProductionService:
    @staticmethod
    def get_all_production_orders():
        return [{'id': p.id, 'product_id': p.product_id, 'quantity': p.quantity} 
                for p in Production.query.all()]

    @staticmethod
    def get_production_order_by_id(id):
        production = Production.query.get_or_404(id)
        return {'id': production.id, 'product_id': production.product_id, 'quantity': production.quantity}
