"""
Descrição: Este programa conta o número de letras em uma frase informada pelo usuário.
Autor:Henrique Joner
Versão:0.0.1
Data:10/01/2019
"""

#Inicialização de variáveis

base = 0

dicionario = {}

#Entrada de dados

base1 = input("Digite uma frase e nós contaremos quantes vezes cada caracter aparece nela: ")

base = base1.upper()

#Processamento de dados

for x in base:
    if x in dicionario:
        dicionario[x] += 1
    else:
        dicionario[x] = 1

        
#Saída de dados
print("\n Na frase %s:" % base)
for y in dicionario:
    print("%s apareceu %d vezes!" % (y, dicionario[y]))
