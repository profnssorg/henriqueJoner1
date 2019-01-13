"""
Descrição: Este programa calcula a sua fatura de energia elétrica
Autor:Henrique Joner
Versão:0.0.1
Data:25/11/2018
"""

#Inicialização de variáveis

consumo = 0

tipo = 0

fatura = 0

preco = 0

#Entrada de dados

tipo = input("Informe o tipo de estabelecimento: I para industrial, R para residencial e C para comercial. ")

consumo = float(input("Informe o consumo em kWh: "))

preco = 0.4

#Processamento de dados

if tipo == "I":
    preco = 0.55
    if consumo > 5000:
        preco = 0.6
	
elif tipo == "R":
    preco = 0.4
    if consumo > 500:
        preco = 0.65
     
elif tipo == "C":
     preco = 0.55
     if consumo > 1000:
         preco = 0.60

else:
    print("CÓDIGO INVÁLIDO! CÓDIGO INVÁLIDO! CÓDIGO INVÁLIDO! CÓDIGO INVÁLIDO!") 
    preco = 0
    consumo = 0


fatura = preco * consumo

#Saída de dados

print("O seu consumo foi de %5.2f kWh, a sua classificação é %s e por isso sua fatura será de R$ %5.2f!" % (consumo, tipo, fatura))
