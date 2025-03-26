LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, 
 logradouro, numero, complemento, bairro, cidade, uf, cep, 
 ddd, telefone, fax, endereco_eletronico, representante, 
 cargo_representante, regiao_de_comercializacao, @data_registro_ans)
SET data_registro_ans = STR_TO_DATE(@data_registro_ans, '%Y-%m-%d');