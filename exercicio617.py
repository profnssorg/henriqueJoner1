"""
Descrição: Este programa funciona como um verificador de estoque.
Autor:Henrique Joner
Versão:0.0.1
Data:10/01/2019
"""

#Inicialização de variáveis

vender = False




#Entrada de dados

estoque = {"tomate": [1000, 2.30],
           "alface": [ 500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [ 100, 1.50]}
venda1 = input("Digite o produto desejado: ")

#Processamento de dados
 
while True:
        if venda1 in estoque:
            quant = int(input("Digite a quantidade de %s desejada " % venda1))
            if quant >= estoque[venda1][0]:
                print("Quantidade indisponível!")
                vender = False
                break  
            else:
                vender = True
                break
        else: 
            print("Produto indisponível!")
            break
if vender:            
    venda = [[venda1, quant]]
    total = 0
    print("Vendas: \n")
    for operação in venda:
        produto, quantidade = operação
        preço = estoque[produto][1]
        custo = preço * quantidade
        print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade, preço, custo))
        estoque[produto][0] -= quantidade
        total += custo

#Saída de dados

        print("Custo total: %21.2f\n" % total)
print("Estoque: \n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])