"""
Descrição: Este programa soma números inteiros informados pelo usuário 
Autor:Henrique Joner
Versão:0.0.1
Data:27/11/2018
"""

#Inicialização de variáveis

numero = 0

soma = 0

x = 0

media = 0

#Entrada de dados




#Processamento de dados

while True:
     x = x + 1
     numero = int(input("Digite um número: "))
     if numero ==0:
        x = x-1
        media = soma / x
        break

     soma = soma + numero


#Saída de dados

print("Sua conta finalizou em %d, você somou %d números e a média deles foi %d!" % (soma, x, media))
