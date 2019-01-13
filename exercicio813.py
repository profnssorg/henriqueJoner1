"""
Descrição: Jogo onde o usuário tem três chances para acertar um número aleatório.
Autor:Henrique Joner
Versão:0.0.1
Data:13/01/2019
"""

#Inicialização de variáveis

import random

n = random.randint(1,10)
venceu = False
y = 0


#Entrada de dados


#Processamento de dados

while y < 3:
    x = int(input("Escolha um número entre 1 e 10: "))
    if (x==n):
        print("Você acertou!")
        venceu = True
        break
    else:
        print("Você errou. ")
    y += 1


#Saída de dados
if venceu:
    print("Parabéns!")
    
if not venceu:    
    print("Não deu!")
