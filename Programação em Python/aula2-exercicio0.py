# Calculando a média do aluno
# sintaxe = regras  , if = se  ,  else = se não  ,  elif = else if = se
# or = ou  ,  and = e  , not = não for  , ==  igual  ,  != diferente
# <=  menor igual , >=  maior igual ,

nota1 = int(input("Digite a nota do 1ª bimestre:"))
nota2 = int(input("Digite a nota do 2ª bimestre:"))
nota3 = int(input("Digite a nota do 3ª bimestre:"))

# somando as notas e dividindo por 3
media = (nota1 + nota2 + nota3)/3

# ----------------------------------------------------
# imprimindo resultado (Aprovado) ou (Reprovado)
print(media)

# se a nota do aluno for maior que 7 e menor que 9
if media > 7 and media < 9:
    # imprima:
    print("Aluno Aprovado.")
# se a nota do aluno for igual a 7
elif media == 7:
    # imprima:
    print("Aluno passou raspando.")
# se a nota do aluno for igual a 10
elif media == 10:
    # imprima
    print("Aludo fechou o bimestre com nota máxima")
#se não
else:
    # imprima:
    print("Aluno Reprovado.")
# ----------------------------------------------------