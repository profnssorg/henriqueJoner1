"""
Descrição: Este programa verifica qual número é maior.
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis

a = 0
b = 0



#Entrada de dados


#Processamento de dados

def omaior(a,b):
    if a > b:
        return("%d é maior que %d!" % (a,b))
    elif b > a:
        return("%d é maior que %d!" % (b,a))
    else:
        print("Os dois números são iguais!")

#Saída de dados

print(omaior(10,12))