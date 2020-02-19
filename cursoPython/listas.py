# Listas em pytho funcional com vetores/matrizes(arrays)
# não possui tamanho fixo de um array porque python é dinâmico
# nao é tamanho infinito, enquanto estiver espaço na memoria poderá ser adicionado mais elementos no array
# as listas em python sao representadas por []

'''
type([])


lista2 = ['r', 'c', 'j', 'a', 'v', 'd']
lista3 = []

lista4 = list(range(11)) # 11 seria a posiçao de 0 até 10 no range

lista5 = list('Geek University')
# print(lista5)

# podemos facilmente checar se determinado valor está contido na lista
num = 7

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'nao encontrei o número {num}')

# pode-se ordenar facilmente uma lista
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista1.sort() # .sort ordena a lista
print(lista1) # mostra a lista em ordem crescente

# pode-se facilmente contar o número de ocorrências de um valor de uma lista
print(lista1.count(1))
print(lista5.count('e')) # obs: no count só contar um elemento por vez

# adicionando elementos em uma lista

#lista1.append(42) # obs: no appen só pode adicionar um elemento por vez 
#print(lista1)
lista1.append([3, 2, 4]) # adiciona uma nova lista dentro da lista com os []
print(lista1)

listarTodos = [3, 2, 4]
if listarTodos in lista1:
    print('Encontrei a lista')
else:
    print('nao foi encontrado a lista')

lista1.extend([123, 32, 6]) # adiciona uma nova lista dentro da lista sem os [] e nao aceita valor unico
print(lista1)

# pode-se inserir um novo elemento na lista informando a posiçao do incide
lista1.insert(2, 'item')
print(lista1)

# podemo-se juntar duas listas
listasJuntas = lista1 + lista2
print(listasJuntas)

# podemos facilmente inverter uma lista

# forma 1
# lista1.reverse()
# lista2.reverse()

# forma 2
print(lista1[::-1]) # começa na posiçao 0 até a final e depois inverte colocando -1 
print(lista2[::-1])

# mostrando a quantidade de elementos no total
print('a quantidade de elementos da lista1 é {0}'.format(len(lista1)))

# podemos remover todos os elementos do array
print(lista1)
lista1.clear()
print(lista1)

# convertendo uma lista em string
lista6 = ['Programaçao', 'em', 'Python']
curso = '$'.join(lista6)
print(curso)

# iterando sobre listas

# exemplo 1 - utilizando for

cont = 0
for elemento in lista1:
    print(elemento)
    cont = cont + elemento
    print(cont)
'''
# iterando sobre listas

# exemplo 2 - utilizando while
carrinho = [] # criando uma lista(array) vazia
produto = ''

while(produto != 'sair'):
    print("adicione um produto na lista ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

