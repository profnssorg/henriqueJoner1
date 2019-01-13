"""
Descrição: Este programa lê duas listas e gera uma terceira com os elementos das duas primeiras.
Autor:Henrique Joner
Versão:0.0.1
Data:07/01/2019
"""

#Inicialização de variáveis

produto1 = []

produto2 = []

dados = []


#Entrada de dados

ProdutoNome = input("Digite o nome do produto: ")
ProdutoTipo = input("Digite o principal atributo de %s" % ProdutoNome)

ProdutoNome2 = input("Digite o nome do próximo produto: ")
ProdutoTipo2 = input("Digite o principal atributo de %s" % ProdutoNome2)

#Processamento de dados
produto1 = [ProdutoNome, ProdutoTipo]

produto2 = [ProdutoNome2, ProdutoTipo2]

dados = produto1 + produto2

#Saída de dados
print("Os dados da primeira lista são:")
print(produto1)
print("Os dados da segunda lista são: ")
print(produto2)
print("Os dados foram armazenados da seguinte forma:" )
print(dados)

