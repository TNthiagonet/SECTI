# Número é igual ao que for digitado após a mensagem "Digite um número: "
numero = int(input("Digite um número: "))
# Se o numero for divisivel por 2, imprima que "O número é par e maior igual a 10."
if numero % 2 == 0 and numero >= 10:
    print("O número é par e maior igual a 10.")

# Se também o número for maior igual a 10 e não for divisivel por 2 imprima "O número é impar e maior que 10."
elif numero >= 10 and not numero % 2 == 0:
    print("O número é impar e maior que 10.")

# Se também o número for menor que 10 e não for divisivel por 2 imprima "O numéro é menor que 10 e ele é impar""
elif numero < 10 and not numero % 2 == 0:
    print ("O numéro é menor que 10 e ele é impar")

# Se não, imprima que "O número é impar"
else:
    print("O número é impar ou menor que 10")