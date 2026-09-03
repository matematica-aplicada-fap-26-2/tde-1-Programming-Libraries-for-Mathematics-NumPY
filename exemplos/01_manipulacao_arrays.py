"""Exemplo de criação e manipulação básica de arrays com NumPy."""

import numpy as np

# Cria um array unidimensional com quatro números inteiros.
numeros = np.array([40, 10, 30, 20])

print("Original:", numeros)

# Altera o primeiro elemento (índice 0) de 40 para 50.
numeros[0] = 50

# Acrescenta o valor 60 ao final do array.
numeros = np.append(numeros, 60)

# Remove o elemento que está no índice 1 (o número 10).
numeros = np.delete(numeros, 1)

# Ordena os valores em ordem crescente.
numeros = np.sort(numeros)

print("Resultado:", numeros)
