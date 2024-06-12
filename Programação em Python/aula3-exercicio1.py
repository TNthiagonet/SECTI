# sintaxe = regras  , if = se  ,  else = se não  ,  elif = else if = se
# or = ou  ,  and = e  , not = não for  , ==  igual  ,  != diferente
# <=  menor igual , >=  maior igual ,

nota1 = int(input("Digite a nota do 1ª bimestre:"))
nota2 = int(input("Digite a nota do 2ª bimestre:"))
nota3 = int(input("Digite a nota do 3ª bimestre:"))
nota4 = int(input("Digite a nota do 4ª bimestre:"))

media = (nota1 + nota2 + nota3 + nota4)/4

print(media)
# Se a média do aluno for maior igual a 7 e menor que 10 imprima "Aluno Aprovado"
if media >= 7 and media <10:
    print("Aluno Aprovado")

# Também se a media for menor que 7 e menor igual a 5
# condição precisa ser montada desta forma
elif 5 <= media < 7:
    print("Aluno em Recuperação")

# Também se a média for igual a 10 imprima "Aluno tirou nota máxima"
elif media == 10:
    print("Aluno tirou nota máxima")

# Também se a média for igual a 0, imprima "Aluno nem apareceu"
elif media == 0:
    print("Aluno nem apareceu")

# se não, imprima "Aluno foi Reprovado"
else:
    print("Aluno foi Reprovado")
