# Número é igual ao que for digitado após a mensagem "Digite um número: "
numero = int(input("Digite um número: "))

# Se o número for menor que 5 ou maior que 100, imprima "O número está fora do intervalo de 5-100. "
if numero < 5 or numero > 100:
    print("O número está fora do intervalo de 5-100. ")

# Se não imprima "O número entre o intervalo de 5-100. "
else:
    print("O número entre o intervalo de 5-100. ")