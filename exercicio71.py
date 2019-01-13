"""
Descrição: Este programa procura uma expressão dentro de uma frase informada pelo usuário.
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis

primeira = []
segunda = []


#Entrada de dados

primeira = input("Digite uma frase: ")
segunda = input("Digite uma expressão para pesquisar na frase anterior: ")

#Processamento de dados

valor = primeira.find(segunda)

if valor == -1:
    print("Não rolou! Não achei!")

#Saída de dados
if valor > 0:
    print("Encontrei na %s posição!" % valor)

