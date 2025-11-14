import math

def jump_search(arr, target):
    """
    Поиск скачками - прыгает с фиксированным шагом по массиву,
    затем выполняет линейный поиск в найденном блоке.
    """
    n = len(arr)
    
    # Определяем размер прыжка (обычно квадратный корень из n)
    step = int(math.sqrt(n))
    
    # Находим блок, где может находиться элемент
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Выполняем линейный поиск в найденном блоке
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    # Если элемент найден
    if arr[prev] == target:
        return prev
    
    return -1

# Пример использования
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
target = 55
print(f"Массив: {arr}")
print(f"Поиск элемента {target}: индекс {jump_search(arr, target)}")
