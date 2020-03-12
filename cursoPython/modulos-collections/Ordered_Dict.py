'''
módulo collections: ordered dict que garante a ordem de inserçao dos elementos

já um dict comum a ordem nao importa

'''
# importando o orderedDict
from collections import OrderedDict
# em um dicionario a ordem de inserção dos elementos não é garantida
dicionario = OrderedDict({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')