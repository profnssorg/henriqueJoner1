"""
Descrição: Este programa verifica os caracteres que não estão repetidos nas expressões informadas pelo usuário.
Autor:Henrique Joner
Versão:0.0.1
Data:03/01/2019
"""

#Inicialização de variáveis

primeira = 0
segunda = 0
terceira = []
p=0

#Entrada de dados

primeira = input("Digite uma frase: ")
segunda = input("Digite uma expressão para comparar com a frase anterior: ")

#Processamento de dados

for x in primeira:
    if x not in segunda and x not in terceira:
        terceira.extend(x)
        
for x in segunda:
    if x not in primeira and x not in terceira:
        terceira.extend(x)

        
terceira = "".join(terceira)


#Saída de dados
print(terceira)