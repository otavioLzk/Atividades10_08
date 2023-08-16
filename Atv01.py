'''01 - Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
f) imprima a soma dos elementos de valor negativo
'''

lista = [12, -2, 4 ,8 ,29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

print('='*100)
maior_elemento = max(lista)
print("Maior elemento:", maior_elemento)
print('='*100)

menor_elemento = min(lista)
print("Menor elemento:", menor_elemento)
print('='*100)

numeros_pares = [num for num in lista if num % 2 == 0]
print("Números pares:", numeros_pares)
print('='*100)

primeiro_elemento = lista[0]
num_ocorrencias_primeiro = lista.count(primeiro_elemento)
print("Número de ocorrências do primeiro elemento:", num_ocorrencias_primeiro)
print('='*100)

soma_elementos = sum(lista)
media_elementos = soma_elementos / len(lista)
print("Média dos elementos:", media_elementos)
print('='*100)

elementos_negativos = [num for num in lista if num < 0]
soma_elementos_negativos = sum(elementos_negativos)
print("Soma dos elementos negativos:", soma_elementos_negativos)
print('='*100)