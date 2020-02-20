mes = {'jan': 100, 'fev': 250, 'mar': 400}

# iterando dicionario
print(mes) # imprimindo os meses
for chave in mes:
    print(chave) # imprimindo os valores

for chave in mes:
    print(mes[chave]) # imprimindo as suas respectivas chaves

for chave in mes:
    print(f'{chave} : {mes[chave]}') # imprimindo os valores e chaves

# acessando chaves
# print(mes.keys())

for chave in mes.keys(): # forma mais recomendada para trabalahr com chaves no python
    print(mes[chave])

# acessando os valores
# print(mes.values())

for valor in mes.values(): # forma mais recomendada pra trabalhar com valores no python
    print(valor)

# desempacotamento de dicionario
for chave, valor in mes.items():
    print(f'chaves={chave} e valor={valor}')

print(sum(mes.values())) # vai mostrar o resultado da soma dos valores
print(max(mes.values())) # vai mostrar o valor máximo das chaves
print(min(mes.values())) # vai mostrar o valor minimo das chaves
print(len(mes)) # vai mostrar quantos elementos tem dentro
