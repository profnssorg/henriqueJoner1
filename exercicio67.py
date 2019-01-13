"""
Descrição:Este programa verifica se o usuário soube encerrar parênteses corretamente.
Autor:Henrique Joner
Versão:0.0.1
Data:08/01/2019
"""

#Inicialização de variáveis
fila = []



#Entrada de dados
while True:
    operacao = input("Operação '(', ')' ou S para sair):")

#Processamento de dados

    x=0
    sair = False 
    while x < len(operacao):
        if operacao[x] == ")":
            atendido = fila.pop(-1)
            
        elif operacao[x] == "(":
            fila.append('(')
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print("Operação inválida! Digite apenas '(', ')' ou S!")
        x += 1 

#Saída de dados
    if len(fila)>0:
        print("Erro!")
    else:
        print("OK")
    if(sair):
        break
