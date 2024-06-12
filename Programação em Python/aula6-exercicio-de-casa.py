# Exercício de Casa
# opcao recebe qualquer valor numérico inicial
# (pq estamos trabalhando com opções de 1 - 4)
# se fossemos trabalhar com opções alfabéticas
# opcao poderia receber qualquer letra ou frase
opcao = 999999999 # Opção criada para o menu
saldo = 0 # Saldo criado

# Criando um While para quando for diferente de 4 o sistema poderá rodar
while opcao != 4:
    # Menu de Texto
    print('Banco Python')
    print('')
    print('1- Ver saldo')
    print('2- Sacar')
    print('3- Depositar')
    print('4- Sair')
    # Removendo loop e perguntando qual a opção desejada
    opcao = int(input('Digite sua opção: '))

# Opção 1: Ver saldo
    if opcao == 1:
        print('Seu saldo é: ', saldo)

# Opção 2: Sacar
    elif opcao == 2:
        valorSacado = int(input("Digite o valor sacado: "))
        if valorSacado <= saldo:
            saldo = saldo - valorSacado
            print('Seu valor sacado foi de R$', valorSacado)
            print('Saldo atual é de R$ ', saldo)
        else:
            print('Tente Novamente')
            print('Valor desejado é maior que o seu limite.')

# Opção 3: Ver saldo
    elif opcao == 3:
        valorDepositado = int(input('Qual é valor a ser depositado: '))
        saldo = saldo + valorDepositado

        print('Seu saldo atual é de R$: ', saldo)
        print('Seu valor depositado foi de R$: ', valorDepositado)

# Opção 4: Sair
    elif opcao == 4:
        print('Obrigado, volte sempre')
        break # esta opção finaliza o codigo
    else: # Caso seja digitado alguma opção errada
        print('Digite novamente!!')
        print('Opção escolhida não existe')