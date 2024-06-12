# Criar uma lista: [ 1,2,3,4 ]
# .append = adicionar o proximo item
# posso usar o '+' ou a ',' para acrescenter um item a seguir

listaOuvidoria = []
nome = ''
Ocorrencia = ''
opcao = 1

while opcao != 3:
    print('1- Adicionar Nova Ocorrência: ')
    print('2- Vizualizar Ocorrências: ')
    print('3- Sair. ')

    opcao = int(input('Digite sua Opção: '))

    if opcao == 1:
        nome = input('Digite seu Nome: ')
        novaOcorrencia = input('Digite sua Ocorrência: ')

        ocorrenciaCriada = (nome, novaOcorrencia)
        listaOuvidoria.append(ocorrenciaCriada)
        print()
        print('Seu Nome: ' + nome + 'Ocorrencia:', novaOcorrencia)

    elif opcao == 2:
        for variavel in listaOuvidoria:
            print('Nome: ' + variavel[0])
            print('Ocorrência: ' + variavel[1])
            print()

    elif opcao == 3:
        print('Obrigado, volte sempre!')
        break
