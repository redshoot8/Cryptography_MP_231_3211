from utils.validation import validate_matrix_key


def get_test_case(filename: str = '../data/test_case.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            string = file.readline().strip()
            return string
    except FileNotFoundError:
        print(f'Ошибка: Файл {filename} не найден.')
        return None
    except Exception as e:
        print(f'Произошла ошибка при чтении файла: {e}')
        return None


def get_matrix_key():
    while True:
        try:
            matrix_key = []
            for _ in range(3):
                row = list(map(int, input('Введите элементы матрицы 3x3 построчно (через пробел): ').split()))
                matrix_key.append(row)
            matrix_key = validate_matrix_key(matrix_key)
            return matrix_key
        except ValueError as e:
            print(f'Ошибка: {e}')
