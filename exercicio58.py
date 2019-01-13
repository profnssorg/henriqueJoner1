"""
Descrição: Este programa multiplica números informados pelo usuário sem utulizar multiplicação
Autor:Henrique Joner
Versão:0.0.1
Data:26/11/2018
"""

#Inicialização de variáveis

x = 0

y = 0

resultado = 0

z = 0

#Entrada de dados

x = int(input("Informe um número: "))

y = int(input("Informe o número a ser multiplicado pelo primeiro: "))

#Processamento de dados

while z <= y:
    resultado = resultado + x
    z = z + 1

print("%d X %d = %d" % (x, y, resultado))



#Saída de dados

