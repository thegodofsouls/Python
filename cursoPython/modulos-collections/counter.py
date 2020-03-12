

'''
Módulo Collections - Counter (Contador)

Collections -> High-performance Conteiner Datetypes

Counter -> Recebe um interavel com parametro e cria um objeto do tipo Collections counter
que é parecido ocm um dicionario, contendo como chave o elemento da lista passada como parametro
e como valor a quantidade de ocorrencias desse elemento
'''
# realizando a importaçao do Counter
from collections import Counter

# podemos utilizar qaulquer iteravel, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

res = Counter(lista)

print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# veja que para cada elemento da lista o Counter criou uma chave para cada elemento
# e colocou como valor a quantidade de ocorrência