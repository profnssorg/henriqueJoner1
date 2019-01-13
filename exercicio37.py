"""
Descrição: Este programa soma dois números inteiros fornecidos pelo usuário
Autor:Henrique Joner
Versão:0.0.1
Data:23/11/2018
"""

#Inicialização de variáveis

a = 0

b = 0

soma = 0


#Entrada de dados

a = int(input("Digite o primeiro número a ser somado: "))

b = int(input("Digite o segundo número a ser somado: "))


#Processamento de dados

soma = int(a + b)

#Saída de dados

print("A soma dos números %d e %d é: %d" % (a, b, soma))

