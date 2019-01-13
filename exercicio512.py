
"""
Descrição: Este programa calcula o  rendimento de uma aplicação, com depósitos mensais.
Autor:Henrique Joner
Versão:0.0.1
Data:26/11/2018
"""

#Inicialização de variáveis

mensal = 0

deposito = 0

taxa = 0

n = 0

juros = 0

saldo = 0

rendimento = 0

#Entrada de dados


deposito = float(input("Qual o valor do deposito inicial? "))

mensal = float(input("Informe o valor dos depósitos mensais: "))

taxa = float(input("Informe a taxa de juros mensal: "))

n = 1

juros = 0

saldo = deposito

rendimento = saldo - deposito

#Processamento de dados

while n <= 24:
    juros = (saldo * taxa/100)
    saldo = saldo + juros + mensal
    n = n + 1
    rendimento = saldo - deposito
    print("O seu saldo no mês %d é de R$%5.2f e o seu rendimento total foi de R$ %5.2f" % (n, saldo, rendimento))


#Saída de dados

