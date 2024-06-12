# Usando Dicionário

estados = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

nome = ''
opcao = 1
while opcao != 3:
    print('1- Visualizar Estados')
    print('2- Criar conta')
    print('3- Sair')
    print()

    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        for i in estados:
            print('Nomeclatura: ', i)
            print('Estados: ', estados[i])
            print()

    elif opcao == 2:
        nome = input('Digite seu nome: ')
        estado = input('Coloque a nomeclatura do seu estado: ex:(PB) ')

        print(nome + 'é do estado: ', estados[estado])
    elif opcao == 3:
        print('Obrigado, volte sempre!')
        break
