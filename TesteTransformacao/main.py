import os
import zipfile
import pandas as pd
import pdfplumber
from typing import List

def extract_table_from_pdf(pdf_path: str) -> pd.DataFrame:
    """Extrai as tabelas de um arquivo PDF e retorna um DataFrame com os dados.
    
    Args:
        pdf_path (str): Caminho do arquivo PDF."""
    
    data = []
    headers = None
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                if headers is None:
                    headers = table[0]  # Primeira linha como cabeçalho
                    headers.replace()
                for row in table[1:]:   # Ignora a primeira linha de cada página
                    data.append(row)
    
    df = pd.DataFrame(data, columns=headers)
    df.dropna(how='all', inplace=True)  # Remove linhas vazias

    return df

def save_csv(df: pd.DataFrame, csv_path: str) -> None:
    """Substitui as abreviações de acordo com a legenda e salva o DataFrame em um arquivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        csv_path (str): Caminho onde o arquivo CSV será salvo."""
    # legenda = {
    #     "OD": "Seg. Odontológica",
    #     "AMB": "Seg. Ambulatorial",
    #     "HCO": "Seg. Hospitalar Com Obstetrícia",
    #     "HSO": "Seg. Hospitalar Sem Obstetrícia",
    #     "REF": "Plano Referência",
    #     "PAC": "Procedimento de Alta Complexidade",
    #     "DUT": "Diretriz de Utilização"
    # }

    legenda_od_amb = {
        "OD": "Seg. Odontológica",
        "AMB": "Seg. Ambulatorial"
    }

    df.rename(columns={"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}, inplace=True)
    df.replace(legenda_od_amb, inplace=True)
    
    df.to_csv(csv_path, index=False, encoding='utf-8')
    print(f"CSV salvo em: {csv_path}")

def zip_csv(csv_path: str, zip_path: str) -> None:
    """Cria um arquivo ZIP contendo o arquivo CSV fornecido.
    
    Args:
        csv_path (str): Caminho do arquivo CSV a ser adicionado ao ZIP.
        zip_path (str): Caminho do arquivo ZIP a ser criado."""
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))
    print(f"Arquivo ZIP criado: {zip_path}")

if __name__ == "__main__":
    PDF_FILE = "anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    CSV_FILE = "Rol_Procedimentos.csv"
    ZIP_FILE = "Teste_Lucas_Ramson.zip"
    
    df = extract_table_from_pdf(PDF_FILE)
    if not df.empty:
        save_csv(df, CSV_FILE)
        #zip_csv(CSV_FILE, ZIP_FILE)
    else:
        print("Nenhuma tabela encontrada no PDF.")
