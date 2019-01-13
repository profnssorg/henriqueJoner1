"""
Descrição: Este programa calcula a área de um quadrado.
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis

l = 0


#Entrada de dados

l = int(input("Informe o lado do quadrado a calcular a área: "))

#Processamento de dados

def area(l):
    return l*l

#Saída de dados
    
print(area(l))