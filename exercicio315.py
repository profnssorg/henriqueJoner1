"""
Descrição:Este programa calcula a expectativa de vida de um fumante 
Autor:Henrique Joner
Versão:0.0.1
Data:23/11/2018
"""

#Inicialização de variáveis

cigarros = 0

anos = 0

perda = 0

dias = 0

#Entrada de dados

perda = 10 / 1440

cigarros = int(input("Quantos cigarros você fuma por dia? Chaminé!"))

anos = int(input("Você fuma há quantos anos? "))


#Processamento de dados

dias = (cigarros * 365) * anos * perda


#Saída de dados

print("Você viverá %d dias a menos!" % dias)
