import csv
import os
import argparse
from pathlib import Path

def combine_csv_files(input_files, output_file, skip_duplicate_headers=True):
    """
    Combina múltiplos arquivos CSV em um único arquivo.
    Mantém o formato original (delimitador ; e campos entre aspas).
    Normaliza apenas o formato da data.

    Args:
        input_files (list): Lista de caminhos dos arquivos de entrada
        output_file (str): Caminho do arquivo de saída
        skip_duplicate_headers (bool): Ignora arquivos com cabeçalhos diferentes do primeiro arquivo. Padrão: True
    """
    converted_files = len(input_files)

    if not input_files:
        print("Nenhum arquivo de entrada especificado.")
        return

    for file in input_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Arquivo de entrada não encontrado: {file}")

    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = None
        headers = None
        
        for i, file in enumerate(input_files):
            with open(file, 'r', newline='', encoding='utf-8') as infile:
                reader = csv.reader(infile, delimiter=';', quotechar='"')
                current_headers = next(reader)
                
                if i == 0:
                    headers = current_headers
                    writer = csv.writer(outfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
                    writer.writerow(headers)
                else:
                    if current_headers != headers:
                        converted_files -= 1
                        print(f"Aviso: Cabeçalhos em {file} não correspondem aos do primeiro arquivo.")
                        continue
                
                # Processa a primeira linha para saber se precisa de normalizacao
                try:
                    first_row = next(reader)

                    # Flag para necessidade de normalizacao, evitando checagens desnecessarias
                    needs_conversion = '/' in first_row[0]
                    
                    if needs_conversion:
                        first_row[0] = normalize_date(first_row[0])
                    writer.writerow(first_row)
                    
                    for row in reader:
                        if needs_conversion:
                            row[0] = normalize_date(row[0])
                        writer.writerow(row)
                except StopIteration:
                    continue

    print(f"Arquivos combinados com sucesso: {converted_files} arquivos em {output_file}")

def normalize_date(date_str):
    """Converte data de DD/MM/YYYY para YYYY-MM-DD"""
    day, month, year = date_str.split('/')
    return f"{year}-{month}-{day}"

def main():
    parser = argparse.ArgumentParser(description='Combina arquivos CSV com cabeçalhos idênticos')
    parser.add_argument('-i', '--input', nargs='+', required=True,
                      help='Arquivos CSV de entrada (suporta wildcards)')
    parser.add_argument('-o', '--output', required=True,
                      help='Caminho do arquivo de saída')
    args = parser.parse_args()

    input_files = []
    for pattern in args.input:
        input_files.extend(Path().glob(pattern))
    input_files = [str(f) for f in input_files]
    
    combine_csv_files(input_files, args.output)

if __name__ == '__main__':
    main()