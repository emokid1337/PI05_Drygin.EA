def ternary_search(arr, target):
    """
    Тернарный поиск - делит массив на три части и рекурсивно
    ищет в соответствующей части.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Делим текущий отрезок на три части
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # Проверяем, не нашли ли элемент в точках деления
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        # Определяем, в какой части продолжать поиск
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

# Рекурсивная версия тернарного поиска
def ternary_search_recursive(arr, left, right, target):
    if left > right:
        return -1
    
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    
    if target < arr[mid1]:
        return ternary_search_recursive(arr, left, mid1 - 1, target)
    elif target > arr[mid2]:
        return ternary_search_recursive(arr, mid2 + 1, right, target)
    else:
        return ternary_search_recursive(arr, mid1 + 1, mid2 - 1, target)

# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
print(f"Массив: {arr}")
print(f"Итеративный поиск элемента {target}: индекс {ternary_search(arr, target)}")
print(f"Рекурсивный поиск элемента {target}: индекс {ternary_search_recursive(arr, 0, len(arr)-1, target)}")
