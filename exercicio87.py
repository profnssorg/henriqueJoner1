"""
Descrição: Calculando o maior divisor comum.
Autor:Henrique Joner
Versão:0.0.1
Data:11/01/2019
"""

#Inicialização de variáveis

s=False


#Entrada de dados



#Processamento de dados

def mdivisor(a,b):
    if b > a:
        global s
        s=True
        x = "Inválido!"
        return x
    if b == 0:
        return a
    return mdivisor(b, a % b)



#Saída de dados

if s:
    print("Inválido!")
if not s:
    print(mdivisor(100000,800))
