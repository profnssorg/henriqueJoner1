"""
Descrição: Este programa calcula o pagamento de uma dívida.
Autor:Henrique Joner
Versão:0.0.1
Data:26/11/2018
"""

#Inicialização de variáveis

parcela = 0

divida = 0

taxa = 0

n = 0

juros = 0

saldo = 0

amortizacao = 0

jurostotal = 0

#Entrada de dados


divida = float(input("Qual o valor da dívida? "))

parcela = float(input("Informe o valor da parcela a pagar todos os meses: "))

taxa = float(input("Informe a taxa de juros mensal: "))

n = 1

juros = 0

saldo = divida

amortizacao = 0

jurostotal = 0

#Processamento de dados

if (parcela < divida * (taxa/100)):
    print("Sua dívida é impagável mané!")

else:

    while n <= (divida + saldo)/parcela :
        juros = (saldo * taxa/100)
        jurostotal = jurostotal + juros
        saldo = saldo + juros - parcela
        n = n + 1
        amortizacao = divida - (saldo - jurostotal)
        print("Após o pagamento da parcela relativa ao %dº mês você já pagou R$ %5.2f referente à amortização, o saldo a ser quitado é de R$  %5.2f!" % (n, amortizacao, saldo))

#Saída de dados
    print("Você levará %d meses para quitar sua dívida e o total de juros que você pagará é de R$ %5.2f" % (n, jurostotal))

