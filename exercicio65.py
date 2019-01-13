"""
Descrição: Este programa recebe todas as ordens de atentimento de uma fila de uma única fez e depois as executa.
Autor:Henrique Joner
Versão:0.0.1
Data:07/01/2019
Comentário: Não consegui pensar em uma forma diferente de resolver o problema, ficou igual ao livro. :/
"""


#Inicialização de variáveis

ultimo = 0

fila = 0

operacao = 0

x = 0

atendido = 0

sair = 0



#Entrada de dados

ultimo = 10
fila = list(range(1,ultimo+1))
while True:
    print("\n Existem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila, ")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação(F, A ou S):")

#Processamento de dados

    x=0
    sair = False 
    while x < len(operacao):
        if operacao[x] == "A":
            if(len(fila))>0:
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
            else:
                print("Fila vazia! Niguém para atender!")
            
        elif operacao[x] == "F":
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] == "S":
            sair = True
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        x += 1 

#Saída de dados
    if(sair):
        break
