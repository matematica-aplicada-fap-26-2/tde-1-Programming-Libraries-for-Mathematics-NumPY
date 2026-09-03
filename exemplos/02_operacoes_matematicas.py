"""Exemplo de operações matemáticas e vetorização com NumPy."""

import numpy as np

# Armazena quatro notas em um array NumPy.
notas = np.array([6, 7, 8, 9])

# Calcula valores estatísticos do array.
print("Soma:", np.sum(notas))
print("Média:", np.mean(notas))
print("Maior:", np.max(notas))
print("Menor:", np.min(notas))

# A multiplicação é vetorizada: cada nota é multiplicada por 2 sem usar um laço.
print("Dobro:", notas * 2)

# Calcula a raiz quadrada de cada elemento do array.
numeros = np.array([1, 4, 9, 16])
print("Raiz quadrada:", np.sqrt(numeros))
