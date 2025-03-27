from dataclasses import dataclass
import pandas as pd
from typing import Optional

@dataclass
class Operator:
    registro_ans: str
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str]
    modalidade: str
    logradouro: Optional[str]
    numero: Optional[str]
    complemento: Optional[str]
    bairro: Optional[str]
    cidade: str
    uf: str
    cep: Optional[str]
    ddd: Optional[str]
    telefone: Optional[str]
    fax: Optional[str]
    endereco_eletronico: Optional[str]
    representante: Optional[str]
    cargo_representante: Optional[str]
    regiao_comercializacao: Optional[int]
    data_registro_ans: Optional[str]
    
    @classmethod
    def load_from_csv(cls, file_path: str) -> list['Operator']:
        df = pd.read_csv(file_path, sep=';', encoding='utf-8')
        operators = []
        
        for _, row in df.iterrows():
            operators.append(cls(
                registro_ans=str(row['Registro_ANS']),
                cnpj=str(row['CNPJ']),
                razao_social=row['Razao_Social'],
                nome_fantasia=row['Nome_Fantasia'] if pd.notna(row['Nome_Fantasia']) else None,
                modalidade=row['Modalidade'],
                logradouro=row['Logradouro'] if pd.notna(row['Logradouro']) else None,
                numero=row['Numero'] if pd.notna(row['Numero']) else None,
                complemento=row['Complemento'] if pd.notna(row['Complemento']) else None,
                bairro=row['Bairro'] if pd.notna(row['Bairro']) else None,
                cidade=row['Cidade'],
                uf=row['UF'],
                cep=str(row['CEP']) if pd.notna(row['CEP']) else None,
                ddd=str(row['DDD']) if pd.notna(row['DDD']) else None,
                telefone=str(row['Telefone']) if pd.notna(row['Telefone']) else None,
                fax=str(row['Fax']) if pd.notna(row['Fax']) else None,
                endereco_eletronico=row['Endereco_eletronico'] if pd.notna(row['Endereco_eletronico']) else None,
                representante=row['Representante'] if pd.notna(row['Representante']) else None,
                cargo_representante=row['Cargo_Representante'] if pd.notna(row['Cargo_Representante']) else None,
                regiao_comercializacao=int(row['Regiao_de_Comercializacao']) if pd.notna(row['Regiao_de_Comercializacao']) else None,
                data_registro_ans=row['Data_Registro_ANS'] if pd.notna(row['Data_Registro_ANS']) else None
            ))
        
        return operators
    
    def to_dict(self) -> dict:
            return {
                "registro_ans": self.registro_ans,
                "cnpj": self.cnpj,
                "razao_social": self.razao_social,
                "nome_fantasia": self.nome_fantasia,
                "modalidade": self.modalidade,
                "logradouro": self.logradouro,
                "numero": self.numero,
                "complemento": self.complemento,
                "bairro": self.bairro,
                "cidade": self.cidade,
                "uf": self.uf,
                "cep": self.cep,
                "ddd": self.ddd,
                "telefone": self.telefone,
                "fax": self.fax,
                "endereco_eletronico": self.endereco_eletronico,
                "representante": self.representante,
                "cargo_representante": self.cargo_representante,
                "regiao_comercializacao": self.regiao_comercializacao,
                "data_registro_ans": self.data_registro_ans
            }