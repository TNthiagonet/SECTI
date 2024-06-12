# Conceito de Metodos
# cria usando def

#Funcao, metodo , paramentros
def calcularMedia(nome, n1, n2):
    soma = n1+n2
    media = soma / 2
    print(nome,' esta com a media de: ', media)

nome = input('Digite seu nome: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
calcularMedia(nome, nota1,nota2)
