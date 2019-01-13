"""
Descrição: Cálculo do Fibonacci
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis


L=[]

#Entrada de dados

L = [5,8,9,2,11]

#Processamento de dados

def fibonacci(n):
    fibonacci1 = 1
    while n > 1:
        fibonacci1 *= n
        n -= 1
    return fibonacci1


#Saída de dados

print(fibonacci(L[0]))
print(fibonacci(L[1]))
print(fibonacci(L[2]))
print(fibonacci(L[3]))
print(fibonacci(L[4]))