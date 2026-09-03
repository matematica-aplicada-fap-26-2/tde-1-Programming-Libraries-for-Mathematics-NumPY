"""Exemplo de um ndarray bidimensional, usado como matriz."""

import numpy as np

# Cria uma matriz 3 x 3. Cada lista interna representa uma linha.
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print("Matriz:")
print(matriz)

# Os índices começam em zero; [1, 2] acessa a segunda linha e a terceira coluna.
print("Elemento [1, 2]:", matriz[1, 2])

# ndim informa a quantidade de dimensões e shape informa linhas e colunas.
print("Dimensões:", matriz.ndim)
print("Formato:", matriz.shape)
