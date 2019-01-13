"""
Descrição: Este programa informa a tabuada informada pelo usuário
Autor:Henrique Joner
Versão:0.0.1
Data:26/11/2018
"""

#Inicialização de variáveis

n = 0

inicio = 0

fim = 0


#Entrada de dados

inicio = int(input("Informe o número onde a tabuada deve iniciar: "))

fim = int(input("Informe onde a tabuada deve finalizar: "))

n = int(input("Informe o número que você deseja obter a tabuada: "))

x = inicio

#Processamento de dados



while x <= fim and x >= inicio:
 
    print("%d X %d = %d" % (n, x, n * x))
    x = x + 1


#Saída de dados

