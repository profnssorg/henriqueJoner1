"""
Descrição: Este programa converte  uma temperatura em ºC para ºF
Autor:Henrique Joner
Versão:0.0.1
Data:23/11/2018
"""

#Inicialização de variáveis

c = 0

f = 0


#Entrada de dados

c = float(input("Qual a temperatura em ºC: "))

#Processamento de dados

f =  ((9 * c)/ 5) + 32


#Saída de dados

print("A temperatura é: %.2f ºF" % f)
