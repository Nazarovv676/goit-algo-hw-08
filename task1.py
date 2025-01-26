import heapq

def min_cost_to_connect_cables(cables):
    # Перетворюємо список кабелів в купу
    heapq.heapify(cables)
    
    total_cost = 0
    steps = []  # Для збереження кроків з'єднання кабелів

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Вибираємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Витрати на з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost
        
        # Додаємо новий об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)
        
        # Зберігаємо поточний стан списку кабелів
        steps.append(list(cables))  # Копіюємо список на кожному кроці

    return total_cost, steps

# Приклад використання
cables = [4, 3, 2, 6]  # Довжини кабелів
result, steps = min_cost_to_connect_cables(cables)

# Виведення результатів
print(f"Загальні витрати на з'єднання кабелів: {result}")
print("Порядок з'єднання кабелів (стан після кожного кроку):")
for i, step in enumerate(steps, 1):
    print(f"Крок {i}: {step}")