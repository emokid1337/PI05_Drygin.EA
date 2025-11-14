def binary_search(arr, left, right, target):
    """Вспомогательная функция бинарного поиска"""
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    """
    Экспоненциальный поиск - находит диапазон, где может находиться элемент,
    затем выполняет бинарный поиск в этом диапазоне.
    """
    n = len(arr)
    
    # Если элемент в начале массива
    if arr[0] == target:
        return 0
    
    # Находим диапазон для бинарного поиска
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    
    # Выполняем бинарный поиск в найденном диапазоне
    return binary_search(arr, i // 2, min(i, n - 1), target)

# Пример использования
arr = [2, 3, 4, 10, 40, 45, 50, 60, 70, 80, 90, 100]
target = 45
print(f"Массив: {arr}")
print(f"Поиск элемента {target}: индекс {exponential_search(arr, target)}")
