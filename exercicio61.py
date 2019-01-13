"""
Descrição: Este programa solicita as 7 notas de um aluno e calcula sua média
Autor:Henrique Joner
Versão:0.0.1
Data:01/12/2018
"""

#Inicialização de variáveis

notas =[0]

soma = 0

x = 0

#Entrada de dados

notas = [0,0,0,0,0,0,0]

#Processamento de dados

while x<7:
    notas[x] = float(input("Nota %d:" % x))
    soma += notas[x] 
    x += 1

x = 0

while x<7:
    print("Notas %d: %6.2f" % (x, notas[x]))
    x += 1

#Saída dados

print("Média: %5.2f" % (soma/x))


