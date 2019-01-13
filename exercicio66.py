"""
Descrição: Este programa é uma variação do anterior, utilizando agora duas filas.
Autor:Henrique Joner
Versão:0.0.1
Data:07/01/2019
"""

#Inicialização de variáveis

ultimo = 0

fila = 0

operacao = 0

x = 0

atendido = 0

sair = 0

fila2 = []

#Entrada de dados

ultimo = 10
fila = list(range(1,ultimo+1))
fila2 = list(range(1,ultimo+1))
while True:
    print("\n Existem %d clientes na fila" % len(fila))
    print("Fila 1 atual:", fila)
    print("Fila 2 atual:", fila2)
    print("Digite F para adicionar um cliente ao fim da fila 1 ou G para incluir um cliente na fila 2! ")
    print("Digite A para realizar o atendimento na fila 1 ou B para realizar um atendimento na fila 2!")
    print("Digite S para sair.")
    operacao = input("Operação(F, A ou S):")

#Processamento de dados

    x=0
    sair = False 
    while x < len(operacao):
        if operacao[x] == "A":
            if(len(fila))>0:
                atendido = fila.pop(0)
                print("Cliente %d atendido na fila 1" % atendido)
        elif operacao[x] == "B":
            if(len(fila2))>0:
                atendido = fila2.pop(0)
                print("Cliente %d atendido na fila 2" % atendido)
            else:
                print("Fila vazia! Niguém para atender!")
            
        elif operacao[x] == "F":
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] == "G":
            ultimo += 1
            fila2.append(ultimo)
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        x += 1 

#Saída de dados
    if(sair):
        break