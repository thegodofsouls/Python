'''
 módulo collections = Default Dict
'''

dicionario = {'curso': 'programação em python: Essencial'}
print(dicionario)

print(dicionario['curso'])

'''
OBS: Lambbas são funçoes sem nome que podem ou nao receber parametros de entrada e retornar valores

'''
# fazendo a importaçao do defaultdict
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'programaçao em Python: Essencial'

print(dicionario)

dicionario['outro']

print(dicionario)