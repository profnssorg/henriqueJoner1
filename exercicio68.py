"""
Descrição: Este programa encontra os dados em uma lista oferecida pelo sistema.
Autor:Henrique Joner
Versão:0.0.1
Data:09/01/2019
"""

#Inicialização de variáveis

L = []
  
p = 0

x = 0

#Entrada de dados

L = [15,7,27,29]
p = int(input("Digite o valor a procurar:"))

#Processamento de dados

x = 0
while x < len(L):
    if L[x]==p:
        print("Valor %d encontrado na posição %d" % (p,x))
        break
    x += 1

    
#Saída de dados
else:
    print("%d não encontrado" % p)



