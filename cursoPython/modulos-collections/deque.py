'''
modulo collections: deque

pode-se dizer que o denque é uma lista de alta performance

'''
from collections import deque

deq = deque('geek')
print(deq)

deq.append('y') # adiciona mais um elemento no final
print(deq)

deq.appendleft('x') # adiciona mais um elemento no começo
print(deq)