Teste de Nivelamento para vaga de estágio na Intuitive Care
Lucas Ramson Siefert

Os arquivos relativos à cada teste estão separados em diferentes pastas. 
A linguagem de programação utilizada foi Python, e o DB MySQL.

No Teste de Banco de Dados, foi feito um arquivo bônus: um programa em python para normalizar e combinar as tabelas das demonstrações contábeis.
Este programa pode ser executado como:
``` python combiner.py -i 1T2023.csv 2T2023.csv 3T2023.csv -o combined.csv ```
ou
``` python combiner.py -i *.csv -o combined.csv ```
Não há problemas em executar em uma pasta com diferentes arquivos csv, desde que o primeiro tenha o formato final desejado.
Para que os scripts SQL desde mesmo teste funcionem corretamente, é necessário que os arquivos combined.csv e Relatorio_cadop.csv sejam colocados na pasta segura do servidor MySQL, e seus caminhos devidamente modificados.

Como resposta às análises do item 3.5, tem-se que as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU
AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último *trimestre*, e seus respectivos gastos acumulados são:
BRADESCO SAÚDE S.A.	                                        R$30941701628.46
SUL AMERICA COMPANHIA DE SEGURO SAÚDE                       R$21124940442.30
AMIL ASSISTÊNCIA MÉDICA INTERNACIONAL S.A.                  R$20820818085.36
NOTRE DAME INTERMÉDICA SAÚDE S.A.                           R$9307980465.62
HAPVIDA ASSISTENCIA MEDICA S.A.                             R$7755562753.15
CAIXA DE ASSISTÊNCIA DOS FUNCIONÁRIOS DO BANCO DO BRASIL    R$7459368017.21
UNIMED NACIONAL - COOPERATIVA CENTRAL                       R$7002487899.10
PREVENT SENIOR PRIVATE OPERADORA DE SAÚDE LTDA              R$5920615078.62
UNIMED BELO HORIZONTE COOPERATIVA DE TRABALHO MÉDICO        R$5411476065.42
UNIMED SEGUROS SAÚDE S/A                                    R$4824024195.15

Já no último *ano*, são:
BRADESCO SAÚDE S.A.                                         R$77467609279.79
SUL AMERICA COMPANHIA DE SEGURO SAÚDE                       R$51812853068.58
AMIL ASSISTÊNCIA MÉDICA INTERNACIONAL S.A.                  R$51005557507.35
NOTRE DAME INTERMÉDICA SAÚDE S.A.                           R$23545735832.81
HAPVIDA ASSISTENCIA MEDICA S.A.                             R$19385534464.99
CAIXA DE ASSISTÊNCIA DOS FUNCIONÁRIOS DO BANCO DO BRASIL    R$18412177093.19
UNIMED NACIONAL - COOPERATIVA CENTRAL		                R$17391267369.70
PREVENT SENIOR PRIVATE OPERADORA DE SAÚDE LTDA		        R$14635643010.58
UNIMED BELO HORIZONTE COOPERATIVA DE TRABALHO MÉDICO		R$13162050667.89
UNIMED SEGUROS SAÚDE S/A		                            R$11738001188.48