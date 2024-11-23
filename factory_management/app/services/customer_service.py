from app.models import Customer, db

class CustomerService:
    @staticmethod
    def get_all_customers():
        return [{'id': c.id, 'name': c.name, 'email': c.email} 
                for c in Customer.query.all()]

    @staticmethod
    def get_customer_by_id(id):
        customer = Customer.query.get_or_404(id)
        return {'id': customer.id, 'name': customer.name, 'email': customer.email}