# toda lista vai ficar dentro de colchetes

listaDeFrutas = [ 'MAÇA','BANANA','UVA','ABACAXI', ]

listaDeFrutas.append('FOGO')

listaDeFrutas.insert(0,'MARACUJÁ')
listaDeFrutas.insert(1,'MORANGO')
listaDeFrutas.insert(2,'MELÃO')
listaDeFrutas.insert(3,'MELANCIA')

listaDeFrutas.remove('ABACAXI')

for fruta in listaDeFrutas:
    print(fruta)

print(len(listaDeFrutas))