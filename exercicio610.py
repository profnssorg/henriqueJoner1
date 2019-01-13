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

v = 0

#Entrada de dados

L = [15,7,27,29]
p = int(input("Digite o primeiro valor a procurar:"))
v = int(input("Digite o segundo valor a procurar:"))
primeiro = False
segundo = False
achou1 = False
achou2 = False

#Processamento de dados
x = 0

while x < len(L):
    if L[x]== p:
        print("Valor %d encontrado na posição %d" % (p,x))
        achou1 = True
        if not segundo:
            primeiro = True      
    if primeiro:
        print("Primeiro valor encontrado antes!")
    if L[x]== v:
        print("Valor %d encontrado na posição %d" % (v,x))
        if not primeiro:    
            segundo = True
        achou2 = True        
    if segundo:
        print("Segundo valor encontrado antes!")   
       
    x += 1
    
    if x > len(L):
        break
    
    
  

    
#Saída de dados

if not achou1:
    print("%d não encontrado" % p)
if not achou2:
    print("%d não encontrado" % v)
