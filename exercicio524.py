"""
Descrição: Este programa apresenta os primeiros números primos na quantidade informada pelo usuário.
Autor:Henrique Joner
Versão:0.0.1
Data:03/01/2019
"""

#Inicialização de variáveis

numero = 0

x = 0

y = 0

z = 0


#Entrada de dados
print("Um número primo é todo número inteiro, positivo e maior que 1, que só possa ser dividido por ele mesmo e por 1.")
numero = int(input("Levando isso em consideração, digite o número desejado e será apresentada uma listagem contendo os primeiros números primos existentes na quantidade solicitada: "))


#Processamento de dados

if numero >= 1:  
    z = 1
    y = 3
    while z < numero:
        x = 3
        while x < y:
            if y % x == 0:
                break
            x += 2
        if x == y:
            print(x)
            z = z + 1
        y += 2    

#Saída de dados

