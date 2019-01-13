"""
Descrição: Este programa conta as notas que você precisa para realizar um pagamento.
Autor:Henrique Joner
Versão:0.0.1
Data:27/11/2018
"""

#Inicialização de variáveis




#Entrada de dados

valor = float(input("Digite o valor a pagar: "))
cedulas = 0

atual = 100

apagar = valor

while True:
    if atual<= apagar:
        apagar -= atual
        cedulas += 1
    elif valor <= 0.001:
        valor = valor *100
    else:
        if atual >= 1:
            print("%d cédula(s) de R$ %d" % (cedulas, atual))
        else:
            print("%d moeda(s) de R$ %5.2f" % (cedulas, atual))
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        if apagar <0.01:
            print("Valor muito baixo!")
            break

        cedulas = 0


#Processamento de dados



#Saída de dados

