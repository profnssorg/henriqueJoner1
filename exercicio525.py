"""
Descrição: Este programa apresenta a raiz quadrada do número informado pelo usuário.
Autor:Henrique Joner
Versão:0.0.1
Data:03/01/2019
"""

#Inicialização de variáveis

numero = 0

b = 0

p = 0        


#Entrada de dados

numero = float(input("Digite o número que você deseja obter a raíz quadrada: "))

b = 2          
        
#Processamento de dados

while abs(numero-(b*b)) > 0.0001:
    p=(b+(numero/b))/2
    b=p

#Saída de dados
print("A raiz quadrada é %8.4f" %  p)