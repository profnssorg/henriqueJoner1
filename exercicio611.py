"""
Descrição: Este programa utiliza o 'for' sempre que possível. 
Autor:Henrique Joner
Versão:0.0.1
Data:10/01/2019
"""

#Inicialização de variáveis

L=[]


#Entrada de dados
while True:
    n=int(input("Digite um número (0 para sair): "))

#Processamento de dados
    if n == 0:
        break
    L.append(n)



#Saída de dados
    
for e in L:
    print(e)