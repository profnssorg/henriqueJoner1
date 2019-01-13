"""
Descrição: Este programa verifica os maiores e menores números apresentados pelo usuário
Autor:Henrique Joner
Versão:0.0.1
Data:25/11/2018
"""

#Inicialização de variáveis

a = 0

b = 0

c = 0

maior = 0

menor = 0

#Entrada de dados

primeiro = int(input("Digite um número: "))

segundo = int(input("Ok! Agora digite mais um número: "))

terceiro = int(input("Ótimo, precisamos de apenas mais um! Digite um número: "))

#Processamento de dados

if primeiro > segundo and primeiro > terceiro:
    maior = primeiro

if segundo > primeiro and segundo > terceiro:
    maior = segundo

if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

if primeiro < segundo and primeiro < terceiro:
    menor = primeiro

if segundo < primeiro and segundo < terceiro:
    menor = segundo

if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

if primeiro == segundo and primeiro == terceiro:
    print("Todos os números são iguais!")

#Saída de dados

print("O maior número digitado foi %d, e o menor foi %d !" % (maior, menor))

