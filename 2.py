def flip(arr, i):
    """Переворачивает массив от 0 до i-го элемента"""
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max_index(arr, n):
    """Находит индекс максимального элемента в массиве до n-го элемента"""
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    """
    Блинная сортировка - сортирует массив, переворачивая его части,
    как будто переворачиваем стопку блинов.
    """
    n = len(arr)
    
    # Начинаем с конца массива и постепенно уменьшаем размер
    for curr_size in range(n, 1, -1):
        # Находим индекс максимального элемента в несортированной части
        max_index = find_max_index(arr, curr_size)
        
        # Если максимальный элемент не на своем месте
        if max_index != curr_size - 1:
            # Переворачиваем так, чтобы максимальный элемент оказался в начале
            if max_index != 0:
                flip(arr, max_index)
            
            # Переворачиваем так, чтобы максимальный элемент оказался на своем месте
            flip(arr, curr_size - 1)
    
    return arr

# Пример использования
arr = [23, 10, 20, 11, 12, 6, 7]
print("Исходный массив:", arr)
print("Отсортированный массив:", pancake_sort(arr.copy()))