from flask import Flask
from flask_cors import CORS
from .routes.operators import bp as operators_bp
from .services.operator_service import OperatorService

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Inicializa o serviço de operadoras
    operator_service = OperatorService()
    operator_service.load_data('Relatorio_cadop.csv')
    
    # Registra os blueprints
    app.register_blueprint(operators_bp, url_prefix='/api')
    
    # Armazena o serviço de operadoras na aplicação
    app.extensions['operator_service'] = operator_service
    
    return app