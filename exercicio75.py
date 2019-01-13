"""
Descrição: Este programa eliminta os caracteres da segunda frase contidos na primeira!
Autor:Henrique Joner
Versão:0.0.1
Data:03/01/2019
"""

#Inicialização de variáveis

primeira = []
segunda = []
terceira = []
p=0

#Entrada de dados

primeira1 = input("Digite uma frase: ")
segunda1 = input("Digite uma expressão para comparar com a frase anterior: ")

primeira = primeira1.upper()
segunda = segunda1.upper()
#Processamento de dados

for x in primeira:
    if x not in segunda:
        terceira.append(x)
        

        
terceira = "".join(terceira)



#Saída de dados
print("Antes sua frase era assim: ")
print(primeira1)
print("Sem as letras %s sua frase ficou assim:" % segunda)
print(terceira)