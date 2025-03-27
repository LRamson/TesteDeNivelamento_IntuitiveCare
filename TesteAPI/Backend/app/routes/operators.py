from flask import Blueprint, request, jsonify, current_app
from http import HTTPStatus
from ..services.operator_service import OperatorService
from ..schemas.search import OperatorSearchSchema
from pydantic import ValidationError

bp = Blueprint('operators', __name__)

@bp.route('/operators/search', methods=['GET'])
def search_operators():
    service = current_app.extensions['operator_service']

    try:
        # Valida os parametros
        search_params = OperatorSearchSchema(**request.args)
        
        # Realiza a busca
        results = service.search_operators(search_params)
        return jsonify(results)
    
    except ValidationError as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@bp.route('/operators/filters/<field>', methods=['GET'])
def get_filter_options(field: str):
    service = current_app.extensions['operator_service']

    try:
        uf_filter = request.args.get('uf', '').upper()
        values = service.get_distinct_values(field, uf_filter)
        return jsonify({"field": field, "values": values})
    except ValueError as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR