LOAD DATA INFILE 'C:\ProgramData\MySQL\MySQL Server 8.0\Uploads\combined.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET 
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    vl_saldo_inicial = CAST(REPLACE(@vl_saldo_inicial, ",", ".") AS DECIMAL(15,2)),
    vl_saldo_final = CAST(REPLACE(@vl_saldo_final, ",", ".") AS DECIMAL(15,2));