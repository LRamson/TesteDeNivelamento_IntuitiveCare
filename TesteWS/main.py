# TESTE DE WEB SCRAPING
# Este programa visita a URL fornecida, baixa todos os arquivos PDF que possuem "Anexo" no nome e cria um arquivo ZIP com eles.
# Além disso, cria uma pasta chamada "anexos", que será utilizada pelo próximo programa.

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import zipfile
from typing import List


def download_pdfs(base_url: str, download_folder: str) -> List[str]:
    """Baixa os arquivos PDF da URL fornecida e os salva na pasta download_folder.
    
    Args:
        base_url (str): URL da página a ser visitada.
        download_folder (str): Pasta onde os arquivos PDF serão salvos."""
    
    # Faz a requisição GET para a URL fornecida
    response = requests.get(base_url)
    response.raise_for_status()
    
    # Faz o parse do HTML da página
    html = BeautifulSoup(response.text, 'html.parser')
    pdf_links: List[str] = []

    # Procura por links que contenham "Anexo" no nome e terminem com ".pdf"
    # Adiciona o link completo na lista pdf_links
    for link in html.find_all('a', href=True):
        href: str = link['href']
        if 'Anexo' in href and href.endswith('.pdf'):
            full_url: str = urljoin(base_url, href)
            pdf_links.append(full_url)
    
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Para cada link encontrado, faz o download do arquivo PDF e salva na pasta download_folder
    downloaded_files: List[str] = []
    for pdf_url in pdf_links:
        pdf_name = os.path.join(download_folder, pdf_url.split('/')[-1])
        with requests.get(pdf_url, stream=True) as r:
            r.raise_for_status()
            with open(pdf_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        downloaded_files.append(pdf_name)
        print(f"Baixado: {pdf_name}")
    
    return downloaded_files

def zip_files(file_list: List[str], output_zip: str) -> None:
    """Cria um arquivo ZIP com os arquivos fornecidos.
    
    Args:
        file_list (List[str]): Lista com os caminhos dos arquivos a serem adicionados ao ZIP.
        output_zip (str): Nome do arquivo ZIP a ser criado."""
    
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in file_list:
            zipf.write(file, os.path.basename(file))
    print(f"Arquivo ZIP criado: {output_zip}")

if __name__ == "__main__":
    BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    DOWNLOAD_FOLDER = "anexos"
    ZIP_FILE = "anexos.zip"
    
    pdf_files = download_pdfs(BASE_URL, DOWNLOAD_FOLDER)
    if pdf_files:
        zip_files(pdf_files, ZIP_FILE)
    else:
        print("Nenhum arquivo PDF encontrado.")
