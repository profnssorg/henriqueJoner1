"""
Descrição: Este programa funciona como uma caixa registradora.
Autor:Henrique Joner
Versão:0.0.3
Data:27/11/2018
"""



#Inicialização de variáveis


a = 0.5

b = 1

c = 4

d = 7

e = 9

qtd1 = 0

qtd2 = 0


qtd3 = 0

qtd5 = 0

qtd9 = 0

saldo = 0

saldo1 = 0 

saldo2 = 0

saldo3 = 0

saldo5 = 0

saldo9 = 0

preco = 0

produto1 = 0

produto2 = 0

produto3 = 0

produto5 = 0

produto9 = 0

#Entrada de dados



while True:
    codigo = int(input("Digite o código do produto ou 0 para sair "))


    if codigo == 1:
        qtd1 = int(input("Informe a quantidade adquirida: "))
        preco = a
        saldo1 = qtd1 * preco
        produto1 = 1

    elif codigo == 2:
        qtd2 = int(input("Informe a quantidade adquirida: "))
        preco = b
        saldo2 = qtd2 * preco
        produto2 = 2

    elif codigo == 3:
        qtd3 = int(input("Informe a quantidade adquirida: "))
        preco = c
        saldo3 = qtd3 * preco
        produto3 = 3

    elif codigo == 5:
        qtd5 = int(input("Informe a quantidade adquirida: "))
        preco = d
        saldo5 = qtd5 * preco
        produto5 = 5

    elif codigo == 9:
        qtd9 = int(input("Informe a quantidade adquirida: "))
        preco = e
        saldo9 = qtd9 * preco
        produto9 = 9

    elif codigo == 0:
        break
    else:
        print("Código Inválido!")

saldo = saldo1 + saldo2 + saldo3 + saldo5 + saldo9
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("              Seu total a pagar é de R$ %5.2f!" % saldo)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Você adquiriu %d unidades do produto código %d por %5.2f." % (qtd1, produto1, saldo1) )
print("Você adquiriu %d unidades do produto código %d por %5.2f." % (qtd2, produto2, saldo2) )
print("Você adquiriu %d unidades do produto código %d por %5.2f." % (qtd3, produto3, saldo3) )
print("Você adquiriu %d unidades do produto código %d por %5.2f." % (qtd5, produto5, saldo5) )
print("Você adquiriu %d unidades do produto código %d por %5.2f." % (qtd9, produto9, saldo9) )
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("            OBRIGADO POR COMPRAR, VOLTE SEMPRE!           ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Processamento de dados




#Saída de dados

