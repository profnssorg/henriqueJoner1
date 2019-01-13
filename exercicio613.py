"""
Descrição: Este programa apresenta as variáveis máxima, mínima e média.
Autor:Henrique Joner
Versão:0.0.1
Data:10/01/2019
"""

#Inicialização de variáveis

T = []


#Entrada de dados

T = [-10,-8,0,1,2,5,-2,-4]

#Processamento de dados

maximo = T[0]
for e in T:
    if e > maximo:
        maximo = e
print("A temperatura máxima foi %d" % maximo)

minima = T[0]
for e in T:
    if e < minima:
        minima = e
print("A temperatura mínima foi %d" % minima)

soma = T[0]
for e in T:
    soma += soma
    media = (soma / len(T))
    break

#Saída de dados
print("A temperatura média foi de %d" % media)
