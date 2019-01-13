"""
Descrição: Este programa calcula o tempo de uma viagem de carro
Autor:Henrique Joner
Versão:0.0.1
Data:23/11/2018
"""

#Inicialização de variáveis

distancia = 0

velocidade = 0

tempo = 0


#Entrada de dados

distancia = int(input("Qual a distância (em km) a ser percorrida na sua viagem? "))

velocidade = int(input("Qual a velocidade média (em km/h) que você espera obter no percurso? "))


#Processamento de dados

tempo = float(distancia / velocidade)

 

#Saída de dados

print("Para percorrer %d quilometros a uma velocidade média de %d km/h, você levará %.2f horas!" % (distancia, velocidade, tempo))


