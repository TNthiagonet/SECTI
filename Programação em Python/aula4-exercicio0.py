# Calcular o IMC  e imprimir se o resultado é
# (abaixo do peso, peso normal, acima do peso e obesidade)

# para calcular o intervalo de tempo precisa que a variável
# esteja no meio dos valores e das condições

nome = (input("Digite seu nome: "))
curso = (input("Qual o seu curso: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# imc = peso / (altura ** 2)
# para que o número do imc seja aredondado no print final
imc = round(peso / (altura ** 2), 2)

if imc < 18.5:
    print("Você está abaixo do peso")
elif 18.5 <= imc < 25:
    print("Você está com o peso normal")
elif 25 <= imc < 30:
    print("Você está acima do peso")
else:
    print("você está com obesidade")

print("O aluno", nome, "do curso de", curso, "tem", idade, "anos", "e seu IMC é", imc)