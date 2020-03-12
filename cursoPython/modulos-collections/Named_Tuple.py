'''
módulos collections: named tuple

https://docs.python.org/2/library/collections.html?highlight=collection

'''
tupla = {1, 2, 3}

print(tupla)

# Named Tuple -> são tuplas diferenciadas, onde especificamos um nome para a mesma e também parametros

#importando o named tuple
from collections import namedtuple

# precisamos definir um nome e paramentros
# forma 1:
cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# forma 3
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)

# acessando os dados

#forma 1
print(ray[0])
print(ray[1])
print(ray[2])

#forma2
print(ray.idade)
print(ray.raca)
print(ray.nome)