# Calculadora
valor = 0

def soma(valor,numero):
    valor = valor + numero
    return valor

def subtracao(valor,numero):
    valor = valor - numero
    return valor

def divisao(valor,numero):
    valor = valor / numero
    return valor

def multiplicacao(valor,numero):
    valor = valor * numero
    return valor

print('CALCULADORA DO THIAGO')
print()
opcao = 2
while opcao != 5:
    print('1- Soma')
    print('2- Subtração')
    print('3- Divisão')
    print('4- Multiplicação')
    print('5- Sair')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        print('Seu numero atual é de: ', valor)
        numero = float(input('Digite um numero: '))
        valor = soma(valor,numero)
        print("Seu resultado: ",valor)

    if opcao == 2:
        print('Seu numero atual é de: ', valor)
        numero = float(input('Digite um numero: '))
        valor = subtracao(valor,numero)
        print("Seu resultado: ",valor)

    if opcao == 3:
        print('Seu numero atual é de: ', valor)
        numero = float(input('Digite um numero: '))
        valor = divisao(valor,numero)
        print("Seu resultado: ",valor)

    if opcao == 4:
        print('Seu numero atual é de: ', valor)
        numero = float(input('Digite um numero: '))
        valor = multiplicacao(valor,numero)
        print("Seu resultado: ",valor)

    elif opcao == 5:
        print('Obrigado, volte sempre!')

    else:
        print('Não existe esta opção, tente novamente!')