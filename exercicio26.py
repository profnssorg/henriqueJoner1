"""
Descrição:Este programa calcula um aumento de 15% para um salário de R$ 750,00
Autor:Henrique Joner
Versão:0.0.1
Data:23/11/2018
"""

#Inicialização de variáveis

salario = 0

aumento = 0

novosalario = 0

#Entrada de dados

salario = float(750)

aumento = 15

#Processamento de dados

novosalario = salario * (1 + (aumento/100))

#Saída de dados
print("Seu salario passou de %.2f para %.2f!Parabéns, vá comemorar!" % (salario, novosalario))

