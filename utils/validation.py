import numpy as np


def validate_string_key(
    key: str, 
    length: int | None = None, 
    alphabet: str = 'абвгдежзийклмнопрстуфхцчшщъыьэюя', 
    is_can_repeat: bool = True
):
    alphabet = alphabet.upper()
    
    for char in key:
        if not char in alphabet:
            raise ValueError('Введенный ключ содержит неизвестный символ')
    if not isinstance(key, str):
        raise TypeError('Введенный ключ не является строкой')
    if len(key) != length and length != None:
        raise ValueError('Введенный ключ имеет длину меньше 1')
    if not is_can_repeat and len(set(key)) != len(key):
        raise ValueError('Буквы в ключе не могут повторяться')
    return key


def validate_number_key(key: int):
    if not isinstance(key, int):
        raise TypeError('Введенный ключ не является целым числом')
    if key < 1 or key > 31:
        raise ValueError('Введенный ключ не может быть отрицательным')
    return key


def validate_matrix_key(matrix_key: list[list[int]], dimension: int = 3):
    if not isinstance(dimension, int):
        raise TypeError('Введенная размерность не является целым числом')
    if not dimension > 2:
        raise ValueError('Введенная размерность должна быть не меньше 3')
    for row in matrix_key:
        if len(row) != dimension:
            raise ValueError(f'Введенная матрица не имеет размерность {dimension}x{dimension}')
    
    matrix_key = np.array(matrix_key)
    determinant = np.linalg.det(matrix_key)
    
    if determinant == 0:
        raise ValueError('Матрица вырождена (определитель равен нулю).')
    
    return matrix_key
