-- Tabela para os dados cadastrais das operadoras
CREATE TABLE operadoras (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(100),
    representante VARCHAR(100),
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao VARCHAR(20),
    data_registro_ans DATE
);

-- Tabela para as demonstracoes contabeis 
CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    data DATE,
    reg_ans VARCHAR(20),
    cd_conta_contabil VARCHAR(20),
    descricao VARCHAR(255),
    vl_saldo_inicial DECIMAL(15,2),
    vl_saldo_final DECIMAL(15,2),
);
-- FOREIGN KEY (reg_ans) REFERENCES operadoras(registro_ans)
-- Retirado por pelo fato de ausencia de cadastro de algumas operadoras.

-- Indices para melhorar performance / Tornam as consultas mais rapidas, mas tempo de insercao mais lento
CREATE INDEX idx_dc_reg_ans ON demonstracoes_contabeis(reg_ans);
CREATE INDEX idx_dc_data ON demonstracoes_contabeis(data);
CREATE INDEX idx_dc_descricao ON demonstracoes_contabeis(descricao);