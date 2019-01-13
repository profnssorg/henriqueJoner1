"""
Descrição0: Este programa verifica respostas certas e erradas.
Autor:Henrique Joner
Versão:0.0.1
Data:26/11/2018
"""

#Inicialização de variáveis

pontos = 0

questao = 0

#Entrada de dados

questao = 1

#Processamento de dados
while questao <= 3:
    resposta = input("Resposta da questão %d: " % questao)
    if questao == 1 and resposta == "b" or resposta == "B":
        pontos = pontos + 1
    if questao == 2 and resposta == "a" or resposta == "A":
        pontos = pontos + 1
    if questao == 3 and resposta == "d" or resposta == "D":
        pontos = pontos + 1
    questao += 1


#Saída de dados
print("O aluno fez %d ponto(s)!" % pontos)


