import queue
import random
import time

request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    # Ідентифікатор заявки — унікальне число
    request_id = random.randint(1000, 9999)
    request = f"Заявка #{request_id}"
    print(f"Генерація нової заявки: {request}")
    # Додаємо заявку до черги
    request_queue.put(request)

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        # Видаляємо заявку з черги
        request = request_queue.get()
        print(f"Обробка {request}...")
        # Імітація обробки заявки
        time.sleep(random.uniform(0.5, 1.5))
        print(f"{request} успішно оброблена!")
    else:
        print("Чекаю нових заявок...")

# Головний цикл програми
def main():
    for _ in range(10):
        # Імітація потоку нових заявок
        if random.choice([True, False]):
            generate_request()

        process_request()

        time.sleep(1)

main()
print("Програма завершена.")
