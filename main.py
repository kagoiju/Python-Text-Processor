# (Итерация 2: Реализован ввод данных, заглушки для алгоритма)

from menu_template import start_menu
import random
import re # Добавлен для будущей реализации clean_text, пока не используется

# ГЛОБАЛЬНОЕ СОСТОЯНИЕ
data_input = None       # Введенный текст
algorithm_result = None # Результат работы алгоритма
data_present = False    # Флаг: True, если данные введены
result_present = False  # Флаг: True, если алгоритм выполнен

# ФУНКЦИИ ВВОДА ДАННЫХ (Реализация)

def input_data_manually():
    """Ручной ввод данных."""
    global data_input, data_present, result_present
    print("\n--- 1.1) Ручной ввод данных ---")
    data = input("Введите текст: ")
    if data.strip():
        data_input = data.strip()
        data_present = True
        result_present = False  # Сброс результата при вводе новых данных
        print(f"Данные введены: '{data_input[:50]}...'")
    else:
        print("⚠️ Введена пустая строка. Данные не обновлены.")
    input("Нажмите Enter для продолжения...")

def input_data_randomly():
    """Случайная генерация данных."""
    global data_input, data_present, result_present
    
    words = ["Алгоритм", "Питон", "программирование", "результат", "согласные", "гласные", "тест", "данные"]
    separators = [" ", ", ", ". ", "! "]
    random_text = ""
    
    # Генерируем случайный текст из 5-15 слов с разделителями
    for _ in range(random.randint(5, 15)):
        random_text += random.choice(words)
        random_text += random.choice(separators)
    
    data_input = random_text.strip()
    data_present = True
    result_present = False # Сброс результата при вводе новых данных
    print("\n--- 1.2) Случайная генерация данных ---")
    print(f"Сгенерирован текст: {data_input}")
    input("Нажмите Enter для продолжения...")

def menu_input_data():
    """Подменю для выбора способа ввода."""
    caption_start = "\n--- 1) Ввод данных ---\n1) Ввести вручную\n2) Сгенерировать случайно\n0) Назад\n"
    caption_err = 'Некорректный выбор.'
    menu_template = {
        0: (lambda: True, True),
        1: (input_data_manually, True),
        2: (input_data_randomly, True)
    }
    start_menu(caption_start, caption_err, menu_template)

# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ АЛГОРИТМА (Заглушки) ---

def clean_text(text: str) -> list:
    """ЗАГЛУШКА: Очистка текста и разделение на слова."""
    print(">>> [Stub] clean_text: Имитация очистки и разделения.")
    # Имитация: просто разбиваем по пробелам, игнорируя реальную очистку
    words = text.lower().replace('.', '').replace(',', '').split()
    return words

def count_vowels_consonants(word: str) -> tuple:
    """ЗАГЛУШКА: Подсчет гласных и согласных в слове."""
    print(f">>> [Stub] count_vowels_consonants: Подсчет для слова '{word}'.")
    
    # Имитация подсчета
    word_len = len(word)
    vowels = min(2, word_len) # минимум 2 гласные
    consonants = word_len - vowels 
    if consonants < 0: consonants = 0
    
    return (vowels, consonants) 

# --- ОСНОВНЫЕ ФУНКЦИИ ПРИЛОЖЕНИЯ ---

def execute_algorithm():
    """Выполнение алгоритма по заданию (использует заглушки)."""
    global algorithm_result, result_present, data_present
    if not data_present:
        print("!!! Ошибка: Сначала необходимо ввести исходные данные (Пункт 1).")
        return

    print("\n--- 2) Выполнение алгоритма ---")
    
    words = clean_text(data_input) # Используем заглушку
    
    word_stats = []
    total_vowels = 0
    for word in words:
        v, c = count_vowels_consonants(word) # Используем заглушку
        word_stats.append((word, v, c))
        total_vowels += v

    # Результат: массив троек + общее количество гласных в тексте (последний элемент)
    algorithm_result = word_stats + [total_vowels]
    result_present = True
    print("Алгоритм (пока что заглушка) выполнен.")
    input("Нажмите Enter для продолжения...")

def display_result():
    """Вывод результата (Пункт 3)."""
    global algorithm_result, result_present, data_present
    
    if not data_present:
        print("!!! Ошибка: Сначала необходимо ввести исходные данные (Пункт 1).")
        return
    if not result_present:
        print("!!! Ошибка: Сначала необходимо выполнить алгоритм (Пункт 2).")
        return

    print("\n--- 3) Результат ---")
    print(f"Входные данные: {data_input}")
    print("--- Анализ слов ---")
    # Выводим тройки
    for item in algorithm_result[:-1]:
        word, v, c = item
        print(f"Слово: '{word}' | Гласные: {v} | Согласные: {c}")
    
    # Выводим общее количество гласных
    print(f"\nОбщее количество гласных в тексте: {algorithm_result[-1]}")
    print("--------------------\n")
    input("Нажмите Enter для продолжения...")


def menu_main():
    """Главное меню приложения."""
    # Отображение текущего состояния в заголовке меню
    while True:
        data_status = 'ВВЕДЕНЫ' if data_present else 'НЕТ'
        result_status = 'ГОТОВ' if result_present else 'НЕТ'
        caption_start = f"\n--- ГЛАВНОЕ МЕНЮ (Данные: {data_status} | Результат: {result_status})---\n" \
                        "1) Ввод исходных данных\n" \
                        "2) Выполнение алгоритма по заданию\n" \
                        "3) Вывод результата\n" \
                        "0) Завершение работы программы\n"
                        
        caption_err = 'Некорректный выбор.'
        menu_template = {
            0: (lambda: print("Завершение работы."), True),
            1: (menu_input_data, False),
            2: (execute_algorithm, False),
            3: (display_result, False)
        }
        # Цикл меню
        if start_menu(caption_start, caption_err, menu_template):
            break

if __name__ == "__main__":
    menu_main()