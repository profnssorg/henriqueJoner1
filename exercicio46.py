"""
Descrição: Este programa calcula o valor da passagem de acordo com a distância informada pelo usuário
Autor:Henrique Joner
Versão:0.0.1
Data:25/11/2018
"""

#Inicialização de variáveis

distancia = 0

passagem = 0

valor = 0

#Entrada de dados

distancia = int(input("Qual a distância (em km) que você pretende percorrer? "))

passagem = 0.5

#Processamento de dados

if distancia <= 200:
    valor = float(passagem * distancia)

else:
    passagem = 0.45
    valor = float(passagem * distancia)


#Saída de dados

print("Para percorrer %d km, você deverá pagar R$ %5.2f!" % (distancia, valor))

