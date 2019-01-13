"""
Descrição: Este programa converte metros para milímetros, os valores são inseridos pelo usuário
Autor:Henrique Joner
Versão:0.0.1
Data:23/11/2018
"""

#Inicialização de variáveis

m = 0

mm = 0

resultado = 0

#Entrada de dados

m = float(input("Qual o valor em metros que você gostaria de converter para milímetros? "))


#Processamento de dados

mm = float( m * 1000)


#Saída de dados

print("%0.2f metros é equivalente a  % 0.1f milímetros, mas é difícil acreditar que você não soubesse disso!!" % (m, mm))

