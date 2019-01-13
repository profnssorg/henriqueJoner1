"""
Descrição: Este programa calcula o desconto de uma mercadoria
Autor:Henrique Joner
Versão:0.0.1
Data:23/11/2018
"""

#Inicialização de variáveis

preco = 0

desconto = 0

valor = 0

#Entrada de dados

preco = float(input("Qual o preço da mercadoria? "))

desconto = int(input("Qual o valor do desconto? "))


#Processamento de dados

valor = preco * (1 - desconto/100)

#Saída de dados

print("Com o desconto de %0.2f %% o preço da mercadoria fica: R$  %0.2f " % (desconto, valor))

