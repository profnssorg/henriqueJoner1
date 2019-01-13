"""
Descrição: Este programa verifica se os números informados são múltiplos ou não.
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis

a = 0
b = 0



#Entrada de dados


#Processamento de dados

def multiplo(a,b):
    if a % b ==0:
        return True
    else:
        return False

#Saída de dados
    
print(multiplo(8,3))
print(multiplo(8,4))
print(multiplo(8,2))