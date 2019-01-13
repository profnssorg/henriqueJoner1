"""
Descrição: Este programa divide números informados pelo usuário sem utulizar divisão2
Autor:Henrique Joner
Versão:0.0.1
Data:26/11/2018
"""

#Inicialização de variáveis

x = 0

y = 0

resultado = 0

z = 0

resto = 0

#Entrada de dados

x = int(input("Informe um número: "))

y = int(input("Informe o número a ser dividido pelo primeiro: "))



#Processamento de dados

while x >= y:
    x = x - y
    z = z +1

resto = x % y
resultado = z


print("%d / %d = %d e o resto é %d " % (x, y,resultado, resto))



#Saída de dados

