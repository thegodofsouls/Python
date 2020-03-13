'''
funções com retorno


# exemplo de funcoes

# no python os valores sao retornados com a palavra reservada return
# nao precisa necessariamente passar uma variável para receber o retorno de uma função
def quadrado_de_7():
     return 7 * 7 # retornando a funcao

# foi criado uma variavel para receber o retorno da funçao
ret = quadrado_de_7()

print(f'Retorno {ret}')
print(f'Retorno {quadrado_de_7() + 1}')

'''
from random import random

def joga_moeda():
     # gera um número pseudo-randômico entre 1 e 0 que vai gerar repetiçao
     valor = random()
     if valor > 0.5:
          return 'cara'
     return 'coroa'
print(joga_moeda())