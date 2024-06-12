
nota1 = int(input("Digite a nota do 1ª bimestre:"))
nota2 = int(input("Digite a nota do 2ª bimestre:"))
nota3 = int(input("Digite a nota do 3ª bimestre:"))

media = (nota1 + nota2 + nota3)/3

print(media)

if media > 7 and media <= 9:
    print("Aluno Aprovado.")
elif media == 5 and media < 7:
    print("Aluno Reprovado")
elif media == 10 or media == 0:
    print("Aluno fechou ou zerou")
else:
    print("Aluno na final.")

print("A media do aluno é:" , media)
