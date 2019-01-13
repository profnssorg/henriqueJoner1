"""
Descrição: Este programa ordena os valores de uma lista de forma decrescente
Autor:Henrique Joner
Versão:0.0.1
Data:10/01/2019
"""

#Inicialização de variáveis

L = []


#Entrada de dados

L = [1,2,3,4,5]

fim = 5

#Processamento de dados

while fim > 1:
    trocou = False
    x = 0
    while x < (fim-1):
        if L[x] < L[x+1]:
            trocou = True
            temp = L[x+1]
            L[x+1] = L[x]
            L[x]=temp
        x +=1
    if not trocou:
        break
    fim -= 1


#Saída de dados

for e in L:
    print(e)