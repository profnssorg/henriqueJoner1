"""
Descrição: Este programa verifica se um caractere está na lista informada.
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis

L = []
x = ""


#Entrada de dados

L = ["a", "b", "c", "d"]
x = input("Digite a letra que deseja pesquisa na lista: ").lower()

#Processamento de dados

def find(string, lista):
    return string in lista



#Saída de dados

print(find(x, L))