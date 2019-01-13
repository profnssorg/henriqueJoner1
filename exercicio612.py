"""
Descrição: Este programa imprime o menor valor de uma lista.
Autor:Henrique Joner
Versão:0.0.1
Data:10/01/2019
"""

#Inicialização de variáveis

L = []


#Entrada de dados

L = [10,7,2,4]

#Processamento de dados

minimo=L[0]
for e in L:
    if e < minimo:
        minimo = e

#Saída de dados
    
print(minimo)