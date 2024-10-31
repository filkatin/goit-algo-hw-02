from collections import deque

def is_palindrome(s):
    # Приводимо рядок до нижнього регістру та видаляємо пробіли
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Додаємо всі символи до двосторонньої черги
    char_deque = deque(normalized_str)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклади використання
print(is_palindrome("У дива на виду"))  # True
print(is_palindrome("Абабагаламага"))  # False
print(is_palindrome("Сир і рис"))  # True
print(is_palindrome("кіт утік"))  # True
