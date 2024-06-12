# Calculando Média do Aluno usando (for) e (len)

nota1 = int(input('Digite a nota do primeiro bimentre: '))
nota2 = int(input('Digite a nota do segundo bimentre: '))
nota3 = int(input('Digite a nota do terceiro bimentre: '))
nota4 = int(input('Digite a nota do quarto bimentre: '))

notas = [ nota1,nota2,nota3,nota4 ]
soma = 0

for nota in notas:
    soma = soma + nota

media = soma / len(notas)

print('A média do aluno é: ', media)