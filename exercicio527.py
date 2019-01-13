""" 
Descrição: Este programa verifica se o número informado pelo usuário é palíndromo ou não.
Autor:Henrique Joner
Versão:0.0.1
Data:03/01/2019
"""

#Inicialização de variáveis

numero = 0

inicio = 0

final = 0

#Entrada de dados

numero = input("Digite o número que deseja verificar se é palíndromo: ")

final = len(numero)-1

#Processamento de dados

while final > inicio and numero[inicio] == numero[final]:
    final -= 1
    inicio += 1
   
if numero[inicio] == numero[final]:
    print("O número é palíndromo!")
else:
          print("O número não é palíndromo!")
          


#Saída de dados
