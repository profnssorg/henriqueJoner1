"""
Descrição: Este programa calcula o aumento percentual do salário indicado pelo usuário
Autor:Henrique Joner
Versão:0.0.1
Data:23/11/2018
"""

#Inicialização de variáveis

salario = 0

novosalario = 0

aumento = 0

#Entrada de dados

salario = float(input("Qual o seu salário atual? "))

aumento = float(input("Qual o reajuste do salário: "))


#Processamento de dados

novosalario = salario * (1 + (aumento/100))

#Saída de dados

print("O seu novo salário será: R$ %.2f" % novosalario)

