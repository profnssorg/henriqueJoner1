"""
Descrição: Este programa calcula o número e o valor das prestações a pagar em um imóvel.
Autor:Henrique Joner
Versão:0.0.1
Data:24/11/2018
"""

#Inicialização de variáveis

valorcasa = 0

anos = 0

nprestacao = 0

prestacao = 0

salario = 0

#Entrada de dados

valorcasa = float(input("Qual o valor da casa que você deseja adquirir? "))

anos =  int(input("Deseja pagar em quantos anos? "))

salario = float(input("Qual seu salário atual? "))

#Processamento de dados

nprestacao = anos * 12

prestacao = valorcasa / nprestacao

if prestacao <= salario * 0.3:
    print("Você terá de pagar %d vezes de R$%5.2f !" % (nprestacao, prestacao)) 
else:
    print("Infelizmente sua renda não é compatível com a aquisição que você deseja realizar!")




#Saída de dados

