n1 = input('digite a primeira nota: ')
n2 = input('digite a segunda nota: ')

# convertendo os valores
n1 = float(n1)
n2 = float(n2)

# calculando a média
media = n1 + n2 / 2

if media >= 7:
    print(f'Aprovado! sua media foi {media}')
else:
    print('reprovado!')