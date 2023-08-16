'''2- Faça um programa que preencha por leitura um vetor de 10 posições,
 e conta quantos valores diferentes existem no vetor.'''

print('='*100)
def contar_valores_diferentes(vetor):
    conjunto_valores = set(vetor)
    return len(conjunto_valores)

vetor = []

# Preencher o vetor por leitura
for i in range(10):
    valor = int(input(f"Digite o valor da posição {i}: "))
    vetor.append(valor)

quantidade_valores_diferentes = contar_valores_diferentes(vetor)
print('='*100)

print("Quantidade de valores diferentes:", quantidade_valores_diferentes)
print('='*100)