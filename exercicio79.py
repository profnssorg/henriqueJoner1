"""
Descrição: Jogo da forca onde a palavra secreta é selecionada de uma lista (formação do desenho alterada).
Autor:Henrique Joner
Versão:0.0.1
Data:10/01/2019
"""
#Inicialização de variáveis

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


numero = int(input("Digite um número: "))

linha1 = list("X==:==")
linha2 = list("X  :  ")
linha3 = list("X     ")
linha4 = list("X     ")
linha5 = list("X     ")
linha6 = list("======")


#Processamento de dados



palavra = base[ (numero * 776) % len(base)]

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
            if erros == 1:
                linha3[3] = "o"
            if erros == 2:
                linha4[3] = "|"
            if erros == 3:
                linha4[2] = "\\"
            if erros == 4:
                linha4[4] = "/"
            if erros == 5:
                linha5[2] = "/"
            if erros == 6:
                linha5[4] = "\\"

    print("".join(linha1))
    print("".join(linha2))
    print("".join(linha3))
    print("".join(linha4))
    print("".join(linha5))
    print("".join(linha6))  
   

 #Saída de dados


    if erros == 6:
        print("Enforcado!")
        print("A palavra secreta era: %s" % palavra)
        break