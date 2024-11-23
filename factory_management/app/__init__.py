from flask import Flask
from app.extensions import db
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    from app.blueprints import employees, products, orders, customers, production
    app.register_blueprint(employees.bp)
    app.register_blueprint(products.bp)
    app.register_blueprint(orders.bp)
    app.register_blueprint(customers.bp)
    app.register_blueprint(production.bp)
    
    return app
