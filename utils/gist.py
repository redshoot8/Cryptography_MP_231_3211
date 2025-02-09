import matplotlib.pyplot as plt
from collections import Counter


def plot_letter_count(text):
    # Создание словаря для подсчета частоты букв
    letter_counts = Counter(char.lower() for char in text if char.isalpha())

    # Получение списка всех используемых букв
    categories = sorted(set('абвгдежзийклмнопрстуфхцчшщъыьэюя'))

    # Создание списка встречаемости букв
    counts = [letter_counts.get(letter, 0) for letter in categories]

    # Построение гистограммы
    plt.figure(figsize=(7.5, 5))
    plt.bar(categories, counts)
    plt.title('Гистограмма частоты букв в тексте')
    plt.xlabel('Буквы')
    plt.ylabel('Количество')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_number_count(number_list):
    frequency = {}
    
    # Разбиваем строку на отдельные числа
    numbers = number_list.split()
    
    # Считаем частоту каждого числа
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Создаем список значений для графика
    values = list(frequency.values())
    
    # Создаем список ключей (чисел) для оси X
    keys = sorted(frequency.keys())
    
    # Создаем столбчатую диаграмму
    plt.figure(figsize=(7.5, 5))
    plt.bar(keys, values)
    plt.title('Частота чисел в строке')
    plt.xlabel('Числа')
    plt.ylabel('Частота')
    plt.xticks(rotation=45)  # Поворачиваем метки оси X на 45 градусов
    plt.tight_layout()
    plt.show()
