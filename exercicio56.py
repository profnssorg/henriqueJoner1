"""
Descrição: Este programa informa a tabuada informada pelo usuário
Autor:Henrique Joner
Versão:0.0.1
Data:26/11/2018
"""

#Inicialização de variáveis

n = 0

x = 0

#Entrada de dados

x = 1

n = int(input("Informe o número que você deseja obter a tabuada: "))


#Processamento de dados



while x <= 10:
 
    print("%d X %d = %d" % (n, x, n * x))
    x = x + 1
#Saída de dados

