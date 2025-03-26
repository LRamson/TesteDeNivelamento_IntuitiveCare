from pydantic import BaseModel, Field
from typing import Optional

class OperatorSearchSchema(BaseModel):
    razao_social: Optional[str] = Field(None, description="Filter by company name")
    nome_fantasia: Optional[str] = Field(None, description="Filter by trade name")
    cnpj: Optional[str] = Field(None, description="Filter by CNPJ")
    registro_ans: Optional[str] = Field(None, description="Filter by ANS registration")
    modalidade: Optional[str] = Field(None, description="Filter by modality")
    cidade: Optional[str] = Field(None, description="Filter by city")
    uf: Optional[str] = Field(None, description="Filter by state")
    regiao_comercializacao: Optional[int] = Field(None, description="Filter by commercial region")
    limit: int = Field(20, ge=1, le=100, description="Maximum results to return")
    offset: int = Field(0, ge=0, description="Pagination offset")