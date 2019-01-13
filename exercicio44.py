"""
Descrição: Este programa calcula o reajuste correto de acordo com o salário do funcionário
Autor:Henrique Joner
Versão:0.0.1
Data:25/11/2018
"""

#Inicialização de variáveis

salario = 0

aumento = 0

novosalario = 0

#Entrada de dados

salario = float(input("Para que possamos verificar o seu reajuste, informe o seu salário: "))

aumento = 15

#Processamento de dados

if salario <= 1250:
    novosalario = salario * (1 + aumento/100)

if salario > 1250:
    aumento = 10
    novosalario = salario * (1 + aumento/100)


#Saída de dados

print("O seu novo salário será de R$ %5.2f, seu reajuste foi de %d%%!" % (novosalario, aumento))

