'''3- Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) aparece pela primeira vez no vetor. 
Caso o valor x não seja encontrado, o programa deve imprimir o valor -1'''

print('='*100)
def encontrar_posicao_valor(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i
    return -1

vetor = []

# Preencher o vetor por leitura
for i in range(5):
    valor = int(input(f"Digite o valor da posição {i}: "))
    vetor.append(valor)

valor_x = int(input("Digite o valor que deseja encontrar: "))

posicao = encontrar_posicao_valor(vetor, valor_x)

if posicao != -1:
    print(f"O valor {valor_x} foi encontrado na posição {posicao}.")
else:
    print(f"O valor {valor_x} não foi encontrado no vetor.")

print('='*100)