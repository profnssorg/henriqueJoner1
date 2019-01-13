"""
Descrição: Calculando o minimo multiplo comum.
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis




#Entrada de dados



#Processamento de dados

def mdivisor(a,b):

    if b == 0:
        return a
    return mdivisor(b, a % b)
    
def mmultiplo(a,b):
    return abs(a*b)/ mdivisor(a,b)



#Saída de dados

print(mmultiplo(10,8))