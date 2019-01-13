"""
Descrição: Jogo da forca onde a palavra secreta é selecionada de forma aleatória da lista.
Autor:Henrique Joner
Versão:0.0.1
Data:13/01/2019
"""
#Inicialização de variáveis
import random

for x in range(10):
    print()

palavra = []
digitadas = []
acertos = []
erros = 0
base=[]
numero =0

#Entrada de dados

base = [
          "casa",
          "carro",
          "bicicleta",
          "aviao",
          "motocicleta",
          "aeroporto",
          "ladrao",
          "pobre",
          "rico"
     ]







#Processamento de dados



random.shuffle(base)
palavra = base[0]


while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")

    print("X==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "
    
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /   "
    elif erros >= 6:
        linha3 += " / \ "

#Saída de dados

    print("X%s" % linha3)
    print("X\n========")
    if erros == 6:
        print("Enforcado!")
        print("A palavra secreta era: %s" % palavra)
        break