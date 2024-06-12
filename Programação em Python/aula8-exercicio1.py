# Cadastro de usuário e senha usando while

opcao = 1
nome  = ''
senha = ''

while opcao != 3:
    print('1- Criar Conta')
    print('2- Visualizar conta')
    print('3- Sair')
    print()

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')
        if senha == nome:
            print('Tente novamente, Senha n~qo pode ser igual ao Usuário')
        else:
            print('Usuário cadastrado')

    elif opcao == 2:
        print('Seu nome:'+nome +' Sua senha: '+senha)
    elif opcao ==3:
        print('Obrigado')
        break
    else:
        print('Opção escolhida não existe')
