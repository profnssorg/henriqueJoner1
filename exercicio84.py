"""
Descrição: Este programa calcula a área de um triângulo.
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis

b = 0

a = 0

#Entrada de dados

b = int(input("Informe a base do triângulo que deseja calcular a área: "))

a = int(input("Informe altura do triângulo que deseja calcular a área: "))

#Processamento de dados

def area(b,a):
    return (b*a)/2

#Saída de dados
    
print(area(b,a))
    