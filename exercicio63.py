"""
Descrição: Este programa lê duas listas e gera uma terceira sem os elementos repetidos das duas primeiras.
Autor:Henrique Joner
Versão:0.0.1
Data:07/01/2019
"""

#Inicialização de variáveis

produto1 = []

produto2 = []

dados = []

x = 0

produto11 = []

produto22 = []

produto = []

#Entrada de dados

while True:
    
        ProdutoNome = input("Digite o nome do produto: (Digite 'sair' para parar) ")
        if ProdutoNome == "sair":
                break
        ProdutoTipo = input("Digite o principal atributo de %s: " % ProdutoNome)
        produto1 = [ProdutoNome, ProdutoTipo]
        produto11.extend(produto1)
        x += 1
        
while True:
    
        ProdutoNome = input("Digite o nome do produto: (Digite 'sair' para parar) ")
        if ProdutoNome == "sair":
                break
        ProdutoTipo = input("Digite o principal atributo de %s: " % ProdutoNome)
        produto2 = [ProdutoNome, ProdutoTipo]
        produto22.extend(produto2)
        x += 1
        
#Processamento de dados
dados = produto11[:]
dados.extend(produto22)
dados1 = []
x=0
while x < len(dados):
    y = 0
    while y < len(dados1):
        if dados[x] == dados1[y]:
            break
        y += 1
    if y == len(dados1):
        dados1.append(dados[x])
    x += 1
    

#Saída de dados
print("Lista completa: ")
print(dados)
print("lista sem repetições: ")
print(dados1)
