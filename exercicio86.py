"""
Descrição: Listagem 8.8 reescrita.
Autor:Henrique Joner
Versão:0.0.1
Data:03/01/2019
"""

#Inicialização de variáveis

L = []

x = 0


#Entrada de dados

L=[1,7,2,9,15]

#Processamento de dados

def soma(L):
    total = 0
    for x in L:
        total = sum(L)
        
    return total


#Saída de dados

print(soma(L))
print(soma([7,9,12,3,100,20,4]))