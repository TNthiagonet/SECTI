# Convertendo o Real(R$) em Dolar($)

#----------metodo--------#
def realEmDolar(real):
    dolar = 5.28
    converter = real / dolar
    return converter
#----------metodo--------#


real = float(input('Digite o valor em Reais(R$): '))

converter = realEmDolar(real)

print('Seu valor em R$: ',real)
print('Convertido em Dolar($)',converter)