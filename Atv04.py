'''4- Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. 
Faça um programa que simule o lançamento do dado e determine o percentual de ocorrências de face 6 do dado dentre 
esses 50 lançamentos.'''

print('='*100)
import random

def percentual_face_6(lancamentos):
    contador_face_6 = lancamentos.count(6)
    return (contador_face_6 / len(lancamentos)) * 100

# Simular o lançamento do dado 50 vezes
num_lancamentos = 50
lancamentos = [random.randint(1, 6) for _ in range(num_lancamentos)]

percentual = percentual_face_6(lancamentos)

print(f"Percentual de ocorrências da face 6: {percentual:.2f}%")

print('='*100)