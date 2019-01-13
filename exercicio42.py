"""
Descrição: Este programa aplica uma multa para usuários que ultrapassem 80 km/h
Autor:Henrique Joner
Versão:0.0.1
Data:25/11/2018
"""

#Inicialização de variáveis

velocidade = 0

multa = 0

multatotal = 0

#Entrada de dados

velocidade = int(input("Qual a sua velocidade? "))

multa = 5

#Processamento de dados

if velocidade > 80:
    multatotal = (velocidade - 80) * 5
    print ("Você ultrapassou a velocidade limite, sua multa será de R$ %d ! E para piorar, só pode ser paga no Banrisul, no caixa do banco!" % multatotal)

if velocidade <= 80:
    print("Ok! Você está dentro da velocidade limite, mas fique esperto!")

#Saída de dados

