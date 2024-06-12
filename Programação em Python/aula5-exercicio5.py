# Operador for "laços de repetição"


# Lista de compras

primeiroItem = input('Digite seu primeiro item: ')
segundoItem = input('Digite seu segundo item: ')
terceiroItem = input('Digite seu terceiro item: ')
quartoItem = input('Digite seu quarto item: ')

lista = [primeiroItem, segundoItem, terceiroItem, quartoItem]
qtde = 1
for item in lista:
    print(qtde,' ',item)
    qtde = qtde+1

print()
print('Fim da lista')
