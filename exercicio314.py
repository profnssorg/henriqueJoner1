
"""
Descrição: Este programa calcula o valor a pagar por um carro alugado
Autor:Henrique Joner
Versão:0.0.1
Data:23/11/2018
"""

#Inicialização de variáveis

diaria = 0

km = 0

fatura = 0

dias = 0

kmpreco = 0

#Entrada de dados

dias = int(input("Por quantos dias você utilizou o veículo? "))

km = float(input("Quantos quilometros você percorreu com o veículo? "))

diaria = 60

kmpreco = 0.15

#Processamento de dados

fatura = float(dias * diaria + km * kmpreco)

#Saída de dados

print("O valor da sua fatura ficou R$ %0.2f " % fatura)
