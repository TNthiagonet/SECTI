# Calculando IMC

def calcularImc(alt,peso):
    imc = peso/alt**2
    return imc

print('CALCULE SEU IMC!' )
print()

nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = calcularImc(altura,peso)

print(nome, 'seu calculo de IMC é: ', imc)