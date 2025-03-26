SELECT 
    o.razao_social,
    o.nome_fantasia,
    SUM(d.vl_saldo_final) AS total_despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras o ON d.reg_ans = o.registro_ans
WHERE 
    d.descricao LIKE 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
    AND d.data BETWEEN '2024-10-01' AND '2024-12-31' -- Últimos trimestre
GROUP BY 
    o.razao_social, o.nome_fantasia
ORDER BY 
    total_despesas DESC
LIMIT 10;