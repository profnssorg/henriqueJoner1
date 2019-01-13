"""
Descrição: Este programa procura uma expressão dentro de uma frase informada pelo usuário.
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis

primeira = []
segunda = []
terceira = []
p=0

#Entrada de dados

primeira = input("Digite uma frase: ")
segunda = input("Digite uma expressão para pesquisar na frase anterior: ")

#Processamento de dados

while(p>-1):
    p=primeira.find(segunda, p)
    if p>= 0:
        terceira.append(segunda)
        p += 1
        
terceira = "".join(terceira)



#Saída de dados
print(terceira)
