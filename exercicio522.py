"""
Descrição: Este programa demonstra as operações solicitadas pelo usuário.
Autor:Henrique Joner
Versão:0.0.1
Data:01/12/2018
"""

#Inicialização de variáveis


operacao = 0

x = 0

tabuada = 0

#Entrada de dados

while True: 
    operacao1 = input("Informe a operação desejada: adição (+), subtração (-), divisão (/), multiplicação (*) ou tecle sair para encerrar. ")
    operacao = operacao1.lower()
#Processamento de dados   
    if operacao == "sair":
        print("Você saiu!")
        break        
    elif operacao != "+" or "-" or "/" or "*":
        print("Você escolheu a operação %s" % operacao)
        tabuada = int(input("Digite o número que deseja obter a tabuada "))
        x = 1
        
#Saída      
        while x<=10:
            
            if operacao == "+":
                print("%d + %d é %d" % (tabuada, x, x + tabuada))
            elif operacao == "-":
                print("%d - %d é %d" % (tabuada, x, x - tabuada))
            elif operacao == "*":
                print("%d * %d é %d" % (tabuada, x, x * tabuada))
            elif operacao == "/":
                print("%d / %d é %d" % (tabuada, x, x / tabuada))    
            x += 1
    else:
        print("Erro! Você deve escolher uma opção válida!")