from flask import Blueprint, request, jsonify
from http import HTTPStatus
from ..services.operator_service import OperatorService
from ..schemas.search import OperatorSearchSchema
from pydantic import ValidationError

bp = Blueprint('operators', __name__)
service = OperatorService()

@bp.route('/operators/search', methods=['GET'])
def search_operators():
    try:
        # Validate query params
        search_params = OperatorSearchSchema(**request.args)
        
        # Perform search
        results = service.search_operators(search_params)
        return jsonify(results)
    
    except ValidationError as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@bp.route('/operators/filters/<field>', methods=['GET'])
def get_filter_options(field: str):
    try:
        values = service.get_distinct_values(field)
        return jsonify({"field": field, "values": values})
    except ValueError as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR