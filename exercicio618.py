"""
Descrição: Este programa conta as letras em uma frase
Autor:Henrique Joner
Versão:0.0.1
Data:10/01/2019
"""

#Inicialização de variáveis

base = {}


#Entrada de dados

dados = input("Digite uma frase: ")

#Processamento de dados


for x in dados:
    if x in base:
        base[x] = base[x]+1
    else:
        base[x] = 1


#Saída de dados

print(base)
