"""
Descrição: Este programa realiza operações matemáticas simples
Autor:Henrique Joner
Versão:0.0.1
Data:25/11/2018
"""

#Inicialização de variáveis

primeiro = 0

segundo = 0

resultado = 0

#Entrada de dados
primeiro = float(input("Digite um número: "))

segundo = float(input("Digite outro número: "))

operacao = input("Qual operação você deseja realizar? Utilize: soma, subtração, multiplicação ou divisão. ")


#Processamento de dados

if operacao == "soma":
    resultado = float(primeiro + segundo)
elif operacao == "subtração": 
    resultado = float(primeiro - segundo)
elif operacao == "multiplicação":
    resultado = float(primeiro * segundo)
elif operacao == "divisão":
    resultado = float(primeiro / segundo)

else:
    print("Não compreendi qual operação realizar. Utilize: soma, subtração, multiplicação ou divisão!")


#Saída de dados

print("O resultado da %s de %d com %d é %5.2f" % (operacao, primeiro, segundo, resultado))

