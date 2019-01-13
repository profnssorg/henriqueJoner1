"""
Descrição: Este programa converte dias, horas, minutos e segundos
Autor:Henrique Joner
Versão:0.0.1
Data:23/11/2018
"""

#Inicialização de variáveis

dias = 0

horas = 0

minutos = 0

segundos = 0


#Entrada de dados

dias = int(input("Digite o número de dias: "))

horas = int(input("Digite o número de horas: "))

minutos = int(input("Digite o número de minutos: "))

segundos = int(input("Digite o número de segundos: "))

resultado = 0

#Processamento de dados

resultado = dias * 86400 + horas * 3600 + minutos * 60 + segundos

#Saída de dados
print("O total em minutos de %d dias, %d horas, %d minutos e %d segundos em segundos é: %.1d segundos" % (dias, horas, minutos, segundos, resultado))

