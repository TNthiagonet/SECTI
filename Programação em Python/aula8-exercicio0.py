# Cadastro de usuário e senha

print('Bem vindo, cadastre seu usuário e senha para ter acesso a plataforma')

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

if usuario == senha:
    print('A sua senha precisa ser diferente do seu usuário.')

else:
    print('Usuário cadastrado com sucesso.')