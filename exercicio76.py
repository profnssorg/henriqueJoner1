"""
Descrição: Este programa substitui os caracteres de uma expressao informada pelo usuário pelos de outra.
Autor:Henrique Joner
Versão:0.0.1
Data:03/01/2019
"""

#Inicialização de variáveis

base1 = 0

base2 = 0

base3 = 0

final = []


#Entrada de dados

base1 = input("Digite a primeira frase:")

base2 = input("Digite os caracteres que deseja alterar:")

base3 = input("Você deseja alterar estes caracteres por quais?")


#Processamento de dados
x = 0
if x < len(base1)-1:
    for l in base1:
        y = base2.find(l)
        if y == -1:
            final.extend(base1[x])
        if l in base2:
            final.extend(base3[y])
        x += 1




#Saída de dados
final1 = "".join(final)
print(final1)

