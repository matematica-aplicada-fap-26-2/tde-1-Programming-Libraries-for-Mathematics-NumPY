"""Exemplo de medidas estatísticas calculadas com NumPy."""

import numpy as np

# Array com as notas que serão analisadas.
notas = np.array([7, 8, 6, 9, 10, 8])

# mean calcula a média aritmética dos valores.
print("Média:", np.mean(notas))

# median retorna o valor central dos dados ordenados.
print("Mediana:", np.median(notas))

# std calcula o desvio padrão populacional dos valores.
print("Desvio padrão:", np.std(notas))
