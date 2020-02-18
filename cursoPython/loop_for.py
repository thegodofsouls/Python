nome = "geek university"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de for 1

# for letra in nome:
# print(letra)

# Exemplo de for 2 iterando uma lista
# for numero in lista:
# print(numero)

# Exemplo de for 3 iterando sobre o range 
# rage nao imprimi a ultima posiçao
# for numero in range(1, 10):
# print(numero)

# Enumerate pega desde a primeira posiçao até a ultima posiçao diferente deo range
# for indice, letra in enumerate(nome):
#    print(nome[indice])

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')