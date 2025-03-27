import os
from pathlib import Path
from typing import List, Dict, Optional
from ..models.operator import Operator
from ..schemas.search import OperatorSearchSchema

class OperatorService:
    def __init__(self):
        # Operadores salvos em memória
        # Em um projeto completo, isso seria um banco de dados,
        # mas para fins de simplicidade, estou apenas salvando
        # em memória.
        self.operators: List[Operator] = []
        self.ALLOWED_FILTERS = {'uf', 'cidade', 'regiao_comercializacao', 'modalidade'}
    
    def load_data(self, file_path: str) -> None:
        """Carrega e realiza parse do arquivo CSV"""

        project_root = Path(__file__).parent.parent

        csv_path = project_root / "files" / "Relatorio_cadop.csv"
        
        if not csv_path.exists():
            raise FileNotFoundError(f"CSV file not found at {csv_path}")
            
        self.operators = Operator.load_from_csv(csv_path)
        print(f"Loaded {len(self.operators)} operators")
    
    def search_operators(self, search_params: OperatorSearchSchema) -> Dict:
        """
        Método para buscar operadoras de planos de saúde com base em filtros.
        """
        filtered = self.operators

        # Busca geral 
        if search_params.search_term:
            filtered = self._text_search(filtered, search_params.search_term)

        # Filtros
        if search_params.uf:
            filtered = self._filter_by_field(filtered, "uf", search_params.uf.upper(), exact=True)
            
        if search_params.cidade:
            filtered = self._filter_by_field(filtered, "cidade", search_params.cidade, exact=True)

        if search_params.modalidade:
            filtered = self._filter_by_field(filtered, "modalidade", search_params.modalidade, exact=True)
        
        paginated = filtered[
            search_params.offset : search_params.offset + search_params.limit
        ]
        
        return {
            "total": len(filtered),
            "limit": search_params.limit,
            "offset": search_params.offset,
            "results": [op.to_dict() for op in paginated]
        }
    
    def _text_search(self, operators: List[Operator], search_term: str) -> List[Operator]:
        """Busca entre razão social, nome fantasia e CNPJ"""
        if not search_term:
            return operators
            
        search_term = search_term.lower()
        results = []
        
        for op in operators:
            if (op.razao_social and search_term in op.razao_social.lower()) or \
            (op.nome_fantasia and search_term in op.nome_fantasia.lower()) or \
            (op.cnpj and search_term in op.cnpj.lower()):
                results.append(op)
            
        return results
    
    def _filter_by_field(
        self, 
        operators: List[Operator], 
        field: str,
        value: str,
        exact: bool = True
    ) -> List[Operator]:
        """Método auxiliar para filtrar por campo"""
        filtered = []
        for op in operators:
            field_value = getattr(op, field)
            if not field_value:
                continue
                
            if exact:
                if str(field_value).lower() == value.lower():
                    filtered.append(op)
            else:
                if value.lower() in str(field_value).lower():
                    filtered.append(op)
        return filtered
    
    def get_distinct_values(self, field: str) -> List[str]:
        """Retorna valores distintos para um campo específico (ex: UF)"""
        if field not in self.ALLOWED_FILTERS:
            raise ValueError(f"Field {field} not allowed")
        return sorted({
            getattr(op, field) 
            for op in self.operators 
            if getattr(op, field)
        })