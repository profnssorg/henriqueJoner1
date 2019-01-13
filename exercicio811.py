"""
Descrição: Programa que valida o número de caracteres de uma frase.
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis

max = 0

min = 0


#Entrada de dados

max = int(input("Qual é o máximo de caracteres? "))
min = int(input("Qual é o mínimo de caracteres? "))

#Processamento de dados

def faixa_int(string, mínimo, máximo):
    
    while True:
        v = input("Digite uma frase")
        global max
        global min
        if len(v) < mínimo or len(v) > máximo:
            print("Frase muito grande. Digite uma frase mais curta!")
        else:
            return True


#Saída de dados

print(faixa_int(v, min,max))