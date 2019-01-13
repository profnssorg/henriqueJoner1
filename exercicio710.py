"""
Descrição: Modelo de Jogo da Velha
Autor:Henrique Joner
Versão:0.0.1
Data:12/01/2019
"""

#Inicialização de variáveis





print("""         *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
         |   Instrução: Após escolher se deseja jogar com Xis (X) ou Bola (O),               |
         |  você deverá escolher um número, que será substituído pelo item escolhido!|
         *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*   """)
print(""" Exemplo:        +-----+-----+-----+                 
                 |  7  |  8  |  9  |                 
                 +-----+-----+-----+                 
                 |  4  |  5  |  6  |                 
                 +-----+-----+-----+                 
                 |  1  |  2  |  3  |                 
                 +-----+-----+-----+""")

print("OK??")
continuar = input("Tecle S para continuar... ").upper()
fim = False
z = 0
vezantiga = "PRÓXIMO!"
if continuar == "S":
    print("OK!")
    continua = True
else:
    print("Você precisa teclar S para continuar... ")
    continuar = input("Tecle S para continuar ou qualquer tecla para sair. ").upper()
    if continuar == "S":
        print("OK!")
        continua = True
    else:
        print("Você saiu!")
        continua = False

        
#Entrada de dados

if continua:
    nome1 = input("Digite o nome do jogador 1: ").upper()
    nome2 = input("Digite o nome do jogador 2: ").upper()
    continua = False    
    simbolo = input("ATENÇÃO %s: Você quer ser o Xis ou a Bola? Digite X ou O." % nome1).upper()
    if simbolo != 'O' and simbolo != 'X':
        print("Você deve escolher entre O e X. Tá díficil hein?")
        simbolo = input("ATENÇÃO %s: Você quer ser o Xis ou a Bola? Digite X ou O." % nome1).upper()
        while simbolo != 'O' and simbolo != 'X':
            print("Assim não dá! Tchau!")
            break
    if simbolo == "O":
        jogador = "O"
        adversario = "X"
        print("%s é a Bola e %s é o Xis" % (nome1, nome2))
        print("Sem Briga!")
        continua = True
    if simbolo == "X":
        jogador = "X"
        adversario = "O"
        print("%s é a Bola e %s é o Xis" % (nome2, nome1))
        print("Sem Briga!")
        continua = True

if continua:
    vez = nome1
    linhajogador = list("|                  JOGADOR DA VEZ:                  |")
    linhajogador[35] = vez
    linhajogador1 = "".join(linhajogador)
    linha9 = list("|               |  7  |  8  |  9  |                   |")
    linha11 = list("|               |  4  |  5  |  6  |                   |")
    linha13 = list("|               |  1  |  2  |  3  |                   |")
    linha99 = "".join(linha9)
    linha111 = "".join(linha11)
    linha133 = "".join(linha13)
    
    del linhajogador[53-len(vez):50]
    linhajogador1 = "".join(linhajogador)
    if vez == nome1:
        
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|                   JOGO DA VELHA                     |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print(linhajogador1)
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|                                                     |")
        print("|               +-----+-----+-----+                   |")
        print(linha99)
        print("|               +-----+-----+-----+                   |")
        print(linha111)
        print("|               +-----+-----+-----+                   |")
        print(linha133)
        print("|               +-----+-----+-----+                   |")
        print("|                                                     |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

       
    while not fim:
  
        linhajogador = list("|                  JOGADOR DA VEZ:                  |")
        linhajogador[35] = vezantiga
        linhajogador1 = "".join(linhajogador)
        del linhajogador[53-len(vezantiga):50]
        linhajogador1 = "".join(linhajogador)
        
        x = input("É sua vez %s escolha uma posição: " % vez)

        if vez == nome1:
            y = jogador
        if vez == nome2:
            y = adversario
        if x == "1":
            linha13[19] = y
        if x == "2":
            linha13[25] = y
        if x == "3":
            linha13[31] = y
        if x == "4":
            linha11[19] = y
        if x == "5":
            linha11[25] = y
        if x == "6":
            linha11[31] = y
        if x == "7":
            linha9[19] = y
        if x == "8":
            linha9[25] = y
        if x == "9":
            linha9[31] = y
          
        linha99 = "".join(linha9)
        linha111 = "".join(linha11)
        linha133 = "".join(linha13)

        
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|                   JOGO DA VELHA                     |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print(linhajogador1)
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        print("|                                                     |")
        print("|               +-----+-----+-----+                   |")
        print(linha99)
        print("|               +-----+-----+-----+                   |")
        print(linha111)
        print("|               +-----+-----+-----+                   |")
        print(linha133)
        print("|               +-----+-----+-----+                   |")
        print("|                                                     |")
        print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n")
        
        if vez == nome2:
            vez = nome1
            vezantiga = nome2
        else:
            vez = nome2
            vezantiga = nome1
        
        
        if z > 8:
            print("Acabou! Ninguém venceu!")
            break
        z += 1
#Processamento de dados

        #VITÓRIA EM LINHAS    
        if linha99[19] == "X" and linha99[25] == "X" and linha99[31] == "X":
            fim = True
        if linha99[19] == "O" and linha99[25] == "O" and linha99[31] == "O":
            fim = True
        if linha11[19] == "X" and linha11[25] == "X" and linha11[31] == "X":
            fim = True
        if linha11[19] == "O" and linha11[25] == "O" and linha11[31] == "O":
            fim = True
        if linha13[19] == "O" and linha13[25] == "O" and linha13[31] == "O":
            fim = True
        if linha13[19] == "X" and linha13[25] == "X" and linha13[31] == "X":
            fim = True
        #VITÓRIA NAS DIAGONAIS
        if linha99[19] == "X" and linha11[25] == "X" and linha13[31] == "X":
            fim = True
        if linha99[19] == "O" and linha11[25] == "O" and linha13[31] == "O":
            fim = True
        if linha13[19] == "X" and linha11[25] == "X" and linha99[31] == "X":
            fim = True
        if linha13[19] == "O" and linha11[25] == "O" and linha99[31] == "O":
            fim = True     
        #VITÓRIA NAS COLUNAS
        if linha99[19] == "X" and linha11[19] == "X" and linha13[19] == "X":
            fim = True
        if linha99[19] == "O" and linha11[19] == "O" and linha13[19] == "O":
            fim = True
        if linha99[25] == "X" and linha11[25] == "X" and linha13[25] == "X":
            fim = True
        if linha99[25] == "O" and linha11[25] == "O" and linha13[25] == "O":
            fim = True
        if linha99[31] == "O" and linha11[31] == "O" and linha13[31] == "O":
            fim = True
        if linha99[31] == "X" and linha11[31] == "X" and linha13[31] == "X":       
            fim = True
      
 #Saída de dados        
        if fim:
            print("*~~~~~~~~~~~~~~~~~~~*")
            print("|  É o fim! ACABOU! |")
            print("   %s VENCEU!   " % vezantiga)
            print("|    ¯\_(ツ)_/¯     |")
            print("*~~~~~~~~~~~~~~~~~~~*")
            break