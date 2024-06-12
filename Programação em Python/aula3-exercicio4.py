# Idade é igual ao que for digitado após: "Digite sua idade: "
idade = int(input("Digite sua idade: "))
# Condição Física é igual a
condicaoFisica = input("Você está em boa condição física (sim ou não). ").lower()

# Se idade for maior igual 18 e condição física receber: sim, imprima "Você está apto para participar da corrida. "
if idade >= 18 and condicaoFisica == "sim":
    print("Você está apto para participar da corrida. ")

# Se não, imprima "Você não está apto, pois não possui 18 anos ou não tem uma boa condição física"
else:
    print("Você não está apto, pois não possui 18 anos ou não tem uma boa condição física") 