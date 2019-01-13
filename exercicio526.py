"""
Descrição: ESte programa calcula o resto de uma divisão entre dois números inteiros.
Autor:Henrique Joner
Versão:0.0.1
Data:03/01/2019
"""

#Inicialização de variáveis

dividendo = 0

divisor = 0

resto = 0

#Entrada de dados

dividendo = int(input("Digite o dividendo: "))

divisor = int(input("Digite o divisor: "))

#Processamento de dados

resto = dividendo - divisor

while resto >= divisor:
    resto = resto - divisor

if resto < divisor:
    print(resto)

#Saída de dados

