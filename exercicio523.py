"""
Descrição: Este programa identifica se o número informado pelo usuário é primo ou não.
Autor:Henrique Joner
Versão:0.0.1
Data:03/01/2019
"""

#Inicialização de variáveis

numero = 0


#Entrada de dados
print("Um número primo é todo número inteiro, positivo e maior que 1, que só possa ser dividido por ele mesmo e por 1.")
numero = int(input("Levando isso em consideração, digite o número que deseja verificar se é primo: "))


#Processamento de dados
if numero == 2:
    print("Você escolheu o número 2, este número é primo!")

elif numero % 2 == 0:
    print("Você escolheu o número %d, este número não é primo!" % numero)
    
else:
    x = 3
    while x < numero:
        if numero % x == 0:
            break
        x += 2
    if numero == x:
#Saída de dados        
            print("Você escolheu o número %d, este número é primo!" % numero)
    else:
            print("Você escolheu o número %d, este número não é primo!" % numero)

if numero < 2:
    print ("Número inválido! Seu número precisa ser inteiro e maior que 1!")
            
