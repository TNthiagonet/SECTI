# Operador for "laços de repetição"

# Media usando for

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
nota4 = float(input('Digite sua quarta nota: '))

notas = [nota1, nota2, nota3, nota4]
soma = 0

for nota in notas:
    soma = soma + nota
media = soma / 4

if media >= 5 and media < 7:
    print('aluno em recuperação. ')
elif media >= 7 and media <= 10:
    print('aluno aprovado')
elif media < 0 or media > 10:
    print('Valores incoerentes')
else:
    print('aluno reprovado')

print('sua média foi', media)

opiniao = float(input(''))

print(opiniao)