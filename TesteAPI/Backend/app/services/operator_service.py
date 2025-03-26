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
    
    def load_data(self, file_path: str) -> None:
        """Carrega e realiza parse do arquivo CSV"""
        self.operators = Operator.load_from_csv(file_path)
    
    def search_operators(self, search_params: OperatorSearchSchema) -> Dict:
        """
        Método para buscar operadoras de planos de saúde com base em filtros.
        """
        filtered = self.operators

        if search_params.razao_social:
            filtered = self._filter_by_field(
                filtered, 
                "razao_social", 
                search_params.razao_social,
                exact=False
            )

        if search_params.nome_fantasia:
            filtered = self._filter_by_field(
                filtered, 
                "nome_fantasia", 
                search_params.nome_fantasia,
                exact=False
            )
        
        if search_params.uf:
            filtered = self._filter_by_field(
                filtered,
                "uf",
                search_params.uf.upper(),
                exact=True
            )

        if search_params.cnpj:
            filtered = self._filter_by_field(
                filtered,
                "cnpj",
                search_params.cnpj.upper(),
                exact=True
            )
        
        paginated = filtered[
            search_params.offset : search_params.offset + search_params.limit
        ]
        
        return {
            "total": len(filtered),
            "limit": search_params.limit,
            "offset": search_params.offset,
            "results": [op.to_dict() for op in paginated]
        }
    
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
        if not hasattr(Operator, field):
            raise ValueError(f"Invalid field: {field}")
            
        return sorted({
            getattr(op, field) 
            for op in self.operators 
            if getattr(op, field)
        })