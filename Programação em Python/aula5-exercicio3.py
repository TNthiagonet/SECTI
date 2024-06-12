# Condições da idade
idade = int(input('Digite sua idade'))

if idade >= 0 and idade < 14:
    print('você é uma criança')
elif idade >=14 and idade < 18:
    print('você é um adolescente')
elif idade >= 18:
    print('Você é maior de idade')
if idade > 40:
    print('Você está coroa')
if idade > 60 and idade <= 100:
    print('Você está na melhor idade')
else:
    print('Você já viveu mais de 100 anos')