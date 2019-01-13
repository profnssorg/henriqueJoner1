"""
Descrição: Listagem 8.5 reescrita.
Autor:Henrique Joner
Versão:0.0.1
Data:03/01/2019
"""

#Inicialização de variáveis


L = []

lista = 0

valor = 0

#Entrada de dados

L=[10, 20, 25, 30]

#Processamento de dados

def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor) #Neste caso lista.find não funciona, pois estamos procurando dentro de uma lista. Acho!
    return None


#Saída de dados

print(pesquise(L, 25))
print(pesquise(L, 27))