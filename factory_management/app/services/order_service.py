from app.models import Order, db

class OrderService:
    @staticmethod
    def get_all_orders():
        return [{'id': o.id, 'customer_id': o.customer_id, 'total_amount': o.total_amount} 
                for o in Order.query.all()]

    @staticmethod
    def get_order_by_id(id):
        order = Order.query.get_or_404(id)
        return {'id': order.id, 'customer_id': order.customer_id, 'total_amount': order.total_amount}
